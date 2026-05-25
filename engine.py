import os
import google.generativeai as genai

# Setup API
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Initialize a reliable model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate Content for your site
prompt = "Write a catchy, professional promotional blurb for Systeme.io with a call to action. Format it in clean HTML tags like <h1> and <p>."
response = model.generate_content(prompt)

# Save as index.html so GitHub Pages can show it to the world
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>My SaaS Hub</title>
</head>
<body style="font-family: sans-serif; padding: 20px;">
    {response.text}
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)
