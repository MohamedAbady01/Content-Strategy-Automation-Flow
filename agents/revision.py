"""
Revision Agent - Improves content based on feedback
"""

from models.state import MarketingState
from skills.llm_client import llm_client
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

class RevisionAgent:
    """Agent that revises content based on user feedback"""
    
    AGENT_NAME = "Revision Agent"
    
    @staticmethod
    def run(state: MarketingState) -> MarketingState:
        """Revise content based on feedback"""
        print(f"\n🔄 [{RevisionAgent.AGENT_NAME}] Revising content...")
        
        if state.get("revision_count", 0) >= config.MAX_REVISIONS:
            print(f"⚠️ Max revisions ({config.MAX_REVISIONS}) reached. Proceeding with current version.")
            return state
        
        revision_prompt = f"""
        ORIGINAL CONTENT:
        {state['created_content']}
        
        USER FEEDBACK:
        {state.get('final_feedback', 'No specific feedback. Make it better.')}
        
        STRATEGY CONTEXT:
        {state['analysis_data']}
        
        Please revise the content to address the feedback. Focus on:
        1. Addressing specific criticisms
        2. Adding more value and examples
        3. Improving clarity and flow
        4. Making the call-to-action stronger
        
        Keep the same format and length, just improve quality.
        """
        
        revised_content = llm_client.call(
            revision_prompt,
            "You are an expert editor who improves content based on feedback."
        )
        
        state["created_content"] = revised_content
        state["revision_count"] = state.get("revision_count", 0) + 1
        
        print(f"✅ Revision #{state['revision_count']} complete!")
        return state