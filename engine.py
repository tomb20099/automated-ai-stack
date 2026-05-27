import os
import time
from google.generativeai import configure, GenerativeModel

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
configure(api_key=api_key)

# Configuration
NEWSLETTER_LINK = "https://tombeattie09.systeme.io/7a3a6748"
IMAGE_URL = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800"

PAGES = {
    "index.html": "High-converting promotional article about Systeme.io all-in-one features.",
    "automation.html": "Guide on how to automate your sales funnel.",
    "courses.html": "Guide on how to host and sell online courses using Systeme.io."
}

def generate_content(prompt):
    # UPDATED: Switched to gemini-3.5-flash
    model = GenerativeModel('gemini-3.5-flash') 
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    if not os.path.exists("template.html"):
        raise FileNotFoundError("template.html is missing!")

    with open("template.html", "r") as f:
        template = f.read()

    for filename, topic in PAGES.items():
        try:
            print(f"Generating {filename}...")
            # Still using 70s sleep to respect API rate limits
            time.sleep(70) 
            
            prompt = f"Write a 500-word article about: {topic}. Use HTML tags (<h2>, <p>). Include this image: <img src='{IMAGE_URL}'>"
            
            content = generate_content(prompt)
            
            final_html = template.replace("{CONTENT}", content)\
                                 .replace("{NEWSLETTER_LINK}", NEWSLETTER_LINK)\
                                 .replace("{TITLE}", filename.replace(".html", "").title())
            
            with open(filename, "w") as f:
                f.write(final_html)
            print(f"Successfully saved {filename}.")
            
        except Exception as e:
            print(f"FAILED to generate {filename}: {e}")
            # Fallback to prevent 404s
            with open(filename, "w") as f:
                f.write(f"<h1>Coming Soon</h1><p>We are updating this content. Please check back later.</p>")
            continue 

    print("Process finished.")
