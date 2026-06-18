import datetime, requests

def get_live_data():
    today = datetime.date.today().strftime("%d %B %Y")
    try:
        gas = requests.get('https://ethgas.website/api', timeout=5).json()
        gas_fast = gas.get('fast', 25)
    except:
        gas_fast = 25
    apex = {"mrr":85000,"arr":1020000,"burn":22600,"runway":33,"margin":26.6,"expenses":62400}
    return today, gas_fast, apex

today, gas_fast, apex = get_live_data()

pages = {
"index.html": "Startup Runway Calculator UK",
"ethereum-gas-today.html": f"Ethereum Gas Fees Today: {gas_fast} gwei",
"burn-rate-guide.html": "How to Calculate Burn Rate UK",
"uk-train-delay-repay.html": "UK Train Delay Repay Calculator 2026"
}

template = """<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {today}</title><meta name="description" content="{title} with live startup metrics"></head>
<body><header><h1>{title}</h1><p><em>Updated: {today}</em></p></header><main>
<h2>Live Data Dashboard</h2>
<table border="1" cellpadding="8"><tr><th>Metric</th><th>Value</th></tr>
<tr><td>Date</td><td>{today}</td></tr>
<tr><td>Ethereum Fast Gas</td><td>{gas} gwei</td></tr>
<tr><td>Example MRR</td><td>${mrr:,}</td></tr>
<tr><td>Example ARR</td><td>${arr:,}</td></tr>
<tr><td>Monthly Burn</td><td>${burn:,}</td></tr>
<tr><td>Runway</td><td>{runway} months</td></tr>
<tr><td>Net Margin</td><td>{margin}%</td></tr>
</table>

<h2>What This Means for UK Founders</h2>
<p>With a burn of ${burn:,} and runway of {runway} months, reducing expenses by 10% adds over 3 months of runway. Track this weekly.</p>

<h3>Actionable Tip</h3>
<p>Use the live gas price ({gas} gwei) to time Ethereum transactions and save on fees — critical when margins are {margin}%.</p>

<p>Data updated {today}. Try the free tools at ApexCFO and ethgas.website</p>
</main><footer><p>© 2026 Automated AI Stack | <a href="/privacy.html">Privacy</a></p></footer></body></html>"""

for filename, title in pages.items():
    html = template.format(title=title, today=today, gas=gas_fast, **apex)
    with open(filename, "w", encoding="utf-8") as f: f.write(html)
    print(f"SUCCESS: {filename}")
