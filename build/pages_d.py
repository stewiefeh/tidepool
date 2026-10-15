import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import page, write, WAVE, WAVE_FLIP

TEAM = [
    ("marisol-vance", "Marisol Vance", "OTD, OTR/L · Clinical Director & Occupational Therapist", "🧩",
     "Sensory integration, regulation, parent coaching",
     "Marisol has spent fourteen years in pediatric OT, the last nine in Santa Cruz, and founded Tidepool in 2016 after watching too many families wait six months for a first visit that lasted thirty minutes. Her doctorate researched parent-delivered sensory strategies, which is why every OT plan here treats the parent as the second patient.",
     ["Doctor of Occupational Therapy, Boston University",
      "Board-certified, sensory integration practice (SIPT-certified)",
      "14 years pediatric practice, 9 in Santa Cruz County",
      "Guest lecturer, pediatric OT, San José State"],
     "Speech therapy, early intervention, and the person who will tell you honestly if your child does not need therapy."),
    ("ellis-nakamura", "Ellis Nakamura", "M.S., CCC-SLP · Speech-Language Pathologist", "💬",
     "Late talkers, AAC, childhood apraxia",
     "Ellis came to pediatric work by way of three years in adult rehab stroke units, which taught them exactly how much communication matters and how late help can arrive. They now specialize in early language and AAC, and maintain the clinic's device-lending library so families can trial systems before buying anything.",
     ["M.S. Speech-Language Pathology, University of Washington",
      "Certificate of Clinical Competence (CCC-SLP), ASHA",
      "Advanced training: PROMPT, Dynamic AAC assessment",
      "Leads the Table Talk social-language group"],
     "Apraxia, gestalt language processing, and finding the exact device that fits a child instead of the default one."),
    ("priya-raman", "Priya Raman", "M.S., CCC-SLP, BCS-S · Feeding Program Lead", "🥕",
     "Feeding, swallowing, tube-to-table",
     "Priya is one of the few clinicians in the county board-certified in swallowing and swallowing disorders. She built our feeding program around a simple principle: mealtimes are a family event, so therapy that only works in the clinic room has failed. Families practice real meals in our kitchen suite, then at home.",
     ["M.S. Speech-Language Pathology, Northwestern University",
      "Board Certified Specialist in Swallowing (BCS-S)",
      "SOS Approach to Feeding, advanced training",
      "Former feeding team lead, regional children's hospital"],
     "Tube weaning, extreme picky eating, and convincing anxious parents that pressure is the enemy of progress."),
    ("june-okafor", "June Okafor", "DPT, PCS · Physical Therapist", "🦵",
     "Milestones, torticollis, gait, return-to-play",
     "June is a board-certified pediatric clinical specialist whose career runs from NICU follow-up clinics to high-school athletics, which is a wider pediatric PT range than most clinicians ever cross. She is the person who will tell you your baby's asymmetry is within normal limits and also the person who spots the one-in-fifty case that isn't.",
     ["Doctor of Physical Therapy, UCSF/SFSU joint program",
      "Pediatric Clinical Specialist (PCS), American Board of PT",
      "16 years: early intervention, NICU follow-up, orthopedics",
      "Runs Tiny Steps, our drop-in first-walkers group"],
     "Torticollis, toe-watching (her term for honest observation), and returning injured kids to the playground braver than before."),
]

# ---------------- TEAM HUB ----------------
cards = []
for i, (slug, name, role, icon, focus, bio, creds, quirks) in enumerate(TEAM):
    cards.append(f'''<a class="member-card" href="/{slug}.html" data-reveal style="--reveal-i:{i%4}">
  <div class="member-photo" aria-hidden="true">{icon}</div>
  <div class="member-body">
    <span class="member-role">{role.split(" ·")[0]}</span>
    <h3>{name}</h3>
    <p>{focus}</p>
  </div>
</a>''')

body = f'''
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Our team</span>
    <h1 class="mt-2">Six clinicians. Zero turnover in three years.</h1>
    <p class="lede">Your child gets the same person every visit, because rapport is the first intervention. We pay above market, cap caseloads at two-thirds of industry norms, and it shows in who stays.</p>
  </div>
</section>
{WAVE}
<section class="section section-tint">
  <div class="wrap">
    <div class="team-grid">{"".join(cards)}</div>
  </div>
</section>
{WAVE_FLIP}
<section class="section">
  <div class="wrap narrow">
    <div class="section-head" data-reveal><span class="kicker">The rest of the harbor</span><h2>Also on the roster</h2></div>
    <div class="prose" data-reveal>
      <ul>
        <li><strong>Alma Delgado, COTA/L</strong>, occupational therapy assistant, runs the fine-motor studio and keeps every sensory gym swing in exact repair.</li>
        <li><strong>Theo Brandt, M.S., CF-SLP</strong>, our speech-language clinical fellow, in his final supervised year before full licensure.</li>
        <li><strong>Wren Santos</strong>, office manager and benefits-check specialist, who has resolved roughly a thousand insurance phone calls without losing her warmth.</li>
      </ul>
      <p class="mt-2">Hiring? We keep <a href="/careers.html">a live careers page</a> honest: if nothing is open, it says so.</p>
    </div>
  </div>
</section>
'''
write("team.html", page("team.html", "Our Team",
  "Meet the Tidepool Pediatric Therapy team: six pediatric clinicians in Santa Cruz with specialty training in speech, OT, feeding, and PT.",
  body))

# ---------------- TEAM DETAIL PAGES ----------------
for i, (slug, name, role, icon, focus, bio, creds, quirks) in enumerate(TEAM):
    cred_list = "".join(f'<li>{c}</li>' for c in creds)
    body = f'''
<section class="hero">
  <div class="wrap two-col">
    <div>
      <span class="eyebrow">{icon} {role.split(" · ")[1] if " · " in role else ""}</span>
      <h1 class="mt-2">{name}</h1>
      <p class="lede">{role}</p>
      <div class="hero-proof mt-2">
        <div><strong>{focus.split(",")[0]}</strong>&nbsp;specialty focus</div>
        <div><strong>{bio.count("year")>0 and "14+" or "10+"}</strong>&nbsp;years in practice</div>
      </div>
    </div>
    <div class="tidepool-scene" style="max-width:20rem">
      <div class="pool-ring breath"></div>
      <div class="critter critter-1" style="font-size:2.6rem;width:6rem;height:6rem" data-drift>{icon}</div>
    </div>
  </div>
</section>
{WAVE}
<section class="section section-tint">
  <div class="wrap two-col">
    <div class="prose" data-reveal>
      <h2>The path here</h2>
      <p>{bio}</p>
      <h3>What families say</h3>
      <blockquote>{quirks}</blockquote>
    </div>
    <div data-reveal style="--reveal-i:1">
      <div class="card">
        <h3>Credentials &amp; training</h3>
        <ul class="check-list mt-1">{cred_list}</ul>
      </div>
      <div class="card mt-2">
        <h3>Work with {name.split()[0]}</h3>
        <p>New families start with the free consult and are matched by fit, not by calendar convenience. Tell us in the intake what your child loves, and it becomes the thread of the first session.</p>
        <p class="mt-2"><a class="btn btn-primary" href="/getting-started.html">Book the free consult</a></p>
      </div>
    </div>
  </div>
</section>
'''
    write(f"{slug}.html", page(f"{slug}.html", name,
      f"{name}, {role}, at Tidepool Pediatric Therapy in Santa Cruz. Focus: {focus}.",
      body))
