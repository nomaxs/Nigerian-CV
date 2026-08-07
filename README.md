# Nigerian CV — CV & Cover Letter Builder

A no-login, mobile-first static site for building a Nigerian-style CV or
cover letter and downloading it as a PDF. **24 CV designs and 15 cover
letter designs**, each available in colour and in a dedicated
**black-and-white** variant for anyone printing on a monochrome printer,
across **46 job categories** with tailored preview data, autofill
presets, optional photo upload, a real logo/favicon set, 15 downloadable
sample PDFs, and 48 free CV/cover-letter writing guides. Pure HTML/CSS/JS
— no build step, no backend. Ready to push straight to GitHub and host
on GitHub Pages, Cloudflare Pages, Netlify or Vercel.

## Try it locally

Browser security rules block `fetch()` on `file://` pages, so serve the
folder over http instead of double-clicking `index.html`:

```bash
cd nigerian-cv
python3 -m http.server 8080
# open http://localhost:8080
```

## Before you deploy

Every canonical URL, Open Graph tag, JSON-LD block and the sitemap
currently point at the placeholder domain `nigeriancv.example.com`.
Once you know your real domain, run:

```bash
grep -rl "nigeriancv.example.com" . | xargs sed -i 's/nigeriancv.example.com/YOURDOMAIN.com/g'
python3 scripts/build_sitemap.py   # regenerates sitemap.xml + robots.txt with the fixed BASE
```

(update the `BASE` constant near the top of `scripts/build_sitemap.py` first).

## How the template count works

Rather than hand-authoring dozens of near-identical files, each
template card in the gallery is a **layout × colour-theme** combination:

- **8 CV layouts** (Sidebar, Minimal ATS, Header Band, Two-Column
  Classic, Timeline, Compact Modern, Portrait Modern, Print Classic) ×
  **3 themes** (Signature colour, Alternate colour, Black & White) =
  **24 CV templates**
- **5 cover letter layouts** (Classic Block, Modern Header, Minimal
  Line, Elegant Serif, Print Minimal) × **3 themes** = **15 cover
  letter templates**

The **Black & White** theme isn't just a CSS filter — it's a real
colour-token override (`data/layouts.json`) that swaps every accent
colour for ink, charcoal and grey. **Portrait Modern** and **Compact
Modern** additionally support an uploaded photo (`supportsPhoto: true`
in `data/layouts.json`); **Print Classic** and **Print Minimal** use no
colour fills at all, by design, for anyone printing on a monochrome
printer or photocopier.

**46 job categories** (Software Engineer, Nurse, Teacher, Banking,
Plumbing, Pharmacy, Event Planning, and so on — the same 46 for both
CVs and cover letters) don't add more template files either: picking a
job category swaps the **sample data** used to preview all 24 (or 15)
templates, so every design shows a realistic, Nigerian,
profession-appropriate document instantly. The same 46 categories also
drive **autofill** — arriving at the form with `?profession=<id>` in
the URL pre-fills every field with that job's sample entry, which the
person then edits rather than starting from a blank form.

## How it's organised

