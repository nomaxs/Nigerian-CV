import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(f"{ROOT}/data/professions.json") as f:
    PROF = json.load(f)

CV_BY_ID = {p["id"]: p for p in PROF["cv"]}
CL_BY_ID = {p["id"]: p for p in PROF["cover-letter"]}

DEFAULT_CV_LAYOUT = "sidebar-navy"
DEFAULT_CL_LAYOUT = "classic-block"

def esc(s):
    return html.escape(str(s), quote=True)

def page(pid):
    cv = CV_BY_ID[pid]["sample"]
    cl = CL_BY_ID[pid]["sample"]
    name = CV_BY_ID[pid]["name"]
    tags = CV_BY_ID[pid]["tags"]

    title_line = cv["personal"]["title"]
    skills = cv["skills"]
    certs = cv["certifications"]
    exp = cv["experience"][0]
    bullets = exp["responsibilities"]
    employer_example = exp["company"]
    cl_company = cl["recipient"]["company"]
    cl_open = cl["body"][0]

    skill_tags_html = "".join(f"<span>{esc(s)}</span>" for s in skills)
    bullet_html = "".join(f"<li>{esc(b)}</li>" for b in bullets)
    cert_html = "".join(f"<li>{esc(c)}</li>" for c in certs) if certs else "<li>Any relevant professional certification for this field</li>"

    page_title = f"How to Write a {esc(name)} CV & Cover Letter in Nigeria | Nigerian CV"
    meta_desc = f"A tailored guide to writing a {name} CV and cover letter in Nigeria — what skills to list, example achievement lines, and free templates."

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title}</title>
<meta name="description" content="{esc(meta_desc)}">
<link rel="canonical" href="https://nigeriancv.example.com/guides/jobs/{pid}.html">
<meta property="og:title" content="How to Write a {esc(name)} CV &amp; Cover Letter in Nigeria">
<meta property="og:description" content="{esc(meta_desc)}">
<meta property="og:type" content="article">
<link rel="stylesheet" href="../../css/theme.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Write a {esc(name)} CV & Cover Letter in Nigeria",
  "description": {json.dumps(meta_desc)},
  "author": {{ "@type": "Organization", "name": "Nigerian CV" }},
  "publisher": {{ "@type": "Organization", "name": "Nigerian CV" }}
}}
</script>
</head>
<body class="mesh-bg">
  <div class="topbar">
    <a class="back-link" href="../index.html">← Guides</a>
    <div class="brand"><span class="seal">N</span>Nigerian CV</div>
  </div>
  <nav class="site-nav">
    <a href="../../index.html">Home</a>
    <a href="../../cv.html">CV Templates</a>
    <a href="../../cover-letter.html">Cover Letters</a>
    <a href="../index.html" class="active">Guides</a>
  </nav>

  <div class="wrap">
    <p class="breadcrumb" style="padding-left:0;"><a href="../index.html">Guides</a> / {esc(name)}</p>

    <div class="article-hero">
      <span class="eyebrow">{esc(name)} Guide</span>
      <h1>How to Write a {esc(name)} CV &amp; Cover Letter in Nigeria</h1>
      <p class="lede">What to include, which skills to highlight, and example achievement lines for a {esc(name)} application — plus ready-to-edit templates.</p>
    </div>

    <div class="article-body">
      <h2>What to include in your {esc(name)} CV</h2>
      <p>For a <strong>{esc(title_line)}</strong> role, lead your professional summary with your years of experience and your single strongest result — recruiters in this field decide whether to keep reading within the first few seconds. Keep your title line close to how the job advert phrases it.</p>

      <h3>Skills recruiters look for</h3>
      <div class="skill-tags">{skill_tags_html}</div>

      <h3>Example achievement lines</h3>
      <p>Don't just list your duties — show the result. Here's the kind of specific, numbers-first bullet point that works well for this role:</p>
      <ul>{bullet_html}</ul>

      <h3>Certifications worth listing</h3>
      <ul>{cert_html}</ul>

      <h2>What to include in your {esc(name)} Cover Letter</h2>
      <p>Open by naming the exact role and, if possible, the company — for example, a strong opening line for this field reads something like: <em>"{esc(cl_open)}"</em></p>
      <p>Use your second paragraph to connect one concrete achievement (ideally with a number, like the examples above) directly to what the employer is likely looking for. Close with a short, confident line inviting an interview — see the <a href="../cover-letter-guide.html">full cover letter guide</a> for the paragraph-by-paragraph breakdown.</p>

      <div class="callout"><strong>Worked example:</strong> our {esc(name)} sample templates are pre-filled with a realistic profile — a {esc(title_line).lower()} with experience at a company like {esc(employer_example)} — so you can see the finished result before you start editing.</div>

      <div class="cta-row">
        <a class="btn btn-primary" href="../../create.html?type=cv&layout={DEFAULT_CV_LAYOUT}&theme=signature&profession={pid}">Start your {esc(name)} CV →</a>
        <a class="btn btn-coral" href="../../create.html?type=cover-letter&layout={DEFAULT_CL_LAYOUT}&theme=signature&profession={pid}">Start your Cover Letter →</a>
      </div>
      <div class="cta-row">
        <a class="btn btn-ghost" href="../../cv.html?q={esc(name)}">Browse all {esc(name)} CV designs</a>
        <a class="btn btn-ghost" href="../index.html">← Back to all guides</a>
      </div>
    </div>
  </div>

  <p class="foot-note">Nigerian CV · Built for job seekers across Nigeria 🇳🇬</p>
