import os
import time
import google.generativeai as genai
from google.generativeai import configure, GenerativeModel

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
configure(api_key=api_key)

NEWSLETTER_LINK = "https://tombeattie09.systeme.io/7a3a6748"
IMAGE_URL = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800"

PAGES = {
    "index.html": "The evolution of digital business and why all-in-one platforms are replacing fragmented tool stacks.",
    "automation.html": "A guide on building a stress-free automated sales funnel for beginners.",
    "courses.html": "How to structure and launch your first online course for maximum student success."
}

def get_authoritative_prompt(topic):
    return f"""
    You are an expert digital marketing consultant. Write a 600-word, educational guide about: {topic}.
    Follow this structure using HTML tags (<h2>, <h3>, <p>, <ul>, <li>):
    1. THE HOOK: Identify a specific frustration or pain point.
    2. THE WHY: Explain the strategy behind the solution.
    3. THE HOW-TO: Provide a step-by-step, numbered implementation guide.
    4. COMMON PITFALLS: List 3 mistakes to avoid.
    5. THE RECOMMENDATION: A single, non-pushy paragraph about using Systeme.io.
    Include this image at the top: <img src='{IMAGE_URL}' style='width:100%; height:auto;'>
    """

def generate_content(prompt):
    # Hardcoded to a universally supported stable model to avoid 404/list_models errors
    model = GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    if not os.path.exists("template.html"):
        raise FileNotFoundError("template.html is missing!")

    with open("template.html", "r") as f:
        template = f.read()

    for filename, topic in PAGES.items():
        # INITIALIZE: If file doesn't exist, create it so the link works immediately
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write(template.replace("{CONTENT}", "<h1>Loading...</h1><p>Content is being generated. Please check back shortly.</p>"))
            print(f"Created placeholder for {filename}")

        try:
            print(f"Attempting to generate content for {filename}...")
            time.sleep(70) 
            
            content = generate_content(get_authoritative_prompt(topic))
            
            final_html = template.replace("{CONTENT}", content)\
                                 .replace("{NEWSLETTER_LINK}", NEWSLETTER_LINK)\
                                 .replace("{TITLE}", filename.replace(".html", "").title())
            
            with open(filename, "w") as f:
                f.write(final_html)
            print(f"Successfully updated {filename}.")
            
        except Exception as e:
            print(f"FAILED to generate {filename}: {e}. Keeping existing content.")
            continue 

    print("Process finished.")