```
index.html              Landing page
cv.html                  CV gallery — job-category chips, colour/B&W filter,
                          search, 24 live templates
cover-letter.html        Cover letter gallery — 15 live templates
create.html               The data-entry form (shared by both document types).
                          Reads ?profession= to autofill from a job preset,
                          and shows a photo upload field for layouts that
                          support one.
preview.html              Full preview + "watch an ad to download" PDF flow
render.html                The engine that turns layout + theme + data into a
                          document (used inside iframes: thumbnails, overlay,
                          preview, print). noindex — not a content page.

guides/index.html         Guides hub — search/browse all 46 job guides
guides/cv-writing-guide.html        General "how to write a Nigerian CV" guide
guides/cover-letter-guide.html      General cover-letter guide
guides/jobs/<job-id>.html            46 tailored job-specific guides, each with
                          real skills/achievement examples pulled from
                          data/professions.json and CTA buttons that deep-link
                          into the pre-filled form

samples/index.html         Browsable gallery of 15 downloadable sample PDFs
samples/*.pdf                The PDFs themselves — real print-to-PDF exports,
                          not mockups
samples/manifest.json       What's in each sample PDF — read by
                          scripts/build_samples_page.py

assets/logo.svg             Brand mark (see "Logo & brand assets" below)
assets/favicon*.png, apple-touch-icon.png, icon-512.png, og-image.png

css/theme.css             The whole site design system (colour, type, buttons,
                          nav, filters, guide/article styling)
js/render.js               Data-binding engine (data-field / data-field-html /
                          data-field-img / data-list / data-if)
js/gallery.js              Builds the layout×theme grid, job-category chips,
                          colour/B&W filter, preview overlay
js/form.js                 The form: repeatable sections, tag inputs, photo
                          upload, profession autofill, autosave
js/util.js                 Shared helpers (toast, query-string reader)

data/layouts.json          Every layout, its two colour themes, the shared
                          Black & White theme, and which layouts support a photo
data/professions.json       Sample CV/cover-letter data per job category —
                          used for gallery previews AND form autofill

scripts/build_professions.py   Generates data/professions.json from compact
                          per-profession definitions — the fast way to add
                          or edit many job categories at once
scripts/build_guides.py        Generates guides/index.html and all 46
                          guides/jobs/<id>.html pages from data/professions.json
scripts/build_sitemap.py       Generates sitemap.xml + robots.txt from every
                          indexable page

sitemap.xml, robots.txt    SEO — see "Before you deploy" above

templates/
  cv/layouts/
    sidebar-navy/           template.html + style.css (theme-variable driven)
    minimal-ats/
    banking-band/
    two-column-classic/
    timeline-clean/
    compact-modern/          supports an optional uploaded photo
    portrait-modern/          supports an optional uploaded photo
    print-classic/            no colour fills — built for B&W printing
  cover-letter/layouts/
    classic-block/
    modern-header/
    minimal-line/
    elegant-serif/
    print-minimal/            no colour fills — built for B&W printing
```

## Adding a new layout (no code changes needed elsewhere)

1. Duplicate a folder under `templates/cv/layouts/` or
   `templates/cover-letter/layouts/`, e.g. `templates/cv/layouts/executive/`.
2. Write `template.html` using the same `data-field`/`data-field-html`/
   `data-field-img`/`data-list`/`data-if` binding vocabulary as the
   others (see below), and `style.css` using `var(--t-primary)`,
   `var(--t-accent)`, `var(--t-ink)`, `var(--t-muted)`, `var(--t-line)`,
   `var(--t-surface)`, `var(--t-primary-ink)` for every colour — never a
   hardcoded hex — so the Black & White theme works automatically.
3. Add one entry to `data/layouts.json` under `cv` (or `cover-letter`)
   with a `signature` and an `alt` colour palette. `mono` is shared
   across every layout and needs no per-layout entry. Add
   `"supportsPhoto": true` if the layout includes a
   `data-field-img="personal.photo"` element.

That's it — the layout now appears in the gallery three times
(Signature / Alt / Black & White), for every job category, automatically.

## Adding a new job category

1. Add one entry to **both** the `cv` and `cover-letter` arrays in
   `data/professions.json` (or, more easily, add one entry to the
   `NEW` list in `scripts/build_professions.py` and re-run it), using
   the same `id` in each, with a `name`, `tags` (for search) and a
   `sample` object matching the data shape below.
2. Re-run `python3 scripts/build_guides.py` and
   `python3 scripts/build_sitemap.py` to generate that job's guide
   page and add it to the sitemap.

It immediately becomes selectable in both galleries, previews against
all 24 CV templates and all 15 cover letter templates, autofills the
form via `?profession=<id>`, and gets its own guide page — no other
file to hand-edit.

## Data-binding vocabulary (inside `template.html` files)

- `data-field="personal.fullName"` — fills the element's text from that path
- `data-field-html="personal.summary"` — same, but line breaks become `<br>`
- `data-field-img="personal.photo"` — sets the element's `src`; the
  element is removed entirely if the value is empty, so a photo-less
  CV never shows a broken image icon
- `data-list="experience"` — the element holds one `<template>`, cloned once
  per array item; inside the clone, `data-field="company"` reads from the
  current item, and `data-field="."` reads the item itself (for arrays of
  plain strings, like skills)
