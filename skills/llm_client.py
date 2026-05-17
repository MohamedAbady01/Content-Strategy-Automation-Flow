"""
LLM Client - Handles communication with free LLM APIs
"""

import requests
import json
from typing import Optional
import sys
import os

# Add parent directory to path to import config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import config
except ImportError:
    class Config:
        LLM_PROVIDER = "mock"
        GEMINI_API_KEY = ""
        GEMINI_MODEL = "gemini-1.5-flash"
        GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
        GROQ_API_KEY = ""
        GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
        GROQ_MODEL = "llama-3.3-70b-versatile"
    config = Config()

class LLMClient:
    """Client for interacting with free LLM providers"""
    
    def __init__(self):
        self.provider = getattr(config, 'LLM_PROVIDER', 'mock')
        
    def call(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Call the LLM with a prompt
        
        Args:
            prompt: User prompt
            system_prompt: System instruction (optional)
            
        Returns:
            LLM response as string
        """
        if self.provider == "gemini":
            return self._call_gemini(prompt, system_prompt)
        elif self.provider == "groq":
            return self._call_groq(prompt, system_prompt)
        else:
            return self._call_mock(prompt, system_prompt)
    
    def _call_gemini(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Call Google Gemini API"""
        full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        
        model = getattr(config, 'GEMINI_MODEL', 'gemini-1.5-flash')
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        
        payload = {
            "contents": [{
                "parts": [{"text": full_prompt}]
            }]
        }
        
        try:
            api_key = getattr(config, 'GEMINI_API_KEY', '')
            if not api_key:
                return "[Error] Gemini API key not configured. Please set GEMINI_API_KEY in config.py"
            
            response = requests.post(
                f"{url}?key={api_key}",
                json=payload,
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json()["candidates"][0]["content"]["parts"][0]["text"]
            else:
                return f"[Error] Gemini API: {response.status_code} - {response.text[:200]}"
        except Exception as e:
            return f"[Error] Failed to call Gemini: {str(e)}"
    
    def _call_groq(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Call Groq API (Llama 3)"""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        payload = {
            "model": getattr(config, 'GROQ_MODEL', 'llama-3.3-70b-versatile'),
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 4096
        }
        
        headers = {
            "Authorization": f"Bearer {getattr(config, 'GROQ_API_KEY', '')}",
            "Content-Type": "application/json"
        }
        
        try:
            api_key = getattr(config, 'GROQ_API_KEY', '')
            if not api_key:
                return "[Error] Groq API key not configured. Please set GROQ_API_KEY in config.py"
            
            if not api_key.startswith("gsk_"):
                return "[Error] Invalid Groq API key format. Keys should start with 'gsk_'"
            
            response = requests.post(
                config.GROQ_URL,
                json=payload,
                headers=headers,
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"[Error] Groq API: {response.status_code} - {response.text[:200]}"
        except Exception as e:
            return f"[Error] Failed to call Groq: {str(e)}"
    
    def _call_mock(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Mock LLM for testing without API keys"""
        return f"""[MOCK RESPONSE - Set up API key for real content]

Based on your request about Michael Jackson's journey, here's a sample response:

MICHAEL JACKSON: THE KING OF POP'S JOURNEY

Michael Jackson's journey from child star to global icon is one of the most remarkable stories in music history. Born in Gary, Indiana in 1958, he began performing with his brothers in The Jackson 5 at just 6 years old.

Key milestones in his journey:
- 1979: "Off the Wall" - His first solo masterpiece
- 1982: "Thriller" - The best-selling album of all time
- 1983: Moonwalk debut on Motown 25
- 1985: Co-wrote "We Are the World"
- 1988: Purchased Neverland Ranch

His legacy continues to influence artists across all genres, from pop to hip-hop to rock.

(This is mock content. Get a free API key from Groq or Gemini for real AI-generated content!)"""

# Global instance
llm_client = LLMClient()