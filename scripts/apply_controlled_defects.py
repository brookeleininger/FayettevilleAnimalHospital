"""Apply the 50 documented CrawlMetric defects to the expanded clean baseline.

Run only against the intentionally defective experiment copy. The protected clean
baseline must remain separate. Every mutation below maps to testing/test-matrix.md.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://brookeleininger.github.io/FayettevilleAnimalHospital/"

def read(path): return (ROOT / path).read_text(encoding="utf-8")
def write(path, text): (ROOT / path).write_text(text, encoding="utf-8")

def replace(path, old, new, count=1):
    text = read(path)
    found = text.count(old)
    assert found >= count, f"{path}: expected at least {count} copies of {old!r}, found {found}"
    write(path, text.replace(old, new, count))

def sub(path, pattern, replacement, count=1, flags=0):
    text = read(path)
    new, changed = re.subn(pattern, replacement, text, count=count, flags=flags)
    assert changed == count, f"{path}: expected {count} regex replacements, got {changed}: {pattern}"
    write(path, new)

def add_to_head(path, markup):
    replace(path, "</head>", markup + "</head>")

def remove_hub_card(path, href):
    sub(path, rf'<article class="hub-card">(?:(?!</article>).)*href="{re.escape(href)}"(?:(?!</article>).)*</article>', "", flags=re.S)

# A. Titles and meta descriptions: CM-001 through CM-010.
sub("services/wellness-exams.html", r"<title>.*?</title>", "")
duplicate_title = "Preventive Pet Care | Fayetteville Animal Hospital"
sub("services/vaccinations.html", r"<title>.*?</title>", f"<title>{duplicate_title}</title>")
sub("services/parasite-prevention.html", r"<title>.*?</title>", f"<title>{duplicate_title}</title>")
sub("resources/articles/brush-dog-teeth.html", r"<title>.*?</title>", "<title>Teeth</title>")
sub("services/dental-care.html", r"<title>.*?</title>", "<title>Veterinarian Dental Care Pet Dentist Dog Dentist Cat Dentist Fayetteville Arkansas Vet Dental | Fayetteville Animal Hospital</title>")
sub("team/mara-ellison-dvm.html", r"<title>.*?</title>", "<title>Meet Doctor Mara Ellison Fictional Fayetteville Arkansas Veterinarian for Preventive Medicine Puppy Care Kitten Care and Family Pet Wellness | Fayetteville Animal Hospital</title>")
sub("pet-care/puppy-care.html", r'<meta name="description" content="[^"]*">', "")
duplicate_description = "Guidance for healthy adult pets, including preventive visits, daily wellness, and changing care needs."
sub("pet-care/adult-dog-care.html", r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{duplicate_description}">')
sub("pet-care/adult-cat-care.html", r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{duplicate_description}">')
sub("faq.html", r'<meta name="description" content="[^"]*">', '<meta name="description" content="FAQ.">')
long_meta = "Learn about skin allergies and itching in dogs and cats, including scratching, licking, redness, recurring ear concerns, seasonal patterns, food reactions, flea exposure, environmental triggers, secondary infection, diagnostic conversations, home observations, treatment planning, follow-up care, and reasons to contact a veterinarian in Fayetteville, Arkansas."
sub("resources/conditions/skin-allergies.html", r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{long_meta}">')
sub("payment-information.html", r'<meta name="description" content="[^"]*">', '<meta name="description" content="Discover seasonal garden design, lawn care packages, and outdoor planting ideas for beautiful residential landscapes.">')

# B. Headings and content: CM-011 through CM-017.
sub("pet-care/kitten-care.html", r"<h1>Kitten Care</h1>", "")
replace("pet-care/senior-dog-care.html", '<h2>Care for this chapter</h2>', '<h1>Care for this chapter</h1>')
replace("new-patients.html", '<h2>Questions are welcome</h2>', '<h4>Questions are welcome</h4>')
replace("services/diagnostics.html", '<h1>Veterinary Diagnostics</h1>', '<h1>Learn More</h1>')
sub("team/lena-park.html", r'<article class="prose">.*?</article>', '<article class="prose"><p>Lena helps visits feel calm, clear, and welcoming for pets and their people.</p></article>', flags=re.S)
dog_article = re.search(r'<article class="prose">.*?</article>', read("resources/articles/brush-dog-teeth.html"), re.S).group(0)
sub("resources/articles/brush-cat-teeth.html", r'<article class="prose">.*?</article>', dog_article, flags=re.S)
text = read("resources/conditions/pet-anxiety.html")
main_start = text.index('<article class="prose">')
main_end = text.index('</article>', main_start)
section = text[main_start:main_end]
section = section.replace('<h2>', '<h3>').replace('</h2>', '</h3>')
write("resources/conditions/pet-anxiety.html", text[:main_start] + section + text[main_end:])

# C. Images and alt text: CM-018 through CM-023.
sub("about.html", r'(<img src="images/exam-room-cat\.jpg") alt="[^"]*"', r'\1')
sub("index.html", r'(<img src="images/ozark-dog-hero\.jpg") alt="[^"]*"', r'\1 alt=""')
sub("index.html", r'(<img src="images/exam-room-cat\.jpg") alt="[^"]*"', r'\1 alt="image"')
replace("services/dental-care.html", '<article class="prose">', '<article class="prose"><img class="content-photo" src="../images/exam-room-cat.jpg" width="1536" height="1024" alt="Fayetteville veterinarian pet dentist dog dental care cat dental care animal hospital dental veterinarian">')
replace("services/pet-surgery.html", '<article class="prose">', '<article class="prose"><img class="content-photo" src="../images/surgery-suite-missing.jpg" width="1536" height="1024" alt="Prepared veterinary surgery room">')
replace("resources/articles/heartworm-arkansas.html", '<article class="prose">', '<article class="prose"><img class="content-photo" src="../../images/ozark-dog-hero.png" width="1983" height="793" alt="Dog outdoors in the wooded Ozarks">')

# D. Links and redirect behavior: CM-024 through CM-029.
replace("services/nutrition-weight-management.html", 'href="../services/wellness-exams.html"', 'href="../services/metabolic-health.html"')
replace("resources/articles/dog-wellness-frequency.html", 'href="../../resources.html">Return to the resource library</a>', 'href="../../resources/articles/annual-exam-planner.html">Annual exam planning guide</a>')
insert = '<article class="hub-card"><span class="eyebrow">Seasonal guide</span><h2>Holiday Pet Safety</h2><p>Planning guidance for celebrations, food, decorations, and visitors.</p><a class="text-link" href="resources/articles/holiday-pet-safety.html">Learn more</a></article>'
replace("resources.html", '</div></div></section><section class="section section-paper">', insert + '</div></div></section><section class="section section-paper">')
replace("team/nina-solis-dvm.html", 'href="../about.html">Return to About</a>', 'href="../../about.html">Return to About</a>')
replace("resources/conditions/urinary-issues.html", 'href="../../contact.html#appointment">Request an appointment</a>', 'href="../../book-now.html">Request an appointment</a>')
add_to_head("payment-information.html", '<meta http-equiv="refresh" content="2; url=faq.html">')

# E. Canonicals and indexability: CM-030 through CM-035.
sub("services/spay-neuter.html", r'<link rel="canonical" href="[^"]*">', "")
sub("resources/articles/cat-wellness-frequency.html", r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{BASE}resources/articles/dog-wellness-frequency.html">')
sub("resources/conditions/vomiting-diarrhea.html", r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{BASE}resources/conditions/digestive-health.html">')
sub("team/theo-bennett-dvm.html", r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{BASE}about.html">')
add_to_head("services.html", '<meta name="robots" content="noindex,follow">')
sub("pet-care/adult-cat-care.html", r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{BASE}pet-care/adult-dog-care.html">')
add_to_head("pet-care/adult-cat-care.html", '<meta name="robots" content="noindex,follow">')

# F. Sitemap and robots: CM-036 through CM-039.
sitemap = read("sitemap.xml")
urgent = f'  <url><loc>{BASE}services/urgent-sick-care.html</loc></url>\n'
assert urgent in sitemap
sitemap = sitemap.replace(urgent, "", 1)
sitemap = sitemap.replace('</urlset>', f'  <url><loc>{BASE}services/ghost-service.html</loc></url>\n  <url><loc>{BASE}index.html</loc></url>\n</urlset>')
write("sitemap.xml", sitemap)
robots = read("robots.txt")
assert "heartworm-arkansas" not in robots
write("robots.txt", robots.replace("Allow: /", "Allow: /\nDisallow: /FayettevilleAnimalHospital/resources/articles/heartworm-arkansas.html"))

# G. Internal linking and architecture: CM-040 through CM-043.
remove_hub_card("about.html", "team/lena-park.html")
replace("resources/articles/seasonal-allergies-dogs.html", 'href="../../services/behavioral-consultations.html"', 'href="../../services/diagnostics.html"')
replace("resources/conditions/pet-anxiety.html", 'href="../../services/behavioral-consultations.html"', 'href="../../services/diagnostics.html"')
replace("new-patients.html", '<h4>Questions are welcome</h4>', '<p>For a detailed visit overview, <a href="what-to-expect.html">click here</a>.</p><h4>Questions are welcome</h4>')
remove_hub_card("resources.html", "resources/articles/healthy-weight-cats.html")
remove_hub_card("resources.html", "resources/articles/new-kitten-checklist.html")
replace("resources/articles/brush-cat-teeth.html", '</article><aside', '<p><a href="new-kitten-checklist.html">Continue to our new kitten checklist</a>.</p></article><aside')
replace("resources/articles/new-kitten-checklist.html", '</article><aside', '<p><a href="healthy-weight-cats.html">Continue to healthy weight guidance for cats</a>.</p></article><aside')

# H. Structured data: valid controls plus CM-044 through CM-047 defects.
def jsonld(path, data):
    add_to_head(path, '<script type="application/ld+json">' + json.dumps(data, separators=(",", ":")) + '</script>')

article_files = sorted((ROOT / "resources/articles").glob("*.html"))
for file in article_files:
    slug = file.stem
    if slug in {"dog-wellness-frequency", "puppy-vaccines"}:
        continue
    title_match = re.search(r'<h1>(.*?)</h1>', file.read_text(encoding="utf-8"))
    headline = re.sub('<[^>]+>', '', title_match.group(1)) if title_match else slug.replace('-', ' ').title()
    jsonld(file.relative_to(ROOT), {"@context":"https://schema.org","@type":"Article","headline":headline,"publisher":{"@type":"Organization","name":"Fayetteville Animal Hospital"},"url":BASE+file.relative_to(ROOT).as_posix()})
add_to_head("resources/articles/puppy-vaccines.html", '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"What Vaccines Does My Puppy Need?",}</script>')
for path, name in [("team/mara-ellison-dvm.html","Dr. Mara Ellison"),("team/theo-bennett-dvm.html","Dr. Theo Bennett"),("team/lena-park.html","Lena Park")]:
    jsonld(path,{"@context":"https://schema.org","@type":"Person","name":name,"worksFor":{"@type":"Organization","name":"Fayetteville Animal Hospital"}})
jsonld("team/nina-solis-dvm.html",{"@context":"https://schema.org","@type":"Person","name":"Dr. Nina Solis","worksFor":{"@type":"VeterinaryCare"}})
for path, url in [("services/wellness-exams.html",BASE+"services/wellness-exams.html"),("services/pet-surgery.html",BASE+"services/pet-surgery.html")]:
    jsonld(path,{"@context":"https://schema.org","@type":"VeterinaryCare","name":"Fayetteville Animal Hospital","url":url})
jsonld("services/dental-care.html",{"@context":"https://schema.org","@type":"VeterinaryCare","name":"Fayetteville Animal Hospital","url":"dental care near me"})

# I. Performance and technical: CM-048 through CM-050.
replace("resources/articles/new-kitten-checklist.html", '<article class="prose">', '<article class="prose"><img class="content-photo" src="../../images/resources-cat-care.jpg" alt="Orange tabby cat receiving gentle grooming at home">')
replace("resources/conditions/pet-obesity.html", '<link rel="stylesheet" href="../../css/style.css">', '<link rel="stylesheet" href="../../css/style.css"><link rel="stylesheet" href="../../css/style.css">')
replace("team/theo-bennett-dvm.html", '<script src="../js/script.js" defer></script>', '<script src="../js/script.js"></script><script src="../js/script.js" defer></script>')

print("Applied controlled defects CM-001 through CM-050")
