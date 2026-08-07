import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLES_DIR = os.path.join(ROOT, "samples")

with open(os.path.join(SAMPLES_DIR, "manifest.json")) as f:
    MANIFEST = json.load(f)

def esc(s):
    import html
    return html.escape(str(s), quote=True)

cards = []
for fname, label, doctype, layout, theme, profession, size_kb in MANIFEST:
    icon = "📄" if doctype == "cv" else "✉️"
    theme_badge = "B&W" if theme == "mono" else "Colour"
    cards.append(f'''
      <a class="tpl-card" href="{fname}.pdf" style="display:flex;" download>
        <div class="tpl-thumb" style="aspect-ratio:3/4;display:flex;align-items:center;justify-content:center;background:var(--paper-dim);">
          <span class="seal-badge">{theme_badge}</span>
          <span style="font-size:40px;">{icon}</span>
        </div>
        <div class="tpl-meta">
          <div class="name">{esc(label)}</div>
          <div class="tags">PDF &middot; {size_kb} KB</div>
        </div>
      </a>''')

html_out = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" type="image/svg+xml" href="../assets/logo.svg">
<link rel="icon" type="image/png" sizes="32x32" href="../assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="../assets/favicon-16.png">
<link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
<title>Sample PDF Downloads — Nigerian CV</title>
<meta name="description" content="Download real PDF sample copies of our Nigerian CV and cover letter templates — see exactly what you'll get before you start filling in your own.">
<link rel="canonical" href="https://nigeriancv.example.com/samples/index.html">
<meta property="og:title" content="Sample PDF Downloads — Nigerian CV">
<meta property="og:description" content="Download real PDF sample copies of our CV and cover letter templates.">
<meta property="og:type" content="website">
<meta property="og:image" content="https://nigeriancv.example.com/assets/og-image.png">
<link rel="stylesheet" href="../css/theme.css">
</head>
<body class="mesh-bg">
  <div class="topbar">
    <a class="back-link" href="../index.html">← Home</a>
    <div class="brand"><img class="seal" src="../assets/logo.svg" alt="Nigerian CV logo" width="30" height="30">Nigerian CV</div>
  </div>
  <nav class="site-nav">
    <a href="../index.html">Home</a>
    <a href="../cv.html">CV Templates</a>
    <a href="../cover-letter.html">Cover Letters</a>
    <a href="../guides/index.html">Guides</a>
    <a href="index.html" class="active">Sample PDFs</a>
  </nav>

  <div class="wrap">
    <h1 style="font-size:24px;margin-top:6px;">Sample PDF downloads</h1>
    <p class="muted" style="margin-top:6px;font-size:14px;">Real, finished PDF exports of our templates — filled with sample data — so you know exactly what you'll get. Tap any card to download.</p>

    <div class="gallery-grid" style="margin-top:18px;">
      {"".join(cards)}
    </div>

    <p class="muted" style="font-size:12.5px;margin-top:22px;">These are illustrative samples using placeholder names and details. When you build your own, only your information appears in the download — nothing here is uploaded or shared.</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="../cv.html">Build your own CV →</a>
      <a class="btn btn-coral" href="../cover-letter.html">Build your own Cover Letter →</a>
    </div>
  </div>

  <p class="foot-note">Nigerian CV · Built for job seekers across Nigeria 🇳🇬</p>
</body>
</html>
'''
with open(os.path.join(SAMPLES_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_out)
print("Generated samples/index.html")
