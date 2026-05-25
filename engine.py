import os
import google.generativeai as genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Configuration
MY_AFFILIATE_LINK = "https://systeme.io/?sa=sa0272561737740b78da5351c120a4a094cf24ecb8"

def get_working_model():
    models = genai.list_models()
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            return genai.GenerativeModel(m.name)
    return None

model = get_working_model()

if model:
    # Stricter prompt to ensure a single, persuasive article
    prompt = f"""
    Write one single, high-converting promotional article for Systeme.io.
    
    CRITICAL INSTRUCTIONS:
    - Do NOT provide "options". 
    - Do NOT use headers like "Option 1" or "Option 2".
    - Write exactly one polished, cohesive article.
    
    Structure:
    1. THE PAIN: Start by highlighting the frustration of managing multiple expensive marketing tools.
    2. THE SOLUTION: Introduce Systeme.io as the 'all-in-one' secret weapon that solves this instantly. 
    3. THE PROOF: Mention that it is designed to save money and consolidate their entire tech stack.
    4. THE CALL TO ACTION: End with this exact sentence: 'Stop struggling with your workflow. Click here to launch your business for free: {MY_AFFILIATE_LINK}'

    Tone: Energetic, professional, and empathetic. 
    """
    
    response = model.generate_content(prompt)
    
    # HTML template with SEO tags and affiliate disclosure
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Systeme.io Review & All-in-One Marketing Platform</title>
        <meta name="description" content="Discover how to simplify your online business with Systeme.io. An all-in-one platform for sales funnels, email marketing, and course hosting.">
        <meta name="keywords" content="Systeme.io, online business, sales funnels, email marketing, passive income, digital marketing">
        <meta name="robots" content="index, follow">
    </head>
    <body style='font-family: sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: auto;'>
        <p style='font-size: 12px; color: #555; border: 1px solid #ddd; padding: 10px;'>
            <strong>Disclosure:</strong> This post contains affiliate links. If you click and purchase, I may earn a commission at no extra cost to you.
        </p>
        {response.text.replace('**', '<b>').replace('>', '<br>')}
    </body>
    </html>
    """
    
    with open("index.html", "w") as f:
        f.write(html_content)
else:
    print("No usable models found.")
    exit(1)
