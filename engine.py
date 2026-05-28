import os
import time
from google import genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Ensure the 'public' directory exists
os.makedirs("public", exist_ok=True)

pages = {
    "public/index.html": "The evolution of digital business.",
    "public/automation.html": "Building an automated sales funnel.",
    "public/courses.html": "Structuring an online course."
}

def generate_page(filepath, topic):
    print(f"DEBUG: Generating {filepath}...")
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"Write a short 300-word article about: {topic}"
        )
        content = response.text
    except Exception as e:
        content = f"<h1>API ERROR</h1><p>{str(e)}</p>"
        print(f"DEBUG: Error in {filepath}: {str(e)}")

    with open(filepath, "w") as f:
        f.write(f"<html><body><h1>{topic}</h1>{content}</body></html>")
    print(f"DEBUG: Saved {filepath}")

if __name__ == "__main__":
    for filepath, topic in pages.items():
        generate_page(filepath, topic)
        print("Waiting 60 seconds...")
        time.sleep(60)
