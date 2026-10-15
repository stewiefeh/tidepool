import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import page, write, WAVE, WAVE_FLIP

def service_hero(icon, name, tagline, ages, colors_note):
    return f'''
<section class="hero" style="padding-bottom:0">
  <div class="wrap">
    <span class="eyebrow">{icon} {name}</span>
    <h1 class="mt-2" style="max-width:18ch">{tagline}</h1>
    <div class="hero-proof mt-2">
      <div><strong>{ages}</strong> typical age range</div>
      <div><strong>45–60 min</strong> session length</div>
      <div><strong>In-network</strong> with 9 plans</div>
    </div>
  </div>
</section>
{WAVE}'''

FAQ_BLOCK = '''
<details class="faq-item" data-reveal><summary>Do we need a referral? <span class="faq-caret">+</span></summary><div class="faq-body"><p>No. California gives families direct access to therapy evaluations. If your insurance plan requires a physician referral for reimbursement, we will tell you during the benefits check and help you get one quickly.</p></div></details>
<details class="faq-item" data-reveal><summary>How often will we come in? <span class="faq-caret">+</span></summary><div class="faq-body"><p>Most families start with one 45–60 minute session per week. Kids who need faster progress often do two. We re-check frequency at every twelve-week plan review rather than letting it drift.</p></div></details>
<details class="faq-item" data-reveal><summary>What do sessions actually look like? <span class="faq-caret">+</span></summary><div class="faq-body"><p>Play-based and purposeful. Your child will experience it as games, obstacles, and stories. You will experience it as a clinician who can name exactly which skill they were targeting and how you can practice it at home in five minutes a day.</p></div></details>
<details class="faq-item" data-reveal><summary>Can you work with my child's school? <span class="faq-caret">+</span></summary><div class="faq-body"><p>Yes. With your written OK we share goals and progress notes with teachers, join IEP meetings by request, and coach school staff on the same strategies we use in the clinic so the approach is consistent everywhere.</p></div></details>
<details class="faq-item" data-reveal><summary>What if my child refuses to participate? <span class="faq-caret">+</span></summary><div class="faq-body"><p>That is information, not failure. Early sessions may look like relationship-building: showing your child the room, the toys, and the person. We would rather spend two sessions earning trust than one session forcing compliance.</p></div></details>
'''

def service_body(name, intro, sections, who_for, evidence, team_link, faq_note=""):
    secs = ""
    for h, p in sections:
        secs += f'<div class="card" data-reveal><h3>{h}</h3><p>{p}</p></div>'
    whos = "".join(f'<li>{w}</li>' for w in who_for)
    ev = "".join(f'<li>{e}</li>' for e in evidence)
    return f'''
{intro}
<section class="section section-tint">
  <div class="wrap">
    <div class="section-head" data-reveal><span class="kicker">What a plan covers</span><h2>Inside {name.lower()} at Tidepool</h2></div>
    <div class="card-grid">{secs}</div>
  </div>
</section>
{WAVE_FLIP}
<section class="section">
  <div class="wrap two-col">
    <div data-reveal>
      <div class="section-head"><span class="kicker">Is this the right door?</span><h2>Who we typically see</h2></div>
      <ul class="check-list">{whos}</ul>
      <p class="mt-2" style="color:var(--ink-faint);font-size:var(--step--1)">Not sure your child fits these? The free consult exists exactly for that question. Twenty minutes, honest answer.</p>
    </div>
    <div data-reveal style="--reveal-i:1">
      <div class="card">
        <h3>Our evidence baseline</h3>
        <ul class="check-list mt-1">{ev}</ul>
        <p class="mt-2" style="font-size:0.92rem;color:var(--ink-soft)">We track each child's progress with the same measures every visit and show you the graph at every plan review. If the line is flat for twelve weeks, we change the plan, not the explanation.</p>
      </div>
      <p class="mt-3"><a class="btn btn-primary" href="/getting-started.html">Book the free consult <span class="btn-arrow">→</span></a></p>
      <p class="mt-2" style="font-size:0.95rem">Curious who you'd be working with? <a href="{team_link}">Meet the {name.lower()} team</a>.</p>
    </div>
  </div>
</section>
<section class="section section-tint">
  <div class="wrap narrow">
    <div class="section-head center" data-reveal><span class="kicker">Common questions</span><h2>{name} FAQ</h2></div>
    <div class="faq-list faq-group">{FAQ_BLOCK}{faq_note}</div>
  </div>
</section>
'''

