import os
import google.generativeai as genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Instead of naming a specific model, we list available ones
# and pick the first one that supports text generation.
def get_working_model():
    models = genai.list_models()
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            return genai.GenerativeModel(m.name)
    return None

model = get_working_model()

if model:
    response = model.generate_content("Write a promotional blurb for Systeme.io.")
    with open("index.html", "w") as f:
        f.write(f"<html><body>{response.text}</body></html>")
else:
    print("No usable models found.")
    exit(1)


