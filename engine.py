import datetime, re, urllib.request

today = datetime.date.today().strftime("%d %B %Y")

# live gas
try:
    with urllib.request.urlopen('https://Tom007.pythonanywhere.com', timeout=10) as r:
        gas = re.search(r'(\d+\.?\d*)\s*Gwei', r.read().decode()).group(1)
except: gas = "0.18"

pages = {
 "index.html": "Startup Runway Calculator UK",
 "ethereum-gas-today.html": f"Live Ethereum Gas – {gas} gwei",
 "burn-rate-guide.html": "Burn Rate Calculator",
 "saas-metrics.html": "SaaS Metrics Tool"
}

for fn, title in pages.items():
    slug = fn.replace('.html','')
    html = f"""<!DOCTYPE html><html lang="en-GB"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>body{{font-family:system-ui;max-width:900px;margin:40px auto;padding:0 20px;line-height:1.6}}</style>
</head><body>
<h1>{title}</h1>
<p><em>Updated {today} – Live ETH gas: <strong>{gas} gwei</strong></em></p>

<!-- FREE CALCULATOR -->
<div style="background:#fff;border:1px solid #ddd;padding:18px;border-radius:10px;margin:20px 0">
<h3>Quick Runway Check</h3>
Cash £<input id=c type=number value=100000 style="width:100px"> 
Burn £<input id=b type=number value=15000 style="width:100px">
<button onclick="document.getElementById('o').innerText=Math.floor(c.value/b.value)+' months'" style="background:#0d6efd;color:#fff;border:none;padding:8px 12px;border-radius:6px">Calc</button>
<span id=o style="font-weight:700;margin-left:10px">6 months</span>
<p><a href="https://apexcfo.lovable.app/?utm_source=stack&utm_campaign={slug}" style="color:#0d6efd">Save this in ApexCFO →</a></p>
</div>

<!-- MAIN CTAS -->
<p>
<a href="https://apexcfo.lovable.app/?utm_source=stack&utm_campaign={slug}" style="display:inline-block;background:#0d6efd;color:#fff;padding:14px 22px;border-radius:8px;text-decoration:none;margin:5px;font-weight:600">Open ApexCFO App</a>
<a href="https://Tom007.pythonanywhere.com/?utm_source=stack&utm_campaign={slug}" style="display:inline-block;background:#198754;color:#fff;padding:14px 22px;border-radius:8px;text-decoration:none;margin:5px;font-weight:600">Check Live Gas Tracker</a>
</p>

<!-- TOOLVAULT EMBED – makes page look full -->
<h3 style="margin-top:30px">Free ToolVault (browse)</h3>
<iframe src="https://tomb20099.github.io/toolvault-/" style="width:100%;height:400px;border:1px solid #eee;border-radius:8px" loading="lazy"></iframe>
<p style="font-size:0.9em;color:#666">ToolVault is embedded for quick access – our main platforms are above.</p>

</body></html>"""
    open(fn, "w", encoding="utf-8").write(html)
    print("SUCCESS:", fn)

# sitemap for the 4 pages only
urls = [f"https://tomb20099.github.io/{p}" for p in pages]
sitemap = '<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{u}</loc></url>' for u in urls) + '</urlset>'
open("sitemap.xml","w").write(sitemap)
print("SUCCESS: sitemap.xml")
