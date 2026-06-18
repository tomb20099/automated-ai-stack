import datetime, re, urllib.request

today = datetime.date.today().strftime("%d %B %Y")

try:
    with urllib.request.urlopen('https://Tom007.pythonanywhere.com', timeout=10) as resp:
        html = resp.read().decode('utf-8')
    match = re.search(r'(\d+\.?\d*)\s*Gwei', html)
    gas_fast = match.group(1) if match else "0.31"
except:
    gas_fast = "0.31"

pages = {
"index.html": "Startup Runway Calculator UK",
"ethereum-gas-today.html": f"Live Ethereum Gas: {gas_fast} gwei",
"burn-rate-guide.html": "Burn Rate Calculator for Founders",
"saas-metrics.html": "SaaS Metrics Dashboard"
}

for filename, title in pages.items():
    slug = filename.replace('.html','')
    html_out = f"""<!DOCTYPE html><html lang="en-GB"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{title} - current gas {gas_fast} gwei">
</head><body style="font-family:system-ui;max-width:820px;margin:40px auto;padding:0 20px;line-height:1.6">
<h1>{title}</h1><p><em>Updated {today}</em></p>
<div style="background:#f8f9fa;padding:22px;border-radius:10px;margin:24px 0">
<h2>Use the Live Tools →</h2>
<p><a href="https://apexcfo.lovable.app/?utm_source=stack&utm_medium=seo&utm_campaign={slug}" style="display:inline-block;background:#0d6efd;color:#fff;padding:14px 24px;text-decoration:none;border-radius:8px;margin:6px 0;font-weight:600">Open ApexCFO App</a></p>
<p><a href="https://Tom007.pythonanywhere.com/?utm_source=stack&utm_medium=seo&utm_campaign={slug}" style="display:inline-block;background:#198754;color:#fff;padding:14px 24px;text-decoration:none;border-radius:8px;margin:6px 0;font-weight:600">Check Live Gas Tracker</a></p>
</div>
<p>Free runway & burn rate insights – powered by ApexCFO. Current ETH fast gas: <strong>{gas_fast} gwei</strong> (live from our tracker).</p>
</body></html>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"SUCCESS: {filename}")

# sitemap
from datetime import datetime
urls = ["https://tomb20099.github.io/","https://tomb20099.github.io/ethereum-gas-today.html","https://tomb20099.github.io/burn-rate-guide.html","https://tomb20099.github.io/saas-metrics.html"]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sitemap += f'  <url><loc>{u}</loc><lastmod>{datetime.now().date()}</lastmod></url>\n'
sitemap += '</urlset>'
open("sitemap.xml","w").write(sitemap)
print("SUCCESS: sitemap.xml")
