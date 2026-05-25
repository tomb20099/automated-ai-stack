import os
import google.generativeai as genai

# Securely grab your hidden Gemini API Key from GitHub Secrets
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY secret is missing!")

# Configure the AI brain using the updated flash model
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# The ultimate SaaS marketing prompt engineered for high conversion
marketing_prompt = (
    "You are an expert SaaS affiliate marketer creating high-converting short-form video scripts "
    "(YouTube Shorts/TikTok) to promote the free all-in-one business builder, Systeme.io.\n\n"
    "Generate a unique, highly engaging 60-second video script. Vary the topic today—choose either "
    "a comparison (e.g., Systeme vs ClickFunnels), a specific tutorial step (e.g., how to build a free landing page "
    "in 5 minutes), or a passive income strategy (e.g., how to sell digital products with $0 startup cost).\n\n"
    "Include the following structural sections:\n"
    "1. HOOK: A jarring or deeply relatable statement in the first 3 seconds to stop the scroll.\n"
    "2. THE PROBLEM: Why traditional software setups are too expensive or complicated for beginners.\n"
    "3. THE SOLUTION: Introduce how Systeme.io solves this perfectly for $0/month.\n"
    "4. CALL TO ACTION (CTA): Explicitly direct viewers to click the link in the comments/description to grab their free account.\n"
    "5. ON-SCREEN VISUAL CUES: Add bracketed notes [like this] explaining what visual or text overlay should be shown on screen during each line.\n\n"
    "Keep the tone sharp, punchy, confident, and highly persuasive. Do not use generic introductions."
)

print("Contacting Gemini for today's high-intent affiliate script...")
response = model.generate_content(marketing_prompt)

# Append the new scripts to a running backlog file
with open("daily_output.txt", "a+", encoding="utf-8") as f:
    f.write("\n" + "="*50 + "\n")
    f.write("AUTOMATED SAAS SCRIPT GENERATION\n")
    f.write("="*50 + "\n\n")
    f.write(response.text)
    f.write("\n\n")

print("Success! Your daily affiliate script has been safely added to your digital asset vault.")
