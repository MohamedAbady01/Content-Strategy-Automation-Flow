"""
Input/output validators for content and user inputs
"""

from typing import Tuple, List, Dict, Any
import re

class Validator:
    """Validates user inputs and agent outputs"""
    
    @staticmethod
    def validate_brief(brief: str) -> Tuple[bool, str]:
        """
        Validate user content brief
        
        Args:
            brief: The user's content brief
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not brief:
            return False, "Brief is empty. Please provide content details."
        
        if len(brief.strip()) < 10:
            return False, "Brief is too short. Please provide at least 10 characters describing your content need."
        
        if len(brief) > 5000:
            return False, "Brief is too long. Please keep under 5000 characters."
        
        # Check for minimum required information
        required_keywords = ["audience", "topic", "content"]
        has_required = any(keyword in brief.lower() for keyword in required_keywords)
        
        if not has_required:
            return False, "Brief should mention target audience, topic, or content type."
        
        return True, "Valid"
    
    @staticmethod
    def validate_rating(rating: int) -> Tuple[bool, str]:
        """
        Validate rating is between 1-10
        
        Args:
            rating: The rating value
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not isinstance(rating, int):
            return False, "Rating must be a number"
        
        if 1 <= rating <= 10:
            return True, "Valid"
        
        return False, f"Rating must be between 1 and 10, got {rating}"
    
    @staticmethod
    def validate_content(content: str, min_length: int = 50, max_length: int = 10000) -> Tuple[bool, List[str]]:
        """
        Validate generated content quality
        
        Args:
            content: The generated content
            min_length: Minimum acceptable length
            max_length: Maximum acceptable length
        
        Returns:
            Tuple of (is_valid, list_of_issues)
        """
        issues = []
        
        if not content:
            issues.append("Content is empty")
            return False, issues
        
        if len(content) < min_length:
            issues.append(f"Content is too short ({len(content)} chars). Minimum {min_length} characters.")
        
        if len(content) > max_length:
            issues.append(f"Content is very long ({len(content)} chars). Consider breaking into parts.")
        
        # Check for essential content elements
        essential_patterns = {
            "title/r": r'(?i)(title|headline|header)',
            "content": r'(?i)(content|body|main|section)',
            "call_to_action": r'(?i)(call to action|cta|click|subscribe|buy|learn more|sign up)'
        }
        
        for element, pattern in essential_patterns.items():
            if not re.search(pattern, content):
                issues.append(f"Missing or weak {element.replace('_', ' ')}")
        
        # Check for placeholder text
        placeholder_patterns = [
            r'\[.*?\]',  # [placeholder]
            r'{.*?}',     # {placeholder}
            r'<.*?>',     # <placeholder>
            r'\(.*?\)',   # (placeholder) - less strict, only check common ones
        ]
        
        for pattern in placeholder_patterns:
            if re.search(pattern, content):
                issues.append(f"Contains placeholder text matching: {pattern}")
                break
        
        # Check for basic structure (paragraphs, line breaks)
        if len(content.split()) < 50 and len(content.splitlines()) < 3:
            issues.append("Content lacks structure. Add paragraphs or sections.")
        
        return len(issues) == 0, issues
    
    @staticmethod
    def validate_platform(platform: str) -> Tuple[bool, str]:
        """
        Validate platform name
        
        Args:
            platform: Platform name
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        valid_platforms = [
            "linkedin", "twitter", "x", "instagram", "facebook", 
            "tiktok", "youtube", "blog", "email", "website", 
            "medium", "substack", "newsletter"
        ]
        
        if not platform:
            return False, "Platform not specified"
        
        platform_lower = platform.lower().strip()
        
        for valid in valid_platforms:
            if valid in platform_lower or platform_lower in valid:
                return True, "Valid"
        
        return True, "Unknown platform but proceeding"  # Warning, not error
    
    @staticmethod
    def validate_timeline(timeline: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate timeline structure
        
        Args:
            timeline: Timeline dictionary
        
        Returns:
            Tuple of (is_valid, list_of_issues)
        """
        issues = []
        
        required_keys = [
            "start_date", "content_ready", "publish_date"
        ]
        
        for key in required_keys:
            if key not in timeline:
                issues.append(f"Missing timeline key: {key}")
        
        # Check date ordering if dates exist
        try:
            if "start_date" in timeline and "publish_date" in timeline:
                start = datetime.strptime(timeline["start_date"], "%Y-%m-%d")
                publish = datetime.strptime(timeline["publish_date"], "%Y-%m-%d")
                
                if publish < start:
                    issues.append("Publish date is before start date")
                
                days_diff = (publish - start).days
                if days_diff < 1:
                    issues.append("Publish date is too close to start date")
                if days_diff > 30:
                    issues.append("Timeline is very long (>30 days)")
        except (ValueError, KeyError):
            issues.append("Invalid date format in timeline")
        
        return len(issues) == 0, issues
    
    @staticmethod
    def validate_conversation_history(history: List[Dict]) -> Tuple[bool, str]:
        """
        Validate conversation history structure
        
        Args:
            history: List of conversation exchanges
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        if not isinstance(history, list):
            return False, "Conversation history must be a list"
        
        for exchange in history:
            if not isinstance(exchange, dict):
                return False, "Each exchange must be a dictionary"
            
            # Should have either 'agent' or 'user' key
            if 'agent' not in exchange and 'user' not in exchange:
                return False, "Exchange missing 'agent' or 'user' key"
        
        return True, "Valid"
    
    @staticmethod
    def sanitize_brief(brief: str) -> str:
        """
        Clean and sanitize user brief
        
        Args:
            brief: Raw user input
        
        Returns:
            Sanitized brief
        """
        # Remove extra whitespace
        brief = ' '.join(brief.split())
        
        # Remove any obvious sensitive info (emails, phone numbers)
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        
        brief = re.sub(email_pattern, '[EMAIL REDACTED]', brief)
        brief = re.sub(phone_pattern, '[PHONE REDACTED]', brief)
        
        return brief.strip()
    
    @staticmethod
    def get_content_stats(content: str) -> Dict[str, Any]:
        """
        Get statistics about generated content
        
        Args:
            content: The content to analyze
        
        Returns:
            Dictionary with content statistics
        """
        words = content.split()
        sentences = re.split(r'[.!?]+', content)
        paragraphs = content.split('\n\n')
        
        return {
            "characters": len(content),
            "words": len(words),
            "sentences": len([s for s in sentences if s.strip()]),
            "paragraphs": len([p for p in paragraphs if p.strip()]),
            "avg_word_length": sum(len(w) for w in words) / len(words) if words else 0,
            "estimated_read_time_minutes": round(len(words) / 200, 1)  # 200 words per minute
        }


# Import datetime for date validation (used in validate_timeline)
from datetime import datetime