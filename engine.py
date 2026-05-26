import os
import time
import google.generativeai as genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Configuration
MY_AFFILIATE_LINK = "https://systeme.io/?sa=sa0272561737740b78da5351c120a4a094cf24ecb8"
NEWSLETTER_LINK = "https://tombeattie09.systeme.io/7a3a6748"
IMAGE_URL = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800"

PAGES = {
    "index.html": "Write a high-converting promotional article about Systeme.io all-in-one features.",
    "automation.html": "Write a comprehensive guide on how to automate your sales funnel.",
    "marketing.html": "Write professional tips on effective email marketing for beginners."
}

def generate_with_retry(prompt, retries=3):
    """Generates content with a built-in retry mechanism for API stability."""
    model = genai.GenerativeModel('gemini-1.5-flash')
    for i in range(retries):
        try:
            return model.generate_content(prompt)
        except Exception as e:
            print(f"Attempt {i+1} failed: {e}. Retrying in 45 seconds...")
            time.sleep(45) 
    return None

if __name__ == "__main__":
    # Read the template
    with open("template.html", "r") as f:
        template = f.read()

    for filename, topic_prompt in PAGES.items():
        print(f"Generating content for {filename}...")
        
        # Enhanced prompt for structure and professional HTML quality
        prompt = f"""
        Write a detailed, 500-word professional article about: {topic_prompt}.
        
        CRITICAL INSTRUCTIONS:
        - Output the content using pure HTML tags only (use <h2> for subheadings, <p> for paragraphs, and <ul><li> for bullet points). 
        - DO NOT use Markdown symbols like ##, **, or -.
        - Include this exact HTML image tag right after the first paragraph: 
          <img src='{IMAGE_URL}' alt='Systeme.io dashboard' class='article-image'>
        - Tone: Expert, engaging, and authoritative.
        - Start with the pain, present the solution, and end with a call to action.
        """
        
        response = generate_with_retry(prompt)
        
        if response:
            content_body = response.text
            
            # Process the affiliate link replacement
            clickable_link = f'<a href="{MY_AFFILIATE_LINK}" target="_blank" style="font-weight: bold; color: #007bff;">Click here to launch your business for free</a>'
            content_body = content_body.replace(f'Click here to launch your business for free: {MY_AFFILIATE_LINK}', f'Stop struggling with your workflow. {clickable_link}')

            # Fill the template mold
            final_html = template.replace("{CONTENT}", content_body)\
                                 .replace("{NEWSLETTER_LINK}", NEWSLETTER_LINK)\
                                 .replace("{TITLE}", filename.replace(".html", "").title() + " | Systeme.io Business Tools")
            
            # Write the file
            with open(filename, "w") as f:
                f.write(final_html)
            print(f"Successfully generated {filename}.")
        else:
            print(f"Failed to generate {filename} after retries.")
            
    print("All pages generated successfully.")
