import os
import google.generativeai as genai

# Configure the library
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# List all models you have permission to access
print("Checking available models...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Available Model ID: {m.name}")