- `data-if="personal.linkedin"` — the element is removed entirely if that
  value is empty, so optional sections (LinkedIn, references, an
  uploaded photo, etc.) never render as blank headings

## The CV/cover-letter data shape

```js
// CV
{
  personal: { fullName, title, phone, email, location, linkedin, summary, photo },
  education: [{ institution, degree, course, year }],
  experience: [{ company, position, dates, responsibilities: [""] }],
  skills: [""], certifications: [""], languages: [""],
  references: [{ name, relation, phone, email }]
}

// Cover letter
{
  personal: { fullName, phone, email, location },
  recipient: { hiringManager, company, companyAddress },
  date, salutation, body: [""], closing
}
```

`personal.photo` is a data URL (from the browser's own FileReader),
never uploaded anywhere — it lives only in `sessionStorage` on the
person's device, same as the rest of their draft.

## The "ad-gated PDF download"

`preview.html` shows a 5-second progress modal to stand in for a rewarded
video ad, then calls `iframe.contentWindow.print()` scoped to just the
document (not the surrounding chrome) — the person picks "Save as PDF" in
their browser's print dialog. This keeps the whole project dependency-free
and works offline, and prints cleanly in black-and-white regardless of
which theme was chosen. To swap in a real ad SDK, replace the
`setInterval` in `preview.html`'s `downloadBtn` handler with your SDK's
rewarded-ad call, and call `triggerDownload()` in its completion callback.

## SEO

- `sitemap.xml` / `robots.txt` — regenerate with `scripts/build_sitemap.py`
  after fixing the placeholder domain (see "Before you deploy").
- Every indexable page (`index.html`, `cv.html`, `cover-letter.html`,
  the 2 general guides, and all 46 job guides) has a unique `<title>`,
  meta description, canonical URL, Open Graph tags, and JSON-LD
  structured data (`WebSite`, `BreadcrumbList` or `Article`).
- `create.html`, `preview.html` and `render.html` are marked
  `noindex` — they're transactional/tool pages with no unique content
  per URL, so indexing them would just create thin/duplicate pages.
- The 46 job guide pages are real, unique, static HTML with genuinely
  different content per page (pulled from `data/professions.json`) —
  not 46 copies of the same template — which is what makes them worth
  indexing individually rather than as one combined page.

## Not built yet

- Accounts / saving multiple CVs (currently: one draft per
  layout+theme, autosaved to `sessionStorage` — cleared when the
  browser tab closes)
- Premium templates / paid tier
- AI rewriting assistance
- A real rewarded-ad SDK (currently simulated — see above)

## Logo & brand assets

`assets/logo.svg` is the source-of-truth mark — a document-and-seal
icon in the same blue/coral palette as the rest of the site. Every
page's `<link rel="icon">`, `<link rel="apple-touch-icon">` and
`og:image` are generated from it:

```
assets/
  logo.svg                 vector source (used directly in every page's nav)
  favicon.ico, favicon-16.png, favicon-32.png, favicon-48.png
  apple-touch-icon.png      180×180, for iOS home-screen bookmarks
  icon-512.png              large raster version (PWA-manifest-ready)
  og-image.png              1200×630 social-share card
```

To change the logo: edit `assets/logo.svg`, then regenerate the raster
sizes and the OG image (both were produced by rendering the SVG in a
headless browser and exporting with Pillow — there's no single script
for this yet, since it was a one-off design pass; open the SVG in any
vector tool and re-export the sizes listed above if you want to change it).

## Sample PDF downloads

`/samples/index.html` lists 15 real, finished PDF exports — one per
layout (in its signature colour) plus a few Black & White showcases —
generated with `scripts/build_pdf_samples.py` using headless
Chromium's native print-to-PDF (the same mechanism `preview.html` uses
for real users' downloads, so these are a true preview of output
quality, not mockups). Regenerate after changing a layout or adding a
new one:

```bash
python3 -m http.server 8000 &
python3 scripts/build_pdf_samples.py --base-url http://localhost:8000
python3 scripts/build_samples_page.py   # rebuilds samples/index.html from the new manifest
```
