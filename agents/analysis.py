"""
Advanced Analysis Agent - Creates strategic insights
"""

from models.state import MarketingState
from skills.llm_client import llm_client

class AnalysisAgent:
    """Agent that analyzes research for strategic insights"""
    
    AGENT_NAME = "Advanced Analysis Agent"
    
    @staticmethod
    def run(state: MarketingState) -> MarketingState:
        """Run strategic analysis"""
        print(f"\n📊 [{AnalysisAgent.AGENT_NAME}] Analyzing research...")
        
        analysis_prompt = f"""
        Based on this research:
        {state.get('research_data', 'No research data')}
        
        Create a strategic analysis with:
        
        1. SWOT ANALYSIS
           - Strengths: What makes this content idea strong?
           - Weaknesses: What are potential risks?
           - Opportunities: What angles are underexplored?
           - Threats: What could make this fail?
        
        2. RECOMMENDED CONTENT ANGLE
           - The single best angle to take
           - Why this angle will resonate
        
        3. PLATFORM STRATEGY
           - Primary platform (with reasoning)
           - Secondary platforms
           - Platform-specific adaptations needed
        
        4. TIMING STRATEGY
           - Best day of week to publish
           - Best time of day
           - Any seasonal or event-based timing
        
        5. MESSAGING PILLARS
           - 3-5 core messages to repeat throughout the content
        
        Make strategic recommendations, not just observations.
        """
        
        analysis = llm_client.call(
            analysis_prompt,
            "You are a senior marketing strategist. Provide clear, actionable recommendations."
        )
        
        state["analysis_data"] = analysis
        
        print(f"\n✅ Analysis complete! ({len(analysis)} characters)")
        return state