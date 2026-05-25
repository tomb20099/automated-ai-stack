import os
import google.generativeai as genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Configuration
MY_AFFILIATE_LINK = "https://systeme.io/?sa=sa0272561737740b78da5351c120a4a094cf24ecb8"
# List of professional stock image URLs to rotate through
IMAGE_URL = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800"

def get_working_model():
    models = genai.list_models()
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            return genai.GenerativeModel(m.name)
    return None

model = get_working_model()

if model:
    prompt = f"""
    Write one single, high-converting promotional article for Systeme.io.
    
    CRITICAL INSTRUCTIONS:
    - Include an HTML image tag <img src='{IMAGE_URL}' alt='Systeme.io dashboard' style='max-width: 100%; height: auto; border-radius: 8px;'> right after the first paragraph.
    - Do NOT use headers like "Option 1".
    - Write exactly one polished, cohesive article.
    
    Structure:
    1. THE PAIN: Start by highlighting the frustration of managing multiple tools.
    2. THE SOLUTION: Introduce Systeme.io as the 'all-in-one' secret weapon.
    3. THE PROOF: Mention it consolidates the tech stack.
    4. THE CALL TO ACTION: End with: 'Stop struggling with your workflow. Click here to launch your business for free: {MY_AFFILIATE_LINK}'
    """
    
    response = model.generate_content(prompt)
    
    # We keep the raw HTML provided by the AI
    content_body = response.text
    clickable_link = f'<a href="{MY_AFFILIATE_LINK}" target="_blank" style="font-weight: bold; color: #007bff;">Click here to launch your business for free</a>'
    content_body = content_body.replace(f'Click here to launch your business for free: {MY_AFFILIATE_LINK}', f'Stop struggling with your workflow. {clickable_link}')

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name='impact-site-verification' value='b52fd6d4-08b7-4aee-b6c1-d9c5a5f65793'>
        <title>Systeme.io Review</title>
    </head>
    <body style='font-family: sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: auto;'>
        {content_body}
    </body>
    </html>
    """
    
    with open("index.html", "w") as f:
        f.write(html_content)
else:
    print("No usable models found.")
    exit(1)
