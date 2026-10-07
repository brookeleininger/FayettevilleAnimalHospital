# CrawlMetric Expanded Clean Baseline

This repository contains the expanded, technically clean baseline for the future CrawlMetric controlled testing environment. It contains **60 indexable HTML pages** and intentionally includes no test defects.

## Architecture

- 5 core pages: Home, About, Services, Resources, and Contact
- 12 detailed service pages under `/services/`
- 6 life-stage guides under `/pet-care/`
- 20 owner education articles under `/resources/articles/`
- 8 care and condition guides under `/resources/conditions/`
- 4 fictional team profiles under `/team/`
- 5 visit-planning and supporting pages at the site root

The architecture uses hub-and-spoke internal linking. Services, Resources, and About are primary hubs; deeper pages include breadcrumbs, contextual links, related content, and appointment pathways. The main navigation remains intentionally compact.

## Clean-baseline status

- Unique titles, meta descriptions, H1s, and canonical URLs are required sitewide.
- Canonicals use `https://brookeleininger.github.io/FayettevilleAnimalHospital/`.
- Relative links and assets support GitHub Pages project hosting.
- `robots.txt` allows crawling and points to the full XML sitemap.
- The fictional-practice disclosure appears in the footer throughout the expanded templates.
- No intentional SEO, accessibility, indexability, schema, link, or content defects have been introduced.

## CrawlMetric workflow

This expanded site is intended to be crawled with Screaming Frog and recorded as the clean baseline before any controlled defects are added. Preserve this state in version control so later experiments remain reversible and measurable. Record every future controlled issue in `test-matrix.md` before implementation.

## Controlled Defect Phase

The clean 60-page baseline was preserved separately before this project entered the controlled-defect phase. A clean Screaming Frog crawl was also saved before modification.

This working version now contains exactly 50 intentionally planted defects covering titles and descriptions, headings and content, images and alternative text, links and response-code behavior, canonicals and indexability, sitemap and crawlability, internal architecture, structured data, and file-level performance concerns. The complete ground-truth answer key is maintained in `testing/test-matrix.md` as CM-001 through CM-050.

The visual design, responsive layout, branding, imagery style, and fictional-practice disclosure were intentionally preserved. This version is the pre-CrawlMetric “bad” website and is intentionally **not SEO clean**. The documented defects must remain in place until the CrawlMetric detection and approved-remediation stages of the experiment.
