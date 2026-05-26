import os
import time
from google import genai
from google.genai import types

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Configuration
MY_AFFILIATE_LINK = "https://systeme.io/?sa=sa0272561737740b78da5351c120a4a094cf24ecb8"
NEWSLETTER_LINK = "https://tombeattie09.systeme.io/7a3a6748"
IMAGE_URL = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800"

PAGES = {
    "index.html": "Write a high-converting promotional article about Systeme.io all-in-one features.",
    "automation.html": "Write a comprehensive guide on how to automate your sales funnel.",
    "courses.html": "Write a guide on how to host and sell online courses using Systeme.io."
}

def generate_with_retry(prompt, retries=3):
    """Generates content using the modern Gemini SDK."""
    for i in range(retries):
        try:
            # Using the latest stable model
            response = client.models.generate_content(
                model='gemini-3.5-flash',
                contents=prompt,
            )
            return response
        except Exception as e:
            print(f"DEBUG ERROR: {e}")
            time.sleep(45) 
    return None

if __name__ == "__main__":
    with open("template.html", "r") as f:
        template = f.read()

    for filename, topic_prompt in PAGES.items():
        print(f"Generating content for {filename}...")
        time.sleep(40) 
        
        prompt = f"""
        Write a detailed, 500-word professional article about: {topic_prompt}.
        
        CRITICAL INSTRUCTIONS:
        - Output pure HTML tags only (<h2>, <p>, <ul><li>). 
        - DO NOT use Markdown symbols.
        - Include this image tag after the first paragraph: 
          <img src='{IMAGE_URL}' alt='Systeme.io dashboard' class='article-image'>
        - Tone: Expert and authoritative.
        """
        
        response = generate_with_retry(prompt)
        
        if response and response.text:
            content_body = response.text
            final_html = template.replace("{CONTENT}", content_body)\
                                 .replace("{NEWSLETTER_LINK}", NEWSLETTER_LINK)\
                                 .replace("{TITLE}", filename.replace(".html", "").title() + " | Systeme.io Business Tools")
            
            with open(filename, "w") as f:
                f.write(final_html)
            print(f"Successfully generated {filename}.")
        else:
            print(f"Failed to generate {filename}.")
