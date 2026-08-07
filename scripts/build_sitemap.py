import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://nigeriancv.example.com"

with open(f"{ROOT}/data/professions.json") as f:
    PROF = json.load(f)

ids = [p["id"] for p in PROF["cv"]]

urls = [
    ("/index.html", "1.0"),
    ("/cv.html", "0.9"),
    ("/cover-letter.html", "0.9"),
    ("/guides/index.html", "0.8"),
    ("/guides/cv-writing-guide.html", "0.8"),
    ("/guides/cover-letter-guide.html", "0.8"),
    ("/samples/index.html", "0.6"),
]
for pid in ids:
    urls.append((f"/guides/jobs/{pid}.html", "0.7"))

xml_entries = "\n".join(
    f'  <url>\n    <loc>{BASE}{path}</loc>\n    <priority>{priority}</priority>\n  </url>'
    for path, priority in urls
)

sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_entries}
</urlset>
'''
with open(f"{ROOT}/sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

robots = f'''User-agent: *
Allow: /

Sitemap: {BASE}/sitemap.xml
'''
with open(f"{ROOT}/robots.txt", "w", encoding="utf-8") as f:
    f.write(robots)

print(f"sitemap.xml: {len(urls)} URLs")
