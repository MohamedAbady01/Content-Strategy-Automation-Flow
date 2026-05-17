"""
Brainstorming Agent - INTERACTIVE - Asks user questions
"""

from models.state import MarketingState
from skills.llm_client import llm_client

class BrainstormingAgent:
    """Agent that asks clarifying questions - INTERACTIVE"""
    
    AGENT_NAME = "Brainstorming Agent"
    
    @staticmethod
    def run(state: MarketingState) -> MarketingState:
        """Run interactive brainstorming process"""
        print(f"\n🤔 [{BrainstormingAgent.AGENT_NAME}] Let me understand your idea better...")
        
        # Generate questions based on brief
        questions_prompt = f"""
        Based on this brief: "{state.get('brief', 'No brief')}"
        
        Generate 4 specific, targeted questions to help understand:
        1. Target audience (who exactly are we talking to? Be specific!)
        2. Desired outcome (what should the audience do after seeing this?)
        3. Tone and style (formal, funny, educational, inspirational, controversial?)
        4. Platform (which specific platform? LinkedIn, Twitter, Instagram, TikTok, Blog?)
        5. Unique angle (what makes this different from what's already out there?)
        
        Output as a simple numbered list of questions, one per line.
        Make questions conversational and easy to answer.
        """
        
        questions = llm_client.call(
            questions_prompt,
            "You are a strategic marketing consultant. Ask smart, targeted, easy-to-answer questions."
        )
        
        print(f"\n💬 Brainstorming Questions:")
        print("-" * 40)
        print(questions)
        print("-" * 40)
        
        # COLLECT USER ANSWERS INTERACTIVELY
        print("\n" + "=" * 50)
        print("📣 YOUR TURN - Please answer the questions")
        print("=" * 50)
        
        user_answers = []
        question_lines = questions.strip().split('\n')
        
        for i, question in enumerate(question_lines, 1):
            # Clean up question number if present
            clean_question = question.strip()
            if clean_question and not clean_question.startswith('Based'):
                # Remove numbering if exists
                if clean_question[0].isdigit() and '.' in clean_question[:3]:
                    clean_question = clean_question.split('.', 1)[1].strip()
                
                answer = input(f"\n❓ {clean_question}\n👉 ").strip()
                if answer:
                    user_answers.append(f"Q{i}: {clean_question}\nA: {answer}")
                else:
                    user_answers.append(f"Q{i}: {clean_question}\nA: [No answer provided]")
        
        # Combine all answers
        full_conversation = "\n\n".join(user_answers)
        
        print("\n" + "=" * 50)
        print("✅ Thank you! I understand your project better now.")
        print("=" * 50)
        
        state["conversation_history"] = [
            {"agent": "brainstorming", "questions": questions},
            {"user": full_conversation}
        ]
        
        return state