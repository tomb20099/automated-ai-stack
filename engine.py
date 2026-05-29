import os
from google import genai

# Setup
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

topics = {
    "index.html": "Welcome to my AI automation hub",
    "automation-tips.html": "Top 5 tips for AI business automation"
}

def generate_content(filename, topic):
    print(f"ATTEMPTING: {topic}...")
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"Write a short page about: {topic}"
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"<html><body><h1>{topic}</h1>{response.text}</body></html>")
        print(f"SUCCESS: {filename}")
    except Exception as e:
        # Instead of crashing, we print the error and continue
        print(f"SKIPPING {topic} due to API limit: {e}")

if __name__ == "__main__":
    for filename, topic in topics.items():
        generate_content(filename, topic)
