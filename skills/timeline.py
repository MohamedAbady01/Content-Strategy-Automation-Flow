"""
Timeline generation utilities
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional

class TimelineGenerator:
    """Generates publishing timelines and schedules"""
    
    def generate_timeline(self, start_date: Optional[datetime] = None) -> Dict[str, str]:
        """
        Generate a day-by-day timeline for content production
        
        Args:
            start_date: Optional custom start date. Defaults to now.
        
        Returns:
            Dictionary with timeline milestones and dates
        """
        if start_date is None:
            start_date = datetime.now()
        
        return {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "start_time": start_date.strftime("%Y-%m-%d %H:%M:%S"),
            
            # Production milestones
            "research_complete": (start_date + timedelta(days=1)).strftime("%Y-%m-%d"),
            "analysis_complete": (start_date + timedelta(days=1, hours=12)).strftime("%Y-%m-%d %H:%M"),
            "content_ready": (start_date + timedelta(days=2)).strftime("%Y-%m-%d"),
            "design_complete": (start_date + timedelta(days=3)).strftime("%Y-%m-%d"),
            "review_complete": (start_date + timedelta(days=4)).strftime("%Y-%m-%d"),
            
            # Publishing milestones
            "publish_date": (start_date + timedelta(days=5)).strftime("%Y-%m-%d"),
            "publish_time": (start_date + timedelta(days=5, hours=9)).strftime("%Y-%m-%d %H:%M"),
            
            # Promotion milestones
            "promotion_start": (start_date + timedelta(days=5, hours=2)).strftime("%Y-%m-%d %H:%M"),
            "first_boost": (start_date + timedelta(days=6)).strftime("%Y-%m-%d"),
            "second_boost": (start_date + timedelta(days=8)).strftime("%Y-%m-%d"),
            
            # Review milestones
            "first_review": (start_date + timedelta(days=12)).strftime("%Y-%m-%d"),
            "performance_report": (start_date + timedelta(days=14)).strftime("%Y-%m-%d"),
            "optimization_day": (start_date + timedelta(days=21)).strftime("%Y-%m-%d"),
        }
    
    @staticmethod
    def generate(start_date: Optional[datetime] = None) -> Dict[str, str]:
        """Static method version for backwards compatibility"""
        generator = TimelineGenerator()
        return generator.generate_timeline(start_date)
    
    def get_milestones(self, timeline: Dict[str, str]) -> List[Dict[str, str]]:
        """Convert timeline dictionary to milestone list for tracking"""
        milestones = [
            {"milestone": "Research Phase", "date": timeline.get("research_complete", "N/A"), "status": "pending", "priority": "high"},
            {"milestone": "Strategic Analysis", "date": timeline.get("analysis_complete", "N/A"), "status": "pending", "priority": "high"},
            {"milestone": "Content Creation", "date": timeline.get("content_ready", "N/A"), "status": "pending", "priority": "high"},
            {"milestone": "Design & Visuals", "date": timeline.get("design_complete", "N/A"), "status": "pending", "priority": "medium"},
            {"milestone": "Review & Approval", "date": timeline.get("review_complete", "N/A"), "status": "pending", "priority": "high"},
            {"milestone": "PUBLISH", "date": timeline.get("publish_date", "N/A"), "status": "pending", "priority": "critical"},
            {"milestone": "Promotion Begins", "date": timeline.get("promotion_start", "N/A"), "status": "pending", "priority": "high"},
            {"milestone": "Performance Review", "date": timeline.get("first_review", "N/A"), "status": "pending", "priority": "medium"},
        ]
        return milestones
    
    def print_timeline(self, timeline: Dict[str, str]) -> None:
        """Pretty print the timeline to console"""
        print("\n" + "=" * 60)
        print("📅 CONTENT PUBLISHING TIMELINE")
        print("=" * 60)
        
        print(f"\n🚀 START: {timeline.get('start_date', 'N/A')}")
        print(f"🔍 Research Complete: {timeline.get('research_complete', 'N/A')}")
        print(f"📊 Analysis Complete: {timeline.get('analysis_complete', 'N/A')}")
        print(f"✍️ Content Ready: {timeline.get('content_ready', 'N/A')}")
        print(f"🎨 Design Complete: {timeline.get('design_complete', 'N/A')}")
        print(f"✅ Review Complete: {timeline.get('review_complete', 'N/A')}")
        print(f"\n📢 PUBLISH DATE: {timeline.get('publish_date', 'N/A')} at 9:00 AM")
        print(f"📣 Promotion Start: {timeline.get('promotion_start', 'N/A')}")
        print(f"📈 First Review: {timeline.get('first_review', 'N/A')}")
        print("=" * 60)
    
    @staticmethod
    def generate_launch_checklist(timeline: Dict[str, str]) -> List[str]:
        """Generate a launch checklist based on timeline"""
        return [
            f"✅ Content reviewed and approved by {timeline.get('review_complete', 'review date')}",
            "✅ Images/visuals created and optimized",
            "✅ Links and UTM parameters added for tracking",
            "✅ Scheduled in publishing tool (Buffer/Hootsuite/etc.)",
            "✅ Team notified for launch day engagement",
            "✅ Tracking dashboard set up",
            f"✅ Pre-launch promotion scheduled for {timeline.get('promotion_start', 'promotion date')}",
            f"✅ Ready to publish on {timeline.get('publish_date', 'publish date')}"
        ]


# Module-level functions for easy importing
def generate_timeline(start_date: Optional[datetime] = None) -> Dict[str, str]:
    """Module-level function to generate timeline"""
    return TimelineGenerator.generate(start_date)

def generate_launch_checklist(timeline: Dict[str, str]) -> List[str]:
    """Module-level function to generate launch checklist"""
    return TimelineGenerator.generate_launch_checklist(timeline)