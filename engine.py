import os
import google.generativeai as genai

# Setup API
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate Content
try:
    response = model.generate_content("Write a promotional blurb for Systeme.io.")
    # Ensure content is simple text to avoid file encoding issues
    with open("index.html", "w") as f:
        f.write(f"<html><body>{response.text}</body></html>")
except Exception as e:
    print(f"Error: {e}")
    exit(1)

