import datetime, re, requests

today = datetime.date.today().strftime("%d %B %Y")

# --- PULL LIVE GAS FROM YOUR SITE ---
try:
    html = requests.get('https://Tom007.pythonanywhere.com', timeout=10).text
    match = re.search(r'(\d+\.?\d*)\s*Gwei', html)
    gas_fast = float(match.group(1)) if match else 0.31
except Exception as e:
    print(f"Gas fetch failed: {e}")
    gas_fast = 0.31

# --- YOUR PAGES ---
pages = {
"index.html": ("Startup Runway Calculator UK", "Free runway & burn rate insights – powered by ApexCFO"),
"ethereum-gas-today.html": (f"Live Ethereum Gas: {gas_fast} gwei", "UK gas tracker – updated every 12 seconds"),
"burn-rate-guide.html": ("Burn Rate Calculator for Founders", "See how long your cash lasts with live market data"),
"saas-metrics.html": ("SaaS Metrics Dashboard", "MRR, ARR and runway examples")
}

template = """<!DOCTYPE html><html lang="en-GB"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{h1}</title>
<meta name="description" content="{desc} – current gas {gas} gwei">
<style>
body{{font-family:system-ui;max-width:820px;margin:40px auto;padding:0 20px;line-height:1.6}}
.cta{{display:inline-block;padding:14px 24px;text-decoration:none;border-radius:8px;margin:10px 8px 10px 0;font-weight:600;color:#fff}}
.blue{{background:#0d6efd}} .green{{background:#198754}}
.card{{background:#f8f9fa;padding:22px;border-radius:10px;margin:24px 0}}
</style>
</head><body>
<h1>{h1}</h1>
<p><em>Updated {today}</em></p>

<div class="card">
<h2>Use the Live Tools →</h2>
<a class="cta blue" href="https://apexcfo.lovable.app/?utm_source=stack&utm_medium=seo&utm_campaign={slug}">Open ApexCFO App</a>
<a class="cta green" href="https://Tom007.pythonanywhere.com/?utm_source=stack&utm_medium=seo&utm_campaign={slug}">Check Live Gas Tracker</a>
</div>

<p>{desc}. Current ETH fast gas: <strong>{gas} gwei</strong> (live from our tracker).</p>

<h3>Why founders click through:</h3>
<ul>
<li>ApexCFO: real-time runway, burn, MRR tracking</li>
<li>Gas Tracker: save on every Ethereum transaction – we update every 12 seconds</li>
</ul>

<p><a href="https://apexcfo.lovable.app">→ Start with ApexCFO</a> | <a href="https://Tom007.pythonanywhere.com">→ Open Gas Tracker</a></p>

<footer><p>© 2026 | Pages auto-generated from Tom007.pythonanywhere.com live data</p></footer>
</body></html>"""

for filename, (h1, desc) in
