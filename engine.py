import os
import requests
import datetime
from google import genai

# Setup
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# --- YOUR LIVE DATA (from your screenshots) ---
def get_live_data():
    today = datetime.date.today().strftime("%d %B %Y")
    
    # Gas from your own tracker (fallback to 25)
    try:
        gas = requests.get('https://ethgas.website/api', timeout=5).json()
        gas_fast = gas.get('fast', 25)
    except:
        gas_fast = 25
    
    apex = {
        "mrr": 85000,
        "arr": 1020000,
        "burn": 22600,
        "runway": 33,
        "margin": 26.6,
        "expenses": 62400
    }
    return today, gas_fast, apex

today, gas_fast, apex = get_live_data()

# --- HIGH-CPC TOPICS (from your £8-22 screenshot) ---
topics = {
    "index.html": f"Startup Runway Calculator UK - Live data {today}",
    "ethereum-gas-today.html": f"Ethereum Gas Fees Today: {gas_fast} gwei live tracker",
    "burn-rate-guide.html": f"How to calculate burn rate - example with ${apex['burn']:,}/mo burn and {apex['runway']} months runway",
    "uk-train-delay-repay.html": "UK Train Delay Repay Calculator 2026 - how much can you claim"
}

def generate_content(filename, topic):
    print(f"ATTEMPTING: {topic}...")
    try:
        prompt = f"""
Write a complete HTML article for UK founders. 

LIVE DATA TO INCLUDE (must appear in a table):
- Date: {today}
- Ethereum fast gas: {gas_fast} gwei
- Example startup metrics: MRR ${apex['mrr']:,}, ARR ${apex['arr']:,}, Monthly expenses ${apex['expenses']:,}, Burn ${apex['burn']:,}, Runway {apex['runway']} months, Net margin {apex['margin']}%

TOPIC: {topic}

Requirements:
1. 700-900 words, practical, no fluff
2. Use H2 and H3 headings
3. Include the live data table early in the article
4. Target keywords: startup runway calculator, burn rate UK, Ethereum gas fees, train delay repay
5. Add one actionable tip using the numbers above
6. End with: "Data updated {today}. Try the free tools at ApexCFO and ethgas.website"
7. Do NOT include affiliate links or promotional language
8. Output ONLY the article body HTML (no <html><body> tags)
"""

        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",  # CHANGED from 2.0-flash to avoid quota 0
            contents=prompt
        )
        
        # Build full AdSense-ready page
        html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{topic} | {today}</title>
<meta name="description" content="{topic} with live data for {today}">
</head>
<body>
<header><h1>{topic}</h1><p><em>Updated: {today}</em></p></header>
<main>
{response.text}
</main>
<footer>
<p>© 2026 Automated AI Stack. This page may contain ads. <a href="/disclaimer.html">Affiliate Disclosure</a> | <a href="/privacy.html">Privacy</a></p>
</footer>
</body>
</html>"""
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"SUCCESS: {filename}")
        
    except Exception as e:
        print(f"SKIPPING {topic} due to error: {e}")

if __name__ == "__main__":
    for filename, topic in topics.items():
        generate_content(filename, topic)
