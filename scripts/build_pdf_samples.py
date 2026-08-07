"""
Regenerates the sample PDFs in /samples/*.pdf plus samples/manifest.json.

Requires:
  pip install playwright --break-system-packages && playwright install chromium

Usage (from the project root, with a local server already running):
  python3 -m http.server 8000 &
  python3 scripts/build_pdf_samples.py --base-url http://localhost:8000

Then regenerate the browsing page:
  python3 scripts/build_samples_page.py
"""
import argparse
import json
import os
import time

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "samples")

# (filename, doc type, layout, theme, profession, label)
JOBS = [
    ("cv-sidebar-navy-signature",        "cv", "sidebar-navy",        "signature", "software-engineer",     "CV — Sidebar (Signature colour) — Software Engineer"),
    ("cv-minimal-ats-signature",         "cv", "minimal-ats",         "signature", "graduate-nysc",          "CV — Minimal ATS (Signature) — Graduate / NYSC"),
    ("cv-banking-band-signature",        "cv", "banking-band",        "signature", "banking-finance",        "CV — Header Band (Signature) — Banking & Finance"),
    ("cv-two-column-classic-signature",  "cv", "two-column-classic",  "signature", "legal-paralegal",        "CV — Two-Column Classic (Signature) — Legal / Paralegal"),
    ("cv-timeline-clean-signature",      "cv", "timeline-clean",      "signature", "nurse-healthcare",       "CV — Timeline (Signature) — Nurse / Healthcare"),
    ("cv-compact-modern-signature",      "cv", "compact-modern",      "signature", "sales-marketing",        "CV — Compact Modern (Signature) — Sales & Marketing"),
    ("cv-portrait-modern-signature",     "cv", "portrait-modern",     "signature", "hospitality-hotel",      "CV — Portrait Modern (Signature) — Hospitality & Hotel"),
    ("cv-print-classic-bw",              "cv", "print-classic",       "signature", "customer-service-admin", "CV — Print Classic — Customer Service & Admin"),
    ("cv-sidebar-navy-mono",             "cv", "sidebar-navy",        "mono",      "engineering-technical",  "CV — Sidebar (Black & White) — Engineering"),

    ("cl-classic-block-signature",       "cover-letter", "classic-block",  "signature", "general",             "Cover Letter — Classic Block (Signature) — General"),
    ("cl-modern-header-signature",       "cover-letter", "modern-header",  "signature", "sales-marketing",     "Cover Letter — Modern Header (Signature) — Sales & Marketing"),
    ("cl-minimal-line-signature",        "cover-letter", "minimal-line",   "signature", "engineering-technical","Cover Letter — Minimal Line (Signature) — Engineering"),
    ("cl-elegant-serif-signature",       "cover-letter", "elegant-serif",  "signature", "legal-paralegal",     "Cover Letter — Elegant Serif (Signature) — Legal / Paralegal"),
    ("cl-print-minimal-bw",              "cover-letter", "print-minimal",  "signature", "teacher-education",   "Cover Letter — Print Minimal — Teacher / Education"),
    ("cl-classic-block-mono",            "cover-letter", "classic-block",  "mono",      "government-civil-service", "Cover Letter — Classic Block (Black & White) — Government"),
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://localhost:8000")
    args = parser.parse_args()

    os.makedirs(OUT_DIR, exist_ok=True)
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 850, "height": 1100})
        for fname, doctype, layout, theme, profession, label in JOBS:
            url = f"{args.base_url}/render.html?type={doctype}&layout={layout}&theme={theme}&profession={profession}&mode=sample"
            page.goto(url, wait_until="networkidle")
            time.sleep(0.3)
            height = page.evaluate("document.getElementById('doc-root').scrollHeight")
            out_path = os.path.join(OUT_DIR, f"{fname}.pdf")
            page.pdf(path=out_path, width="850px", height=f"{height}px",
                     print_background=True,
                     margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
            size_kb = round(os.path.getsize(out_path) / 1024, 1)
            results.append((fname, label, doctype, layout, theme, profession, size_kb))
            print(f"{fname}.pdf  ({size_kb} KB)")
        browser.close()

    with open(os.path.join(OUT_DIR, "manifest.json"), "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nDone: {len(results)} PDFs written to {OUT_DIR}")


if __name__ == "__main__":
    main()
