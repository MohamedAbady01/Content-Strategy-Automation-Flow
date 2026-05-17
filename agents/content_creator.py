"""
Content Creation Agent - Creates the actual content (SUPERPOWER)
"""

from models.state import MarketingState
from skills.llm_client import llm_client
from skills.validators import Validator  # Add this import

class ContentCreatorAgent:
    """Agent that creates publish-ready content"""
    
    AGENT_NAME = "Content Creation Agent"
    
    @staticmethod
    def run(state: MarketingState) -> MarketingState:
        """Create the actual content"""
        print(f"\n✍️ [{ContentCreatorAgent.AGENT_NAME}] Creating actual content...")
        
        # Determine best content format based on analysis
        format_decision = llm_client.call(
            f"""
            Based on: {state.get('analysis_data', 'No analysis data')}
            
            What content format would work BEST for this audience and goal?
            Choose ONE: blog_post, linkedin_carousel, video_script, ad_copy, email_sequence, twitter_thread
            
            Just output the format name, nothing else.
            """,
            "You choose the optimal format."
        )
        
        format_map = {
            "blog_post": ContentCreatorAgent._create_blog_post,
            "linkedin_carousel": ContentCreatorAgent._create_carousel,
            "video_script": ContentCreatorAgent._create_video_script,
            "ad_copy": ContentCreatorAgent._create_ad_copy,
            "email_sequence": ContentCreatorAgent._create_email_sequence,
            "twitter_thread": ContentCreatorAgent._create_twitter_thread,
        }
        
        selected_format = format_decision.strip().lower()
        creator_func = format_map.get(selected_format, ContentCreatorAgent._create_blog_post)
        
        content = creator_func(state)
        
        # Validate content - Now Validator is imported
        is_valid, issues = Validator.validate_content(content)
        if not is_valid:
            print(f"⚠️ Content validation issues: {issues}")
            # Still proceed but log issues
        
        state["created_content"] = content
        
        print(f"\n📝 CONTENT CREATED ({selected_format}):")
        print("=" * 60)
        print(content[:800] + "..." if len(content) > 800 else content)
        print("=" * 60)
        
        return state
    
    @staticmethod
    def _create_blog_post(state: MarketingState) -> str:
        """Create a blog post"""
        prompt = f"""
        Create a complete, publish-ready blog post based on:
        
        Brief: {state.get('brief', 'No brief')}
        Research: {state.get('research_data', 'No research')}
        Strategy: {state.get('analysis_data', 'No analysis')}
        
        Include:
        - SEO-optimized title (with primary keyword)
        - Introduction with hook (question, statistic, or story)
        - 5-7 body sections with H2 and H3 subheadings
        - Real examples or actionable tips
        - Conclusion summarizing key points
        - Clear call-to-action
        - Meta description (150-160 characters)
        - 5-10 suggested tags/keywords
        
        Make it engaging, scannable, and valuable.
        """
        
        return llm_client.call(
            prompt,
            "You are an expert blog writer who creates engaging, SEO-optimized content."
        )
    
    @staticmethod
    def _create_carousel(state: MarketingState) -> str:
        """Create a LinkedIn/Instagram carousel"""
        prompt = f"""
        Create a complete carousel (8-10 slides) based on:
        
        Brief: {state.get('brief', 'No brief')}
        Strategy: {state.get('analysis_data', 'No analysis')}
        
        Output format:
        
        SLIDE 1 (Hook):
        Text: [Headline that grabs attention]
        
        SLIDE 2-8:
        Text: [Key points with examples]
        
        SLIDE 9 (CTA):
        Text: [Call to action]
        
        Also include:
        - Caption for the post (150-200 words with hashtags)
        - Visual descriptions for each slide
        
        Make each slide digestible and punchy.
        """
        
        return llm_client.call(
            prompt,
            "You create high-engagement social media carousels."
        )
    
    @staticmethod
    def _create_video_script(state: MarketingState) -> str:
        """Create a video script"""
        prompt = f"""
        Create a video script (60-90 seconds) based on:
        
        Brief: {state.get('brief', 'No brief')}
        Strategy: {state.get('analysis_data', 'No analysis')}
        
        Format:
        
        HOOK (0-5 sec): [First words to stop scroll]
        
        BODY (5-60 sec): 
        [Visual description]
        [Narration/ Voiceover]
        
        CTA (60-90 sec): [What viewer should do next]
        
        Also include:
        - Estimated duration
        - Suggested background music mood
        - Thumbnail concept
        """
        
        return llm_client.call(
            prompt,
            "You write viral video scripts for TikTok, Reels, and Shorts."
        )
    
    @staticmethod
    def _create_ad_copy(state: MarketingState) -> str:
        """Create ad copy"""
        prompt = f"""
        Create ad copy based on:
        
        Brief: {state.get('brief', 'No brief')}
        Strategy: {state.get('analysis_data', 'No analysis')}
        
        Provide:
        
        VERSION A:
        - Headline: [Short, punchy, benefit-driven]
        - Primary Text: [50-80 words]
        - Description: [20-30 words]
        - CTA Button: [e.g., Learn More, Sign Up]
        
        VERSION B (A/B test variant):
        - Headline: [Different angle]
        - Primary Text: [Different hook]
        - Description: [Different benefit]
        - CTA Button: [Different action]
        
        Also include:
        - Visual direction suggestion
        - Ad platform recommendation
        """
        
        return llm_client.call(
            prompt,
            "You write high-converting ad copy."
        )
    
    @staticmethod
    def _create_email_sequence(state: MarketingState) -> str:
        """Create email sequence"""
        prompt = f"""
        Create a 3-email sequence based on:
        
        Brief: {state.get('brief', 'No brief')}
        Strategy: {state.get('analysis_data', 'No analysis')}
        
        EMAIL 1 (Welcome/Intro):
        - Subject Line
        - Preheader
        - Body (3-4 short paragraphs)
        - CTA
        
        EMAIL 2 (Value/Education):
        - Subject Line
        - Body (tips, insights)
        - CTA
        
        EMAIL 3 (Conversion/Urgency):
        - Subject Line
        - Body (social proof, scarcity)
        - CTA
        
        Also include:
        - Send timing (days after signup)
        - Personalization opportunities
        """
        
        return llm_client.call(
            prompt,
            "You write email sequences that get opened, clicked, and converted."
        )
    
    @staticmethod
    def _create_twitter_thread(state: MarketingState) -> str:
        """Create Twitter/X thread"""
        prompt = f"""
        Create a Twitter thread (10-15 tweets) based on:
        
        Brief: {state.get('brief', 'No brief')}
        Strategy: {state.get('analysis_data', 'No analysis')}
        
        Format each tweet with numbers:
        
        1/12 [Hook tweet]
        2/12 [Value point 1]
        3/12 [Example]
        ...
        12/12 [Call to action + hashtags]
        
        Also include:
        - Media suggestions per tweet
        - Engagement hook in reply
        """
        
        return llm_client.call(
            prompt,
            "You write Twitter threads that go viral."
        )