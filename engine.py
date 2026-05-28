import os
from google import genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

pages = {
    "index.html": "The evolution of digital business.",
    "automation.html": "Building an automated sales funnel.",
    "courses.html": "Structuring an online course."
}

def create_file(filename, topic):
    print(f"--- Attempting to create {filename} ---")
    try:
        # Prompting for content
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=f"Write a short 300-word article about: {topic}"
        )
        content = response.text
    except Exception as e:
        content = f"<h1>Generation Failed</h1><p>Error: {e}</p>"
        print(f"ERROR: Could not generate {filename}: {e}")

    # Fallback to a basic file if template missing
    template = "<html><body>{CONTENT}</body></html>"
    if os.path.exists("template.html"):
        with open("template.html", "r") as f:
            template = f.read()
            
    with open(filename, "w") as f:
        f.write(template.replace("{CONTENT}", content))
    print(f"Successfully wrote {filename}")

if __name__ == "__main__":
    for filename, topic in pages.items():
        create_file(filename, topic)
