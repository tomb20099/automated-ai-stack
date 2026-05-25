import os
import google.generativeai as genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Function to automatically pick a supported model
def get_working_model():
    models = genai.list_models()
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            return genai.GenerativeModel(m.name)
    return None

model = get_working_model()

if model:
    response = model.generate_content("Write a promotional blurb for Systeme.io.")
    
    # Use HTML styling to make the output readable and formatted
    html_content = f"""
    <html>
        <body style='font-family: sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: auto;'>
            {response.text.replace('**', '<b>').replace('>', '<br>')}
        </body>
    </html>
    """
    
    with open("index.html", "w") as f:
        f.write(html_content)
else:
    print("No usable models found.")
    exit(1)
