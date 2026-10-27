import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv("../.env")

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    "Say hello in one sentence."
)

print(response.text)