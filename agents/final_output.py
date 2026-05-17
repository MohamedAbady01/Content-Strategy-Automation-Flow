"""
Final Output Agent - Packages all deliverables
"""

from models.state import MarketingState
from skills.timeline import generate_timeline, generate_launch_checklist
from datetime import datetime
import json
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import config
    OUTPUT_DIR = getattr(config, 'OUTPUT_DIR', 'outputs')
except ImportError:
    OUTPUT_DIR = "outputs"

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

class FinalOutputAgent:
    """Agent that packages final deliverables"""
    
    AGENT_NAME = "Final Output Agent"
    
    @staticmethod
    def run(state: MarketingState) -> MarketingState:
        """Package final deliverables"""
        print(f"\n📦 [{FinalOutputAgent.AGENT_NAME}] Packaging final deliverables...")
        
        # Generate timeline and checklist
        timeline = generate_timeline()
        launch_checklist = generate_launch_checklist(timeline)
        
        final_deliverable = {
            "project_metadata": {
                "name": state.get("brief", "Untitled Project")[:80],
                "created_at": datetime.now().isoformat(),
                "revision_count": state.get("revision_count", 0)
            },
            
            "content": {
                "full_text": state.get("created_content", "No content generated"),
                "word_count": len(state.get("created_content", "").split())
            },
            
            "publishing_timeline": timeline,
            
            "publishing_plan": state.get("publishing_plan", "No plan generated"),
            
            "key_performance_indicators": {
                "primary_kpi": "Engagement Rate > 5%",
                "secondary_kpis": [
                    "Views: 10,000+",
                    "Shares: 500+",
                    "Click-through: 3%+",
                    "Conversions: 100+"
                ]
            },
            
            "launch_checklist": launch_checklist,
            
            "next_steps": [
                f"📅 Publish on: {timeline.get('publish_date', 'N/A')}",
                "📊 Monitor first 24 hours closely",
                "🔄 Repurpose top-performing content after 7 days",
                "📈 Report results to stakeholders"
            ]
        }
        
        state["final_deliverable"] = final_deliverable
        
        # Save to file
        output_filename = f"{OUTPUT_DIR}/marketing_deliverable_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(final_deliverable, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Deliverable saved to: {output_filename}")
        
        # Print summary
        print("\n" + "=" * 70)
        print("🎉 FINAL DELIVERABLE SUMMARY 🎉")
        print("=" * 70)
        print(f"\n📝 Content length: {final_deliverable['content']['word_count']} words")
        print(f"📅 Publish date: {timeline.get('publish_date', 'N/A')}")
        print(f"🔄 Revision count: {state.get('revision_count', 0)}")
        print("\n📋 Launch Checklist:")
        for item in launch_checklist:
            print(f"   {item}")
        print("=" * 70)
        
        return state