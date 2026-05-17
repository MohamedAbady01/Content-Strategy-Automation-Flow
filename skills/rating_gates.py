"""
Rating gates for human-in-the-loop validation - INTERACTIVE VERSION
"""

from typing import Tuple, Optional
import sys
import os

# Add parent directory to path to import config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import config
    IDEA_RATING_THRESHOLD = getattr(config, 'IDEA_RATING_THRESHOLD', 7)
    FINAL_RATING_THRESHOLD = getattr(config, 'FINAL_RATING_THRESHOLD', 7)
except ImportError:
    IDEA_RATING_THRESHOLD = 7
    FINAL_RATING_THRESHOLD = 7

class RatingGate:
    """Handles user rating interactions - INTERACTIVE"""
    
    @staticmethod
    def rate_idea(brief: str, conversation_history: list, use_mock: bool = False) -> Tuple[int, bool, str]:
        """
        Gate 1: User rates the initial idea - INTERACTIVE
        
        Args:
            brief: The user's content brief
            conversation_history: List of brainstorming exchanges
            use_mock: If True, auto-approve. If False, ask user.
        
        Returns:
            Tuple of (rating, is_approved, feedback)
        """
        print("\n" + "=" * 60)
        print("⭐ GATE 1: RATE THE IDEA")
        print("=" * 60)
        print(f"\n📝 Your brief: {brief[:200]}...")
        print(f"\n💬 Brainstorming completed: {len(conversation_history)} exchanges")
        
        if use_mock:
            # Mock mode for testing
            rating = 8
            feedback = "Good idea, proceed (mock mode)"
            print(f"\n📊 Auto-rating: {rating}/10 (mock mode)")
        else:
            # REAL USER INTERACTION
            print("\n" + "=" * 50)
            print("📣 YOUR TURN TO RATE THE IDEA")
            print("=" * 50)
            
            while True:
                try:
                    rating = int(input("\n📊 On a scale of 1-10, how good is this idea? (1=poor, 10=excellent): "))
                    if 1 <= rating <= 10:
                        break
                    else:
                        print("❌ Please enter a number between 1 and 10")
                except ValueError:
                    print("❌ Please enter a valid number")
                except KeyboardInterrupt:
                    print("\n\n❌ Operation cancelled by user")
                    return 0, False, "Cancelled by user"
            
            feedback = input("\n💬 Optional feedback (what could be improved?): ").strip()
            if not feedback:
                feedback = "No specific feedback provided"
        
        is_approved = rating >= IDEA_RATING_THRESHOLD
        
        if is_approved:
            print(f"\n✅ APPROVED! Rating: {rating}/10 (needs {IDEA_RATING_THRESHOLD}+)")
            print("   Moving to research and content creation...")
        else:
            print(f"\n❌ REJECTED. Rating: {rating}/10 (needs {IDEA_RATING_THRESHOLD}+)")
            print("   Please provide a better brief or clarify your idea.")
        
        return rating, is_approved, feedback
    
    @staticmethod
    def rate_final(content: str, plan: str, use_mock: bool = False) -> Tuple[float, bool, str, int, int]:
        """
        Gate 2: User rates the final content and plan - INTERACTIVE
        
        Args:
            content: The generated content
            plan: The publishing plan
            use_mock: If True, auto-approve. If False, ask user.
        
        Returns:
            Tuple of (avg_rating, is_approved, feedback, content_rating, plan_rating)
        """
        print("\n" + "=" * 60)
        print("⭐ GATE 2: RATE FINAL DELIVERABLE")
        print("=" * 60)
        
        print("\n📝 YOUR GENERATED CONTENT:")
        print("-" * 40)
        # Show first 800 chars or full content if shorter
        if len(content) > 800:
            print(content[:800])
            print(f"\n... (content continues, total {len(content)} characters)")
            show_more = input("\n👉 Show more? (y/n): ").strip().lower()
            if show_more == 'y':
                print("\n" + content[800:1600])
                if len(content) > 1600:
                    print(f"\n... (and {len(content) - 1600} more characters)")
        else:
            print(content)
        
        print("\n📅 YOUR PUBLISHING PLAN:")
        print("-" * 40)
        print(plan[:500] + "..." if len(plan) > 500 else plan)
        
        if use_mock:
            # Mock mode for testing
            content_rating = 8
            plan_rating = 8
            feedback = "Great work! (mock mode)"
            print(f"\n📊 Auto-rating - Content: {content_rating}/10, Plan: {plan_rating}/10 (mock mode)")
        else:
            # REAL USER INTERACTION
            print("\n" + "=" * 50)
            print("📣 YOUR TURN TO RATE THE CONTENT")
            print("=" * 50)
            
            while True:
                try:
                    content_rating = int(input("\n📊 Rate the CONTENT (1-10): "))
                    if 1 <= content_rating <= 10:
                        break
                    else:
                        print("❌ Please enter a number between 1 and 10")
                except ValueError:
                    print("❌ Please enter a valid number")
                except KeyboardInterrupt:
                    print("\n\n❌ Operation cancelled by user")
                    return 0, False, "Cancelled", 0, 0
            
            while True:
                try:
                    plan_rating = int(input("\n📊 Rate the PUBLISHING PLAN (1-10): "))
                    if 1 <= plan_rating <= 10:
                        break
                    else:
                        print("❌ Please enter a number between 1 and 10")
                except ValueError:
                    print("❌ Please enter a valid number")
                except KeyboardInterrupt:
                    print("\n\n❌ Operation cancelled by user")
                    return 0, False, "Cancelled", 0, 0
            
            feedback = input("\n💬 Feedback for revision (optional): ").strip()
            if not feedback:
                feedback = "No specific feedback"
        
        avg_rating = (content_rating + plan_rating) / 2
        is_approved = avg_rating >= FINAL_RATING_THRESHOLD
        
        if is_approved:
            print(f"\n✅ APPROVED! Average rating: {avg_rating:.1f}/10 (needs {FINAL_RATING_THRESHOLD}+)")
            print("   Publishing final deliverables...")
        else:
            print(f"\n❌ NEEDS REVISION. Average rating: {avg_rating:.1f}/10 (needs {FINAL_RATING_THRESHOLD}+)")
            print("   Revision agent will improve the content based on your feedback...")
        
        return avg_rating, is_approved, feedback, content_rating, plan_rating