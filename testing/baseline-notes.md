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
