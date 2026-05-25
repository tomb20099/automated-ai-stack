import os
import google.generativeai as genai

# Configure
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Dynamically find a valid model
def get_model():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods and 'flash' in m.name:
            print(f"Using model: {m.name}")
            return genai.GenerativeModel(m.name)
    # Fallback to a standard name if no flash model is dynamically found
    return genai.GenerativeModel("gemini-1.5-flash")

model = get_model()

# Generate
prompt = "Write a one-sentence marketing hook for Systeme.io."
response = model.generate_content(prompt)

# Save
with open("daily_output.txt", "w") as f:
    f.write(response.text)

