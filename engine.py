import os
import time
from google.generativeai import configure, GenerativeModel

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
configure(api_key=api_key)

# Configuration
MY_AFFILIATE_LINK = "https://systeme.io/?sa=sa0272561737740b78da5351c120a4a094cf24ecb8"
NEWSLETTER_LINK = "https://tombeattie09.systeme.io/7a3a6748"
IMAGE_URL = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800"

PAGES = {
    "index.html": "Write a high-converting promotional article about Systeme.io all-in-one features.",
    "automation.html": "Write a comprehensive guide on how to automate your sales funnel.",
    "courses.html": "Write a guide on how to host and sell online courses using Systeme.io."
}

def generate_with_retry(prompt):
    # Using gemini-2.0-flash, the most stable model for your setup
    model = GenerativeModel('gemini-2.0-flash')
    try:
        return model.generate_content(prompt)
    except Exception as e:
        print(f"!!! CRASH REPORT: {e} !!!")
        return None

if __name__ == "__main__":
    # Ensure template exists
    if not os.path.exists("template.html"):
        raise FileNotFoundError("template.html is missing from your repository!")

    with open("template.html", "r") as f:
        template = f.read()

    for filename, topic_prompt in PAGES.items():
        print(f"Generating {filename}...")
        
        # SLOW DOWN to avoid Free Tier Rate Limits (Quota)
        time.sleep(65)
        
        prompt = f"Write a 500-word article about: {topic_prompt}. Use HTML tags (<h2>, <p>). Include this image: <img src='{IMAGE_URL}'>"
        
        response = generate_with_retry(prompt)
        
        if response and response.text:
            # Filling the template
            final_html = template.replace("{CONTENT}", response.text)\
                                 .replace("{NEWSLETTER_LINK}", NEWSLETTER_LINK)\
                                 .replace("{TITLE}", filename.replace(".html", "").title())
            
            # Writing the file
            with open(filename, "w") as f:
                f.write(final_html)
            print(f"Successfully saved {filename}.")
        else:
            # This triggers the pipeline to stop and show you the error in the logs
            raise Exception(f"Failed to generate {filename}. See CRASH REPORT above.")
