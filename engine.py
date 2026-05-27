import os
import time
from google.generativeai import configure, GenerativeModel

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
configure(api_key=api_key)

# Configuration
NEWSLETTER_LINK = "https://tombeattie09.systeme.io/7a3a6748"
IMAGE_URL = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800"

# Updated topics to be educational/consultative
PAGES = {
    "index.html": "The evolution of digital business and why all-in-one platforms are replacing fragmented tool stacks.",
    "automation.html": "A guide on building a stress-free automated sales funnel for beginners.",
    "courses.html": "How to structure and launch your first online course for maximum student success."
}

def get_authoritative_prompt(topic):
    return f"""
    You are an expert digital marketing consultant specializing in business automation. 
    Write a 600-word, highly educational, and practical guide about: {topic}.

    Follow this structure strictly using HTML tags (<h2>, <h3>, <p>, <ul>, <li>):
    1. THE HOOK: Identify a specific frustration or pain point the reader currently faces regarding this topic.
    2. THE WHY: Explain the strategy and logic behind the solution. Be educational, not promotional.
    3. THE HOW-TO: Provide a step-by-step, numbered implementation guide. Be technical and actionable.
    4. COMMON PITFALLS: List 3 mistakes beginners make and how to avoid them.
    5. THE RECOMMENDATION: A single, non-pushy paragraph explaining that for this specific workflow, you use Systeme.io because it unifies these steps into one platform.

    TIPS FOR SUCCESS:
    - Write in a professional, consulting tone.
    - Do NOT use exaggerated sales language (e.g., "life-changing," "guaranteed").
    - Focus on utility: The reader should walk away with a real plan.
    - Include this image at the top of the article: <img src='{IMAGE_URL}' style='width:100%; height:auto;'>
    """

def generate_content(prompt):
    model = GenerativeModel('gemini-1.5-flash') # Using the standard stable model
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
            
            prompt = get_authoritative_prompt(topic)
            content = generate_content(prompt)
            
            final_html = template.replace("{CONTENT}", content)\
                                 .replace("{NEWSLETTER_LINK}", NEWSLETTER_LINK)\
                                 .replace("{TITLE}", filename.replace(".html", "").title())
            
            with open(filename, "w") as f:
                f.write(final_html)
            print(f"Successfully saved {filename}.")
            
        except Exception as e:
            print(f"FAILED to generate {filename}: {e}")
            with open(filename, "w") as f:
                f.write(f"<h1>Coming Soon</h1><p>We are updating this content. Please check back later.</p>")
            continue 

    print("Process finished.")
