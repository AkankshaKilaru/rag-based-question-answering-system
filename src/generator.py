import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(persona, context, query):

    prompt = f"""
You are a customer support assistant.

Detected Persona:
{persona}

Retrieved Knowledge Base:
{context}

User Query:
{query}

IMPORTANT RULES:
1. Answer ONLY using the retrieved knowledge base.
2. Mention specific troubleshooting steps from the knowledge base.
3. Do not make up information.
4. Be persona-aware.

Technical Expert:
- Detailed technical explanation
- Root cause analysis
- Technical troubleshooting steps

Frustrated User:
- Show empathy
- Give clear step-by-step instructions
- Avoid technical jargon

Business Executive:
- Concise answer
- Focus on business impact and resolution

Provide a direct answer.
"""

    try:
        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text

        return str(response)

    except Exception as e:
        return f"Error generating response: {str(e)}"