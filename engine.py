import os
import google.generativeai as genai

# Fetch the key
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Instead of a hardcoded string that might cause 404s, let's list available models
# to ensure we pick one that exists for your specific API key.
# However, for now, let's try 'gemini-1.5-flash' again but ensure the library is fresh.
model = genai.GenerativeModel("gemini-1.5-flash")

prompt = "Write a one-sentence marketing hook for Systeme.io."
response = model.generate_content(prompt)

with open("daily_output.txt", "w") as f:
    f.write(response.text)
