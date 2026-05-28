import os
from google import genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def generate_page(filename, topic):
    print(f"DEBUG: Generating {filename}...")
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"Write a short 300-word article about: {topic}"
        )
        content = response.text
    except Exception as e:
        content = f"<h1>API ERROR</h1><p>{str(e)}</p>"
        print(f"DEBUG: Error in {filename}: {str(e)}")

    # Use a basic structure
    with open(filename, "w") as f:
        f.write(f"<html><body><h1>{topic}</h1>{content}</body></html>")
    print(f"DEBUG: Saved {filename}")

if __name__ == "__main__":
    generate_page("index.html", "Evolution of business")
    generate_page("automation.html", "Building sales funnels")
    generate_page("courses.html", "Online course creation")
