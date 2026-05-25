import os
import google.generativeai as genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Configuration
# This is your unique affiliate link
MY_AFFILIATE_LINK = "https://systeme.io/?sa=sa0272561737740b78da5351c120a4a094cf24ecb8"

def get_working_model():
    models = genai.list_models()
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            return genai.GenerativeModel(m.name)
    return None

model = get_working_model()

if model:
    # This prompt is structured to force a single, persuasive article
    # and includes your affiliate link as requested.
    prompt = f"""
    Write a high-converting, 300-word promotional article for Systeme.io.
    
    CRITICAL INSTRUCTIONS:
    - Do NOT provide "options". 
    - Do NOT use headers like "Option 1" or "Option 2".
    - Write exactly one polished, cohesive article.
    
    Structure the article using these four steps:
    1. THE PAIN: Start by highlighting the frustration of managing multiple expensive marketing tools.
    2. THE SOLUTION: Introduce Systeme.io as the 'all-in-one' secret weapon that solves this instantly. 
    3. THE PROOF: Mention that it is designed to save money and consolidate their entire tech stack.
    4. THE CALL TO ACTION: End with this exact sentence: 'Stop struggling with your workflow. Click here to launch your business for free: {MY_AFFILIATE_LINK}'

    Tone: Energetic, professional, and empathetic. 
    """
    
    response = model.generate_content(prompt)
    
    # HTML template with required affiliate disclosure
    html_content = f"""
    <html>
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
