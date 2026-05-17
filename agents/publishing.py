"""
Publishing Plan Agent - Creates timeline and distribution plan
"""

from models.state import MarketingState
from skills.llm_client import llm_client
from skills.timeline import generate_timeline

class PublishingPlanAgent:
    """Agent that creates publishing timeline and plan"""
    
    AGENT_NAME = "Publishing Plan Agent"
    
    @staticmethod
    def run(state: MarketingState) -> MarketingState:
        """Create publishing plan"""
        print(f"\n📅 [{PublishingPlanAgent.AGENT_NAME}] Creating publishing plan...")
        
        # Generate timeline
        timeline = generate_timeline()
        
        plan_prompt = f"""
        Based on the strategy: {state.get('analysis_data', 'No analysis data available')}
        
        Create a detailed publishing plan including:
        
        1. PLATFORM SELECTION
           - Primary platform (why)
           - Secondary platforms (how to repurpose)
        
        2. POSTING SCHEDULE
           - Best days and times
           - Frequency (daily, weekly, etc.)
        
        3. DISTRIBUTION STRATEGY
           - Organic: hashtags, tagging, engagement
           - Paid: budget suggestion, targeting
        
        4. PROMOTION CALENDAR
           - Pre-launch (2 days before)
           - Launch day (hour by hour)
           - Post-launch (next 7 days)
        
        5. TEAM ROLES
           - Who does what
           - Approval process
        
        Be specific with dates and times.
        """
        
        plan_details = llm_client.call(
            plan_prompt,
            "You are a social media strategist and project manager."
        )
        
        # Combine timeline and plan
        full_plan = f"""
📅 TIMELINE
{'-' * 40}
Start: {timeline.get('start_date', 'N/A')}
Research done: {timeline.get('research_complete', 'N/A')}
Content ready: {timeline.get('content_ready', 'N/A')}
Design complete: {timeline.get('design_complete', 'N/A')}
Review done: {timeline.get('review_complete', 'N/A')}
PUBLISH: {timeline.get('publish_date', 'N/A')}
Promotion: {timeline.get('promotion_start', 'N/A')}
Review results: {timeline.get('first_review', 'N/A')}

📋 DETAILED PLAN
{'-' * 40}
{plan_details}

🎯 KPIs TO TRACK
{'-' * 40}
- Views/Impressions: Target 10,000+
- Engagement Rate: Target 5%+
- Shares/Retweets: Target 500+
- Click-through Rate: Target 3%+
- Conversions: Target 100+
"""
        
        state["publishing_plan"] = full_plan
        
        print(f"\n✅ Publishing plan complete!")
        return state