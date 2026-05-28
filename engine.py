import os
from google import genai

# Setup
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Topics to generate
topics = {
    "index.html": "Welcome to my AI automation hub", # Make sure one is index.html
    "automation-tips.html": "Top 5 tips for AI business automation",
    "sales-funnel-guide.html": "How to build your first AI-driven sales funnel",
    "ai-productivity.html": "How AI tools save 10 hours a week"
}

def generate_content(filename, topic):
    print(f"GENERATING/UPDATING: {filename}...")
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"Write a 500-word SEO-optimized article about: {topic}"
        )
        # Always write (or overwrite) the file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"<html><body><h1>{topic}</h1>{response.text}</body></html>")
        print(f"SAVED: {filename}")
    except Exception as e:
        print(f"FAILED: {topic} - {e}")

if __name__ == "__main__":
    for filename, topic in topics.items():
        generate_content(filename, topic)