# ---------------- SERVICES HUB ----------------
body = f'''
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Therapy services</span>
    <h1 class="mt-2">Four disciplines. One team. One hallway.</h1>
    <p class="lede">Kids rarely need exactly one thing. Our clinicians share a chart, a schedule, and a coffee maker, which means co-treating, warm handoffs, and a plan that fits the whole child instead of one symptom.</p>
  </div>
</section>
{WAVE}
<section class="section section-tint">
  <div class="wrap">
    <div class="card-grid">
      <a class="card" href="/speech-therapy.html" data-reveal><div class="card-icon">💬</div><h3>Speech &amp; language</h3><p>Articulation, late talkers, AAC, stuttering, social language. Led by two ASHA-certified SLPs and one SLP assistant.</p><span class="card-link">Speech therapy <span class="btn-arrow">→</span></span></a>
      <a class="card" href="/occupational-therapy.html" data-reveal style="--reveal-i:1"><div class="card-icon">✋</div><h3>Occupational therapy</h3><p>Sensory regulation, fine motor, handwriting, self-care routines. Led by two OTR/Ls with a certified sensory-integration practice.</p><span class="card-link">Occupational therapy <span class="btn-arrow">→</span></span></a>
      <a class="card" href="/feeding-therapy.html" data-reveal style="--reveal-i:2"><div class="card-icon">🥕</div><h3>Feeding therapy</h3><p>Picky eating, tube-to-table transitions, swallowing safety, mealtime routines. Our most-referred program in the county.</p><span class="card-link">Feeding therapy <span class="btn-arrow">→</span></span></a>
      <a class="card" href="/physical-therapy.html" data-reveal style="--reveal-i:0"><div class="card-icon">🦵</div><h3>Physical therapy</h3><p>Gross motor milestones, toe-walking, torticollis, balance, return to play after injury. Led by a board-certified pediatric clinical specialist.</p><span class="card-link">Physical therapy <span class="btn-arrow">→</span></span></a>
    </div>
  </div>
</section>
{WAVE_FLIP}
<section class="section">
  <div class="wrap two-col">
    <div data-reveal>
      <div class="section-head"><span class="kicker">Programs</span><h2>Group programs</h2>
      <p>Group sessions cost about a third of an individual session and add something one-on-one cannot: other kids.</p></div>
      <table class="rate-table">
        <thead><tr><th>Group</th><th>Who it's for</th><th>Format</th></tr></thead>
        <tbody>
          <tr><td><strong>Table Talk</strong></td><td>Social language, ages 7–10</td><td>6 weeks · 4 kids · Thu 4pm</td></tr>
          <tr><td><strong>Sensory Lab</strong></td><td>Regulation practice, ages 5–9</td><td>Ongoing · 5 kids · Tue 4pm</td></tr>
          <tr><td><strong>Food Explorers</strong></td><td>Picky eating, ages 4–8</td><td>8 weeks · 4 kids · Wed 4:30pm</td></tr>
          <tr><td><strong>Tiny Steps</strong></td><td>First-walkers and their grown-ups</td><td>Drop-in · Sat mornings</td></tr>
        </tbody>
      </table>
      <p class="rate-note">Group placement happens after an evaluation, so the first session is the right one, not a trial-and-error week.</p>
    </div>
    <div data-reveal style="--reveal-i:1">
      <div class="card">
        <h3>Co-treatment, explained</h3>
        <p>When a child's plan spans two disciplines (say, feeding therapy plus OT), both clinicians can be in the room together for one visit billed once. It is the most efficient hour in pediatric therapy, and it is nearly impossible to get from clinics where each discipline books separately.</p>
        <p class="mt-2">About a third of our active plans include some co-treatment time.</p>
      </div>
      <div class="card mt-2">
        <h3>Telehealth options</h3>
        <p>Parent-coaching sessions, progress check-ins, and consults work well by secure video. Hands-on skill work works best in person, and we will always say so when it does.</p>
      </div>
    </div>
  </div>
</section>
<section class="section section-sage">
  <div class="wrap center">
    <div class="statement" data-reveal>
      <h2>Not sure which door your child needs?</h2>
      <p>That is the most common question we get, and the free consult answers it. You talk; a clinician listens; we point you to the right evaluation or tell you to wait six months and re-check. Both are legitimate outcomes.</p>
      <a class="btn btn-primary" href="/getting-started.html">Book the free consult</a>
    </div>
  </div>
</section>
'''
write("services.html", page("services.html", "Therapy Services",
  "Speech, occupational, feeding, and physical therapy plus group programs at Tidepool Pediatric Therapy, Santa Cruz.",
  body))

