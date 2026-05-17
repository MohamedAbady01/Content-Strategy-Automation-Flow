"""
LangGraph workflow definition - INTERACTIVE VERSION
"""

from models.state import MarketingState, create_initial_state
from agents.brainstorming import BrainstormingAgent
from agents.research import ResearchAgent
from agents.analysis import AnalysisAgent
from agents.content_creator import ContentCreatorAgent
from agents.publishing import PublishingPlanAgent
from agents.revision import RevisionAgent
from agents.final_output import FinalOutputAgent
from skills.rating_gates import RatingGate

class MarketingWorkflow:
    """Manages the LangGraph workflow execution - INTERACTIVE"""
    
    def __init__(self, use_mock: bool = False):
        """
        Initialize workflow
        
        Args:
            use_mock: Set to False for real user interaction, True for testing
        """
        self.use_mock = use_mock
        
    def run(self, brief: str) -> MarketingState:
        """
        Execute the complete marketing workflow with REAL USER INTERACTION
        """
        
        print("\n" + "=" * 70)
        print("🚀 MARKETING STRATEGY LANGGRAPH WORKFLOW 🚀")
        print("=" * 70)
        print(f"\n📝 Your Brief: {brief}")
        
        # Initialize state
        state = create_initial_state(brief)
        
        # ========== STEP 1: INTERACTIVE BRAINSTORMING ==========
        print("\n" + "🎯" * 35)
        print("STEP 1: BRAINSTORMING & CLARIFICATION")
        print("🎯" * 35)
        state = BrainstormingAgent.run(state)
        
        # ========== GATE 1: USER RATES THE IDEA ==========
        rating, approved, feedback = RatingGate.rate_idea(
            state["brief"], 
            state["conversation_history"],
            use_mock=self.use_mock  # Pass mock flag
        )
        state["idea_rating"] = rating
        state["idea_feedback"] = feedback
        
        if not approved:
            print("\n❌ Workflow terminated: Idea rating too low")
            print("💡 Please refine your brief and try again.")
            return state
        
        # ========== STEP 2: RESEARCH ==========
        print("\n" + "🔍" * 35)
        print("STEP 2: DEEP RESEARCH")
        print("🔍" * 35)
        print("Researching your topic... (this may take a moment)")
        state = ResearchAgent.run(state)
        
        # ========== STEP 3: ANALYSIS ==========
        print("\n" + "📊" * 35)
        print("STEP 3: STRATEGIC ANALYSIS")
        print("📊" * 35)
        print("Analyzing research data...")
        state = AnalysisAgent.run(state)
        
        # ========== STEP 4: CONTENT CREATION ==========
        print("\n" + "✍️" * 35)
        print("STEP 4: CONTENT CREATION")
        print("✍️" * 35)
        print("Creating your content... (this may take a moment)")
        state = ContentCreatorAgent.run(state)
        
        # ========== STEP 5: PUBLISHING PLAN ==========
        print("\n" + "📅" * 35)
        print("STEP 5: PUBLISHING PLAN")
        print("📅" * 35)
        print("Creating your publishing timeline...")
        state = PublishingPlanAgent.run(state)
        
        # ========== GATE 2: USER RATES FINAL ==========
        final_rating, final_approved, feedback, content_rate, plan_rate = RatingGate.rate_final(
            state["created_content"],
            state["publishing_plan"],
            use_mock=self.use_mock  # Pass mock flag
        )
        state["final_rating"] = final_rating
        state["final_feedback"] = feedback
        
        # ========== REVISION LOOP ==========
        revision_count = 0
        max_revisions = 3
        
        while not final_approved and revision_count < max_revisions:
            print(f"\n🔄 Revision attempt {revision_count + 1}/{max_revisions}")
            
            # Revise content
            state = RevisionAgent.run(state)
            
            # Re-rate with user
            final_rating, final_approved, feedback, content_rate, plan_rate = RatingGate.rate_final(
                state["created_content"],
                state["publishing_plan"],
                use_mock=self.use_mock
            )
            state["final_rating"] = final_rating
            state["final_feedback"] = feedback
            revision_count += 1
            state["revision_count"] = revision_count
        
        if not final_approved:
            print(f"\n⚠️ Max revisions ({max_revisions}) reached. Proceeding with current version.")
            if not self.use_mock:
                user_choice = input("Do you want to proceed anyway? (y/n): ").strip().lower()
                if user_choice != 'y':
                    print("Workflow terminated by user.")
                    return state
        
        # ========== FINAL OUTPUT ==========
        print("\n" + "📦" * 35)
        print("STEP 6: FINAL DELIVERABLES")
        print("📦" * 35)
        state = FinalOutputAgent.run(state)
        
        print("\n" + "=" * 70)
        print("✅ WORKFLOW COMPLETE! ✅")
        print("=" * 70)
        
        return state