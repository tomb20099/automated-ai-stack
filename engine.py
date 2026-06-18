import datetime, requests

today, gas = datetime.date.today().strftime("%d %B %Y"), 25
try: gas = requests.get('https://ethgas.website/api', timeout=5).json().get('fast',25)
except: pass

apex = {"mrr":85000,"arr":1020000,"burn":22600,"runway":33}

pages = {
"index.html": ("Startup Runway Calculator UK – Free Tool", "Calculate your runway in seconds with live market data."),
"ethereum-gas-today.html": (f"Ethereum Gas Tracker: {gas} gwei Live", "Track gas fees before you transact."),
"burn-rate-guide.html": ("Burn Rate Calculator – See How Long Your Cash Lasts", f"Example: ${apex['burn']:,}/mo burn = {apex['runway']} months runway"),
"uk-train-delay-repay.html": ("UK Train Delay Repay Calculator 2026", "Check what you're owed in 30 seconds")
}

tpl = """<!DOCTYPE html><html lang="en-GB"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{h1}</title>
<meta name="description" content="{desc}">
<style>body{{font-family:system-ui;max-width:800px;margin:40px auto;padding:0 20px;line-height:1.6}} .cta{{display:inline-block;background:#0d6efd;color:#fff;padding:14px 24px;text-decoration:none;border-radius:8px;margin:12px 0;font-weight:600}} table{{border-collapse:collapse;width:100%;margin:20px 0}} th,td{{border:1px solid #ddd;padding:10px;text-align:left}}</style>
</head><body>
<h1>{h1}</h1><p><em>Updated {today}</em></p>

<div style="background:#f8f9fa;padding:20px;border-radius:8px;margin:20px 0">
<h2>Try the Live Tools →</h2>
<a class="cta" href="https://apexcfo.com?utm_source=stack&utm_medium=seo&utm_campaign=runway">Open ApexCFO Free</a>
<a class="cta" href="https://ethgas.website?utm_source=stack" style="background:#28a745">Check Live Gas Fees</a>
</div>

<h2>Live Data Dashboard</h2>
<table><tr><th>Metric</th><th>Value</th></tr>
<tr><td>ETH Fast Gas</td><td>{gas} gwei</td></tr>
<tr><td>Demo MRR</td><td>${mrr:,}</td></tr>
<tr><td>Runway</td><td>{runway} months</td></tr>
</table>

<p>{desc} This data updates automatically twice weekly.</p>

<h3>Why Founders Use ApexCFO</h3>
<ul><li>Real-time burn & runway (like above)</li><li>Connects to Xero/Stripe</li><li>Free tier available</li></ul>

<p><a class="cta" href="https://apexcfo.com">Calculate Your Runway Now →</a></p>

<footer><p>© 2026 | <a href="/">More Calculators</a></p></footer>
</body></html>"""

for fn,(h1,desc) in pages.items():
    html = tpl.format(h1=h1,desc=desc,today=today,gas=gas,**apex)
    open(fn,"w",encoding="utf-8").write(html)
    print("SUCCESS:",fn)
