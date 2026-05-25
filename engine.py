import os
import google.generativeai as genai

# Securely grab your hidden Gemini API Key from GitHub Secrets
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY secret is missing!")

# Configure the library
genai.configure(api_key=api_key)

# Use the established model
model = genai.GenerativeModel("gemini-1.5-flash-001")


marketing_prompt = (
    "You are an expert SaaS affiliate marketer. Generate a unique, highly engaging 60-second "
    "video script for Systeme.io. Include a hook, problem, solution, CTA, and visual cues."
)

response = model.generate_content(marketing_prompt)

# Append to output file
with open("daily_output.txt", "a+", encoding="utf-8") as f:
    f.write("\n--- NEW SCRIPT ---\n")
    f.write(response.text)
    f.write("\n")