# ---------------- SPEECH ----------------
body = service_body("Speech therapy",
  f'''{service_hero("💬", "Speech & language therapy", "From first words to fluent conversations.", "1–18", "")}
<section class="section"><div class="wrap"><div class="prose" data-reveal>
<p>Speech therapy at Tidepool covers everything a mouth and a mind do together: saying sounds clearly, understanding language, using it, and carrying it into friendships and classrooms. Our two speech-language pathologists are ASHA-certified and between them hold advanced training in AAC (augmentative and alternative communication), childhood apraxia of speech, and fluency.</p>
<p>We treat late talkers without panic and with a plan. The research is clear that some late talkers catch up alone; the problem is nobody can tell you in advance which ones. So we screen at twenty months rather than waiting for the "wait and see" deadline that keeps arriving and never actually arrives.</p>
</div></div></section>''',
  [
    ("Articulation &amp; phonology", "Speech-sound disorders from a single tricky R to patterns that make a child 40% intelligible to strangers. We use the cycles approach and traditional drill where the evidence supports each."),
    ("Late talking &amp; language delay", "Vocabulary growth, word combinations, and understanding directions. Progress is measured in words gained per week, tracked on a graph you will actually see."),
    ("AAC &amp; complex communication", "Trial, fitting, and coaching for robust AAC systems. An AAC device is never a last resort or a replacement for speech; the evidence says it grows speech."),
    ("Stuttering &amp; fluency", "Family-centered fluency therapy that balances speech tools with confidence, because a child who is afraid to talk works against every technique we teach."),
    ("Social language groups", "Table Talk, our six-week social group, practices conversation repair, flexible thinking, and joining play with three other kids and one SLP."),
    ("School-readiness language", "Pre-literacy foundations: phonological awareness, narrative skills, and vocabulary depth that predict reading success."),
  ],
  [
    "Your 18-month-old says fewer than ten words",
    "Strangers cannot understand your four-year-old's speech",
    "Your child stutters and has started avoiding talking situations",
    "Teachers report your child 'loses' multi-step directions",
    "Your child's thoughts are clearly ahead of their words",
    "An AAC device has been suggested and you don't know where to start",
  ],
  [
    "Cycles approach for phonological patterns, per peer-reviewed outcomes studies",
    "Naturalistic language intervention in play routines, not flashcard drills",
    "AAC access modeling: the device is modeled for the child, never demanded of them",
    " Palin-parent-based fluency principles adapted for our caseload ages",
  ],
  "/team.html")

write("speech-therapy.html", page("speech-therapy.html", "Speech & Language Therapy",
  "Speech and language therapy in Santa Cruz for late talkers, articulation, AAC, and stuttering. ASHA-certified clinicians.",
  body))
