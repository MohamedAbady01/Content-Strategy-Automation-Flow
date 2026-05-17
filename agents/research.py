"""
Deep Research Agent - Gathers data about the topic
"""

from models.state import MarketingState
from skills.llm_client import llm_client

class ResearchAgent:
    """Agent that performs deep research"""
    
    AGENT_NAME = "Deep Research Agent"
    
    @staticmethod
    def run(state: MarketingState) -> MarketingState:
        """Run deep research"""
        print(f"\n🔍 [{ResearchAgent.AGENT_NAME}] Researching topic...")
        
        research_prompt = f"""
        Topic: "{state.get('brief', 'No brief')}"
        
        Conversation history: {state.get('conversation_history', [])}
        
        Provide a comprehensive research report including:
        
        1. CURRENT TRENDS
           - What's trending right now on this topic?
           - Recent news or developments?
        
        2. COMPETITOR ANALYSIS
           - What are others doing on this topic?
           - What's working well for them?
           - What gaps can we fill?
        
        3. KEYWORD OPPORTUNITIES
           - Primary keywords
           - Long-tail keywords
           - Question-based keywords (what people are asking)
        
        4. AUDIENCE INSIGHTS
           - Pain points
           - Desires and goals
           - Objections to overcome
        
        5. PERFORMANCE INSIGHTS
           - What content formats work best for this niche?
           - Best posting times?
           - Expected engagement metrics
        
        Format as clear sections with bullet points.
        """
        
        research = llm_client.call(
            research_prompt,
            "You are a data-driven marketing researcher. Provide factual, actionable insights."
        )
        
        state["research_data"] = research
        
        print(f"\n✅ Research complete! ({len(research)} characters)")
        return state