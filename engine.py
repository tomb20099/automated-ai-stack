import os
from google import genai

# Correctly pull the API key from the GitHub Secrets environment
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("DEBUG ERROR: GEMINI_API_KEY is not set in GitHub Secrets!")
    client = None
else:
    client = genai.Client(api_key=api_key)

# Define the pages
pages = {
    "index.html": "The evolution of digital business and why all-in-one platforms are replacing fragmented tool stacks.",
    "automation.html": "A guide on building a stress-free automated sales funnel for beginners.",
    "courses.html": "How to structure and launch your first online course for maximum student success."
}

def generate_content(topic):
    if client is None:
        return "<h1>Configuration Error</h1><p>API Key is missing.</p>"
    
    prompt = f"Write a 600-word educational guide about: {topic}. Use HTML tags (<h2>, <h3>, <p>, <ul>, <li>)."
    try:
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        return response.text
    except Exception as e:
        # This will print the exact error to your GitHub Action logs
        print(f"DEBUG ERROR: {e}") 
        return f"<h1>Generation Failed</h1><p>Error details: {e}</p>"

if __name__ == "__main__":
    if not os.path.exists("template.html"):
        print("Error: template.html not found.")
        exit(1)

    with open("template.html", "r") as f:
        template = f.read()

    for filename, topic in pages.items():
        print(f"Working on {filename}...")
        content = generate_content(topic)
        final_html = template.replace("{CONTENT}", content)
        
        with open(filename, "w") as f:
            f.write(final_html)
        print(f"Finished {filename}")
