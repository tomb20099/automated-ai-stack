import os
import time
from google import genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

pages = {
    "index.html": "The evolution of digital business.",
    "automation.html": "Building an automated sales funnel.",
    "courses.html": "Structuring an online course."
}

def generate_page(filename, topic):
    print(f"DEBUG: Generating {filename}...")
    try:
        # Generate content
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"Write a short 300-word article about: {topic}"
        )
        content = response.text
    except Exception as e:
        content = f"<h1>API ERROR</h1><p>{str(e)}</p>"
        print(f"DEBUG: Error in {filename}: {str(e)}")

    # Save to file
    with open(filename, "w") as f:
        f.write(f"<html><body><h1>{topic}</h1>{content}</body></html>")
    print(f"DEBUG: Saved {filename}")

if __name__ == "__main__":
    for filename, topic in pages.items():
        generate_page(filename, topic)
        # Wait 60 seconds between requests to avoid 429 Resource Exhausted errors
        print("Waiting 60 seconds for API rate limits...")
        time.sleep(60)
