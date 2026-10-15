import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import page, write, WAVE, CANON, V, logo

def simple_head(icon, kicker, title, lede):
    return f'''
<section class="hero"><div class="wrap narrow">
  <span class="eyebrow">{icon} {kicker}</span>
  <h1 class="mt-2">{title}</h1>
  <p class="lede">{lede}</p>
</div></section>
{WAVE}'''

# ---------------- PRIVACY ----------------
body = simple_head("🔒", "Privacy", "Privacy policy", "Short version: this is a portfolio website. We collect nothing, track nothing, and store nothing. The long version is still short.") + '''
<section class="section section-tint"><div class="wrap narrow"><div class="prose">
<h2>What this site collects</h2>
<p>Nothing. No analytics, no cookies, no tracking pixels, no ad scripts, no session recording, no fonts loaded from third parties that would phone home. Every asset on this site, including the two typefaces, is served from this domain.</p>
<h2>The demo forms</h2>
<p>The consult request, contact, and newsletter forms are demonstrations. When you submit one, the site validates the fields locally, shows a confirmation message that says it's a demo, and discards everything. Nothing is transmitted to any server, and no personal data is stored anywhere by us.</p>
<h2>Children's information</h2>
<p>Because the fictional clinic this site depicts serves children, we say it plainly anyway: if a real site operated this way, it would not knowingly collect any personal information from children under 13, in line with COPPA, and this portfolio site collects nothing from anyone of any age.</p>
<h2>Third parties</h2>
<p>The site is hosted on Cloudflare Pages. Cloudflare's standard CDN handling applies to page requests, as it does to every site on the platform. We have added no analytics, marketing, or advertising integrations of any kind.</p>
<h2>Changes</h2>
<p>If this page ever changes, the change will be dated at the bottom of this page. As of the date below, the policy is: nothing collected, nothing stored, nothing shared.</p>
<p style="color:var(--ink-faint);font-size:var(--step--1)">Tidepool Pediatric Therapy is a fictional clinic created as a design portfolio piece. Any resemblance to a real clinic is coincidental. Questions about this page: hello@tidepoolcare.example.</p>
<p style="color:var(--ink-faint);font-size:var(--step--1)">Last updated: October 15, 2026</p>
</div></div></section>
'''
write("privacy.html", page("privacy.html", "Privacy Policy",
  "Privacy policy for this portfolio site: no analytics, no cookies, no tracking; demo forms transmit nothing and store nothing.",
  body))

# ---------------- TERMS ----------------
body = simple_head("📜", "Terms", "Terms of use", "Using this site means agreeing to the sensible terms below. They exist mostly to keep the fiction honest.") + '''
<section class="section section-tint"><div class="wrap narrow"><div class="prose">
<h2>What this site is</h2>
<p>This is a fictional portfolio website. Tidepool Pediatric Therapy, its clinicians, address, phone number, credentials, outcomes, and rates are invented. No real medical practice is described, and no real patients or families appear here.</p>
<h2>No medical advice</h2>
<p>Nothing on this site is medical advice, and nothing here establishes a clinician-patient relationship, because no such relationship is possible with a portfolio piece. The resource guides reflect real, publicly documented clinical principles but cannot account for any real child's situation. For concerns about a real child, speak with a licensed pediatric professional.</p>
<h2>Do not misrepresent this site</h2>
<p>You may not present this site as a real clinic, quote its fictional rates or outcomes as real, or use its contact details for any real-world solicitation. Reviewers, recruiters, and evaluators: everything here was authored as design work, and that framing should travel with any excerpt.</p>
<h2>Permitted use</h2>
<p>You may view, share, and link to this site freely. Educational discussion of its design is welcome. You may not copy its code or content into a product, or present it as your own work.</p>
<h2>Copyright &amp; contact</h2>
<p>© 2026 Stephen Fehon. The design, code, and text of this site are the author's work. Questions: hello@tidepoolcare.example.</p>
<p style="color:var(--ink-faint);font-size:var(--step--1)">Last updated: October 15, 2026</p>
</div></div></section>
'''
write("terms.html", page("terms.html", "Terms of Use",
  "Terms of use for this fictional portfolio site: no medical advice, do not misrepresent the clinic as real, permitted use.",
  body))

