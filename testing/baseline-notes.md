# CrawlMetric Clean Baseline

This repository is the known-good baseline for the future CrawlMetric controlled testing environment. It intentionally uses sound semantic, accessibility, indexing, navigation, metadata, and responsive-design practices. No test defects have been introduced.

## Baseline scope

- Five static, internally linked HTML pages
- Unique page titles and meta descriptions
- One canonical URL per page using the reserved `.example` domain
- Semantic landmarks and logical heading structures
- Descriptive alternative text for meaningful images
- Labeled, keyboard-accessible prototype form controls
- Responsive navigation and reduced-motion support
- Valid `robots.txt` and XML sitemap structure
- Original generated imagery stored locally in `/images`
- Lightweight, dependency-free JavaScript

## Important deployment note

Before a real deployment, replace `https://fayettevilleanimalhospital.example` in canonical tags, `robots.txt`, and `sitemap.xml` with the final public origin. The `.example` domain is deliberately non-production and prevents this fictional project from being confused with a real clinic.

## Prototype behavior

The appointment form is front-end only. Submission is intercepted in the browser, a confirmation is displayed, and no personal information is transmitted or stored.

## Future testing

Record every controlled defect in `test-matrix.md` before introducing it. Preserve this clean state in version control so experiments remain reversible and measurable.
