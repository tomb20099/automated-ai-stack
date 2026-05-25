import os
import google.generativeai as genai

# Setup
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate Content
prompt = "Write a catchy headline and a 3-sentence promotional blurb for Systeme.io with a placeholder link."
response = model.generate_content(prompt)

# Save as HTML (The 'Platform')
html_content = f"""
<html>
<body>
    <h1>My SaaS Affiliate Hub</h1>
    <div style="font-family: sans-serif;">
        {response.text.replace('$', '<br>')}
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)