# ---------------- ACCESSIBILITY ----------------
body = simple_head("♿", "Accessibility", "Accessibility statement", "Built to WCAG 2.2 AA on purpose, and measured against it, not just claimed.") + '''
<section class="section section-tint"><div class="wrap narrow"><div class="prose">
<h2>What that means here</h2>
<ul>
  <li><strong>Contrast:</strong> all text is deep ink-teal on warm light surfaces, checked at AA for body text and AAA for headings. No low-contrast gray-on-gray anywhere.</li>
  <li><strong>Keyboard:</strong> every interactive element is reachable and operable by keyboard, with a visible focus ring that never disappears. A skip link jumps straight to content.</li>
  <li><strong>Motion:</strong> all animation respects the system reduced-motion setting. With it enabled, reveals, drifts, and the breathing pool are neutralized instantly.</li>
  <li><strong>Structure:</strong> one h1 per page, landmarks for header, main, and footer, form fields with real labels, and error states that are announced rather than colored only.</li>
  <li><strong>Zoom:</strong> layouts hold at 200% zoom and reflow to single column; no horizontal scrolling is ever required to read text.</li>
</ul>
<h2>Known limits</h2>
<p>The decorative tidepool illustration is aria-hidden and conveys nothing required. The tide clock is a playful detail that duplicates the time, so missing it costs nothing. If you use a screen reader and find a gap we missed, tell us; accessibility fixes at this site rank above every feature request.</p>
<p style="color:var(--ink-faint);font-size:var(--step--1)">Statement reviewed October 15, 2026 against WCAG 2.2 Level AA.</p>
</div></div></section>
'''
write("accessibility.html", page("accessibility.html", "Accessibility",
  "Accessibility statement: WCAG 2.2 AA target, reduced-motion support, keyboard operability, and known limits.",
  body))

# ---------------- SITE MAP ----------------
PAGES_MAP = [
    ("Main", [("index.html","Home"),("about.html","About the clinic"),("services.html","Therapy services"),("team.html","Our team"),("getting-started.html","Getting started")]),
    ("Therapies", [("speech-therapy.html","Speech & language"),("occupational-therapy.html","Occupational therapy"),("feeding-therapy.html","Feeding therapy"),("physical-therapy.html","Physical therapy")]),
    ("People", [("marisol-vance.html","Marisol Vance, OT"),("ellis-nakamura.html","Ellis Nakamura, SLP"),("priya-raman.html","Priya Raman, feeding"),("june-okafor.html","June Okafor, PT")]),
    ("Families", [("faq.html","FAQ"),("insurance.html","Insurance & rates"),("resources.html","Family resources"),("resource-milestones.html","Milestones guide"),("resource-insurance-rights.html","Insurance rights guide"),("resource-first-words.html","Late talkers guide")]),
    ("Journal", [("journal.html","Journal"),("journal-waitlists.html","The waiting list"),("journal-screens.html","Screens & labels"),("journal-pronouns.html","The child who refused")]),
    ("Clinic", [("careers.html","Careers"),("contact.html","Contact & directions"),("privacy.html","Privacy"),("terms.html","Terms"),("accessibility.html","Accessibility"),("404.html","404 page")]),
]
rows = ""
for group, links in PAGES_MAP:
    items = "".join(f'<li><a href="/{f}">{t}</a></li>' for f, t in links)
    rows += f'<div class="card" data-reveal><h3>{group}</h3><ul style="list-style:none;padding:0;display:grid;gap:0.5rem;margin-top:0.6rem">{items}</ul></div>'
body = simple_head("🧭", "Site map", "Every page, one list.", "Twenty-eight pages and every one reachable in two clicks or fewer from the home page.") + f'''
<section class="section section-tint"><div class="wrap"><div class="card-grid">{rows}</div></div></section>
'''
write("site-map.html", page("site-map.html", "Site Map",
  "Full site map for the Tidepool Pediatric Therapy portfolio site.",
  body))

# ---------------- 404 ----------------
body = f'''
<section class="hero" style="text-align:center">
  <div class="wrap narrow">
    <div class="tidepool-scene" style="max-width:14rem;margin-bottom:1.5rem" aria-hidden="true">
      <div class="pool-ring breath"></div>
      <div class="critter critter-1" style="font-size:2rem;width:4.5rem;height:4.5rem;left:28%;top:30%">🦀</div>
    </div>
    <span class="eyebrow">404</span>
    <h1 class="mt-2">This tidepool is empty.</h1>
    <p class="lede" style="margin-inline:auto">The page you're after drifted out with the tide. The good news: everything else is one click away.</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-primary" href="/">Back to the harbor</a>
      <a class="btn btn-ghost" href="/site-map.html">See every page</a>
    </div>
  </div>
</section>
'''
write("404.html", page("404.html", "Page Not Found",
  "Page not found. Head back to the Tidepool home page or browse the full site map.",
  body))
