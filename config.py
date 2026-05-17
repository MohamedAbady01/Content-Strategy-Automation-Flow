"""
Configuration file for API keys and settings
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================
# LLM PROVIDER CONFIGURATION
# ============================================

# Choose your provider: "gemini", "groq", or "mock"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")  # Changed to groq by default

# Google Gemini API (backup)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-1.5-flash"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

# Groq API (Recommended - Very Fast, Free)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.3-70b-versatile"  # Best free model on Groq

# Alternative Groq models:
# - "llama-3.3-70b-versatile" (best quality)
# - "llama-3.1-8b-instant" (faster)
# - "mixtral-8x7b-32768" (good for long context)

# ============================================
# WORKFLOW CONFIGURATION
# ============================================

# Rating thresholds
IDEA_RATING_THRESHOLD = 7
FINAL_RATING_THRESHOLD = 7

# Maximum revision attempts
MAX_REVISIONS = 3

# Output directory
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)