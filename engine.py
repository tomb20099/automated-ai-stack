import os
from google import genai

client = genai.Client()

# Define the pages we want to create
pages = {
    "index.html": "The evolution of digital business and why all-in-one platforms are replacing fragmented tool stacks.",
    "automation.html": "A guide on building a stress-free automated sales funnel for beginners.",
    "courses.html": "How to structure and launch your first online course for maximum student success."
}

def generate_content(topic):
    # Using a simple, direct prompt to ensure success
    prompt = f"Write a 600-word educational guide about: {topic}. Use HTML tags (<h2>, <h3>, <p>, <ul>, <li>)."
    try:
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        return response.text
    except Exception as e:
        return f"<h1>Generation Failed</h1><p>Error: {e}</p>"

if __name__ == "__main__":
    # Load the template
    with open("template.html", "r") as f:
        template = f.read()

    for filename, topic in pages.items():
        print(f"Working on {filename}...")
        content = generate_content(topic)
        final_html = template.replace("{CONTENT}", content)
        
        with open(filename, "w") as f:
            f.write(final_html)
        print(f"Finished {filename}")