</body>
</html>
"""

os.makedirs(f"{ROOT}/guides/jobs", exist_ok=True)
ids = [p["id"] for p in PROF["cv"]]
for pid in ids:
    with open(f"{ROOT}/guides/jobs/{pid}.html", "w", encoding="utf-8") as f:
        f.write(page(pid))

print(f"Generated {len(ids)} job guide pages")

# ---------------- guides hub ----------------
cards = []
for p in PROF["cv"]:
    cards.append(f'<a class="job-guide-card" href="jobs/{p["id"]}.html">{esc(p["name"])}<span>{esc(", ".join(p["tags"][:2]))}</span></a>')

hub = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CV &amp; Cover Letter Writing Guides — Nigerian CV</title>
<meta name="description" content="Free guides on writing a professional CV and cover letter in Nigeria, plus tailored advice for 46 job categories from Software Engineer to Plumbing.">
<link rel="canonical" href="https://nigeriancv.example.com/guides/index.html">
<meta property="og:title" content="CV & Cover Letter Writing Guides — Nigerian CV">
<meta property="og:description" content="Free guides on writing a professional CV and cover letter in Nigeria, plus tailored advice for 46 job categories.">
<meta property="og:type" content="website">
<link rel="stylesheet" href="../css/theme.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "CV & Cover Letter Writing Guides",
  "publisher": {{ "@type": "Organization", "name": "Nigerian CV" }}
}}
</script>
</head>
<body class="mesh-bg">
  <div class="topbar">
    <a class="back-link" href="../index.html">← Home</a>
    <div class="brand"><span class="seal">N</span>Nigerian CV</div>
  </div>
  <nav class="site-nav">
    <a href="../index.html">Home</a>
    <a href="../cv.html">CV Templates</a>
    <a href="../cover-letter.html">Cover Letters</a>
    <a href="index.html" class="active">Guides</a>
  </nav>

  <div class="wrap">
    <div class="article-hero">
      <span class="eyebrow">Free Guides</span>
      <h1 style="font-size:24px;">CV &amp; Cover Letter Writing Guides</h1>
      <p class="lede" style="font-size:14px;">Start with the general guides, then find tailored advice for your exact job category below.</p>
    </div>

    <div class="doc-choice" style="grid-template-columns:1fr 1fr;">
      <a href="cv-writing-guide.html">
        <span class="ico">📄</span>
        <span>CV Guide</span>
      </a>
      <a href="cover-letter-guide.html">
        <span class="ico">✉️</span>
        <span>Cover Letter Guide</span>
      </a>
    </div>

    <form class="search-bar" style="margin-top:18px;" onsubmit="return false;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="2"/><path d="M20 20L16.6 16.6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <input id="jobSearch" type="text" placeholder="Find your job category… e.g. Plumbing" />
    </form>

    <h2 style="font-size:16px;margin-top:24px;">Guides by job category</h2>
    <div class="job-guide-grid" id="jobGrid">
      {''.join(cards)}
    </div>
  </div>

  <p class="foot-note">Nigerian CV · Built for job seekers across Nigeria 🇳🇬</p>

  <script>
    document.getElementById('jobSearch').addEventListener('input', (e) => {{
      const q = e.target.value.trim().toLowerCase();
      document.querySelectorAll('#jobGrid .job-guide-card').forEach((card) => {{
        card.style.display = card.textContent.toLowerCase().includes(q) ? '' : 'none';
      }});
    }});
  </script>
</body>
</html>
"""
with open(f"{ROOT}/guides/index.html", "w", encoding="utf-8") as f:
    f.write(hub)
print("Generated guides/index.html")
