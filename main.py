"""
Main entry point for Marketing Strategy LangGraph - INTERACTIVE VERSION
"""

import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from workflow.graph import MarketingWorkflow

def main():
    """Main function to run the interactive workflow"""
    
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║     MARKETING STRATEGY LANGGRAPH - AI Content Agency        ║
    ║                          INTERACTIVE MODE                    ║
    ║                                                              ║
    ║  I'll help you create publish-ready content with:           ║
    ║  • Interactive brainstorming (I'll ask questions)           ║
    ║  • Deep research & analysis                                 ║
    ║  • Full content creation (blog, carousel, video, etc.)      ║
    ║  • Publishing timeline & plan                               ║
    ║  • You rate everything at each step!                        ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Ask user if they want mock mode or real mode
    print("\n" + "=" * 50)
    print("⚙️  SETUP")
    print("=" * 50)
    print("\nDo you want to:")
    print("  1. REAL MODE - I'll ask you questions and you rate the content")
    print("  2. MOCK MODE - Auto-approve everything (for testing)")
    
    mode_choice = input("\n👉 Choose (1 or 2): ").strip()
    use_mock = mode_choice == "2"
    
    if use_mock:
        print("\n⚠️  Running in MOCK MODE - no user interaction required")
    else:
        print("\n✅ Running in REAL MODE - I'll interact with you throughout the process")
    
    # Get user input
    print("\n" + "=" * 50)
    print("📝 YOUR CONTENT BRIEF")
    print("=" * 50)
    print("\nEnter your content brief (or press Enter for example):")
    print("   Example: 'Create a LinkedIn carousel about 5 ChatGPT prompts...'\n")
    
    user_input = input("👉 Brief: ").strip()
    
    if not user_input:
        # Example brief
        user_input = """Create a LinkedIn carousel titled '5 ChatGPT Prompts That Save Small Business Owners 10 Hours Per Week'
        
Target audience: Small business owners, freelancers, and entrepreneurs who are overwhelmed with daily tasks.
Goal: Get 1000+ views, 100+ saves, and 50+ newsletter signups.
Tone: Educational but fun, with real examples they can copy-paste.
Platform: LinkedIn and Twitter/X"""
        print(f"\n📌 Using example brief:\n{user_input}")
    
    # Confirm with user
    print("\n" + "=" * 50)
    print("✅ FINAL CHECK")
    print("=" * 50)
    confirm = input("\nReady to start? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Workflow cancelled.")
        return
    
    # Run workflow with interactive mode
    workflow = MarketingWorkflow(use_mock=use_mock)
    result = workflow.run(user_input)
    
    # Print final result
    if result.get("final_deliverable"):
        print("\n" + "🎉" * 35)
        print("🎉 WORKFLOW COMPLETE! 🎉")
        print("🎉" * 35)
        print(f"\n✅ Content created successfully!")
        print(f"📁 Project: {result['final_deliverable']['project_metadata']['name'][:50]}...")
        
        # Ask if user wants to save content
        save_option = input("\n💾 Save content to text file? (y/n): ").strip().lower()
        if save_option == 'y':
            filename = input("Filename (default: output.txt): ").strip()
            if not filename:
                filename = "output.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(result["final_deliverable"]["content"]["full_text"])
            print(f"✅ Content saved to {filename}")
        
        # Ask if user wants to see the JSON deliverable
        json_option = input("\n📄 See full JSON deliverable? (y/n): ").strip().lower()
        if json_option == 'y':
            import json
            print("\n" + "=" * 50)
            print(json.dumps(result["final_deliverable"], indent=2)[:2000])
            print("\n... (output truncated)")
    else:
        print("\n❌ Workflow did not complete successfully.")
        if result.get("idea_rating", 0) < 7:
            print("   Reason: Your idea rating was below 7.")
            print("   Try again with a more specific or valuable content idea.")

if __name__ == "__main__":
    main()