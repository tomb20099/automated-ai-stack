import os
import google.generativeai as genai

# Fetch the key from environment
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Use the stable pro model
model = genai.GenerativeModel("gemini-1.5-pro")

# Generate content
prompt = "Write a one-sentence marketing hook for Systeme.io."
response = model.generate_content(prompt)

# Save to file
with open("daily_output.txt", "w") as f:
    f.write(response.text)
