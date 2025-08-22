import os
from groq import Groq
from utils import normalize_text, compute_hash

class AIContentGenerator:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("Missing GROQ_API_KEY. Please set it in your environment.")
        self.client = Groq(api_key=api_key)

    def generate(self, prompt: str):
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "You are a helpful assistant. Always reply in only 2-3 concise lines."},
                      {"role": "user", "content": prompt}],
            temperature=0.7,
        )
        content = response.choices[0].message.content
        normalized = normalize_text(content)
        content_hash = compute_hash({"content": normalized})
        return content, content_hash
