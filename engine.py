import os
import google.generativeai as genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Configuration
MY_AFFILIATE_LINK = "https://systeme.io/?sa=sa0272561737740b78da5351c120a4a094cf24ecb8"
NEWSLETTER_LINK = "https://tombeattie09.systeme.io/7a3a6748"
IMAGE_URL = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800"

# Define the pages to build
PAGES = {
    "index.html": "Write a high-converting promotional article about Systeme.io all-in-one features.",
    "automation.html": "Write a comprehensive guide on how to automate your sales funnel.",
    "marketing.html": "Write professional tips on effective email marketing for beginners."
}

def get_working_model():
    models = genai.list_models()
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            return genai.GenerativeModel(m.name)
    return None

# Use the dynamic model selector
model_instance = get_working_model()

if model_instance:
    print(f"Successfully connected to model: {model_instance.model_name}")
    
    # Read the template
    with open("template.html", "r") as f:
        template = f.read()

    for filename, topic_prompt in PAGES.items():
        print(f"Generating content for {filename}...")
        
        prompt = f"""
        Write a high-converting article about: {topic_prompt}
        
        CRITICAL INSTRUCTIONS:
        - Include this exact HTML image tag right after the first paragraph: 
          <img src='{IMAGE_URL}' alt='Systeme.io dashboard' class='article-image'>
        - Write approximately 300 words.
        - Ensure the tone is polished and cohesive.
        - Start with the pain, present the solution, and end with a call to action.
        """
        
        response = model_instance.generate_content(prompt)
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
            
    print("All pages generated successfully.")

else:
    print("Error: No usable models found. Check your API key or permissions.")
    exit(1)
