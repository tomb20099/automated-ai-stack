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
    # Improved prompt to ensure the link is used naturally
    prompt = f"""
    Write a persuasive and helpful promotional article about Systeme.io.
    Explain how it helps entrepreneurs automate their business.
    Naturally include this call to action with the link: 
    'Click here to start your all-in-one business for free: {MY_AFFILIATE_LINK}'
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

