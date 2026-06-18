import datetime, requests

today = datetime.date.today().strftime("%d %B %Y")

# Try to pull live gas from YOUR site
try:
    gas_data = requests.get('https://Tom007.pythonanywhere.com/api', timeout=5).json()
    gas_fast = gas_data.get('fast', 25)
except:
    gas_fast = 25  # fallback

pages = {
"index.html": ("Startup Runway Calculator UK", "Free runway & burn rate insights – powered by ApexCFO"),
"ethereum-gas-today.html": (f"Live Ethereum Gas: {gas_fast} gwei", "Track gas fees on our main tracker"),
"burn-rate-guide.html": ("Burn Rate Calculator for Founders", "See how long your cash lasts"),
"saas-metrics.html": ("SaaS Metrics Dashboard", "Live MRR, ARR and runway examples")
}

template = """<!DOCTYPE html><html lang="en-GB"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{h1}</title>
<meta name="description" content="{desc}">
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

<p>{desc}. Current ETH fast gas: <strong>{gas} gwei</strong> (from our tracker).</p>

<h3>Why founders click through:</h3>
<ul>
<li>ApexCFO: real-time runway, burn, MRR tracking</li>
<li>Gas Tracker: save on every Ethereum transaction</li>
</ul>

<p><a href="https://apexcfo.lovable.app">→ Start with ApexCFO</a> | <a href="https://Tom007.pythonanywhere.com">→ Open Gas Tracker</a></p>

<footer><p>© 2026 | Built by automated-ai-stack to drive traffic to our tools</p></footer>
</body></html>"""

for filename, (h1, desc) in pages.items():
    slug = filename.replace('.html','')
    html = template.format(h1=h1, desc=desc, today=today, gas=gas_fast, slug=slug)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"SUCCESS: {filename} → gas {gas_fast} gwei")
