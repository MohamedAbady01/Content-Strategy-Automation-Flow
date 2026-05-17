"""
State management for LangGraph workflow
"""

from typing import TypedDict, List, Dict, Any, Optional
from datetime import datetime

class MarketingState(TypedDict):
    """
    State object passed between all agents in the workflow
    
    This state accumulates data as it flows through the graph
    """
    # User input
    brief: str
    conversation_history: List[Dict[str, str]]
    
    # Gate 1: Idea rating
    idea_rating: int
    idea_feedback: str
    idea_approved: bool
    
    # Research outputs
    research_data: str
    analysis_data: str
    
    # Content outputs
    created_content: str
    publishing_plan: str
    
    # Gate 2: Final rating
    final_rating: int
    final_feedback: str
    revision_count: int
    final_approved: bool
    
    # Final output
    final_deliverable: Dict[str, Any]
    
    # Metadata
    created_at: str
    updated_at: str

def create_initial_state(brief: str) -> MarketingState:
    """Create initial state with default values"""
    now = datetime.now().isoformat()
    
    return {
        "brief": brief,
        "conversation_history": [],
        "idea_rating": 0,
        "idea_feedback": "",
        "idea_approved": False,
        "research_data": "",
        "analysis_data": "",
        "created_content": "",
        "publishing_plan": "",
        "final_rating": 0,
        "final_feedback": "",
        "revision_count": 0,
        "final_approved": False,
        "final_deliverable": {},
        "created_at": now,
        "updated_at": now
    }