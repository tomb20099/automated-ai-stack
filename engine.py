import os
from google import genai

# Setup
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Topics to generate - only these will be created if they don't exist
topics = {
    "automation-tips.html": "Top 5 tips for AI business automation",
    "sales-funnel-guide.html": "How to build your first AI-driven sales funnel",
    "ai-productivity.html": "How AI tools save 10 hours a week"
}

def generate_content(filename, topic):
    # SAFETY CHECK: If it exists, skip it!
    if os.path.exists(filename):
        print(f"SKIPPING: {filename} already exists.")
        return

    print(f"GENERATING: {topic}...")
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"Write a 500-word SEO-optimized article about: {topic}"
        )
        with open(filename, "w") as f:
            f.write(f"<html><body><h1>{topic}</h1>{response.text}</body></html>")
        print(f"SAVED: {filename}")
    except Exception as e:
        print(f"FAILED: {topic} - {e}")

if __name__ == "__main__":
    for filename, topic in topics.items():
        generate_content(filename, topic)
