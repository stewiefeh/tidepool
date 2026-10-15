import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import page, write, WAVE, WAVE_FLIP

# ---------------- RESOURCES ----------------
body = f'''
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Family resources</span>
    <h1 class="mt-2">The stuff we wish every waiting-room pamphlet said.</h1>
    <p class="lede">Straight answers on milestones, insurance rights, screen-time debates, and the local services that actually return phone calls. Written by our clinicians, no industry jargon, no fear.</p>
  </div>
</section>
{WAVE}
<section class="section section-tint">
  <div class="wrap">
    <div class="post-grid">
      <a class="post-card" href="/resource-milestones.html" data-reveal>
        <div class="post-band"></div>
        <div class="post-body">
          <span class="post-meta">Guide · 12 min read</span>
          <h3>Milestones without the panic</h3>
          <p>What the CDC milestones actually mean, why "not yet" and "never" are different sentences, and the red flags that genuinely warrant an early call.</p>
        </div>
      </a>
      <a class="post-card" href="/resource-insurance-rights.html" data-reveal style="--reveal-i:1">
        <div class="post-band"></div>
        <div class="post-body">
          <span class="post-meta">Guide · 9 min read</span>
          <h3>Your insurance rights, in plain English</h3>
          <p>What California law requires plans to cover for pediatric therapy, how denial appeals actually work, and the one phrase that un-sticks most claims.</p>
        </div>
      </a>
      <a class="post-card" href="/resource-first-words.html" data-reveal style="--reveal-i:2">
        <div class="post-band"></div>
        <div class="post-body">
          <span class="post-meta">Guide · 7 min read</span>
          <h3>Late talkers: the honest version</h3>
          <p>Some late talkers catch up alone. Nobody can predict which. Here's what screening at 20 months buys you, and what "wait and see" actually costs.</p>
        </div>
      </a>
    </div>
  </div>
</section>
{WAVE_FLIP}
<section class="section">
  <div class="wrap two-col">
    <div data-reveal>
      <div class="section-head"><span class="kicker">Local map</span><h2>Santa Cruz County services that return calls</h2></div>
      <div class="prose">
        <ul>
          <li><strong>San Andreas Regional Center</strong> — Early Start intake for children under three. Assessment in about three weeks, and it is free regardless of income or immigration status.</li>
          <li><strong>First 5 Santa Cruz</strong> — free developmental screening events monthly; ask for the "Ages &amp; Stages" clinic.</li>
          <li><strong>SCUSD special education intake</strong> — if your child is three or older, request an assessment in writing; the district has 60 days to respond by law.</li>
          <li><strong>Parents' place (family resource center)</strong> — parent-to-parent matching, Wednesday drop-ins, and the best playground gossip network in the county.</li>
        </ul>
      </div>
    </div>
    <div data-reveal style="--reveal-i:1">
      <div class="card">
        <h3>Our lending library</h3>
        <p>Twenty AAC devices, sensory kits, feeding chairs, and about two hundred books in the lobby, free to borrow for any family in the county, client or not. Ask at the front desk; there is no paperwork gauntlet and no late fee.</p>
      </div>
      <div class="card mt-2">
        <h3>Waiting is hard. Two weeks is not nothing, but it is not forever.</h3>
        <p>If you are on any clinic's waitlist right now: request the screening consult anyway. It is usually free, it usually happens faster than the evaluation queue, and it usually moves your place in line.</p>
      </div>
    </div>
  </div>
</section>
'''
write("resources.html", page("resources.html", "Family Resources",
  "Plain-English guides on milestones, insurance rights, and late talking, plus Santa Cruz County services and our free lending library.",
  body))

# ---------------- RESOURCE GUIDES ----------------
def guide(slug, title, desc, sections):
    secs = ""
    for h, ps in sections:
        body_html = "".join(f"<p>{p}</p>" for p in ps)
        secs += f"<h2>{h}</h2>{body_html}"
    b = f'''
<section class="hero"><div class="wrap narrow">
  <span class="eyebrow">Family resource</span>
  <h1 class="mt-2">{title}</h1>
  <p class="lede">{desc}</p>
</div></section>
{WAVE}
<section class="section section-tint"><div class="wrap"><div class="prose">{secs}</div></div></section>
<section class="section"><div class="wrap narrow center">
  <div class="statement" data-reveal>
    <h2>Reading is a good start. A consult is faster.</h2>
    <p>Every guide here is written to help you decide, not to sell you therapy. If after reading you want twenty honest minutes, the consult is free and a clinician answers.</p>
    <a class="btn btn-primary" href="/getting-started.html">Book the free consult</a>
  </div>
</div></section>
'''
    write(slug, page(slug, title, desc, b))

guide("resource-milestones.html", "Milestones without the panic",
  "What CDC milestones mean, what 'not yet' really means, and which red flags deserve an early call.",
  [
    ("The checklist is a floor, not a leaderboard",
     ["The CDC's checklist describes what most children do by a given age, not what yours must do by it. A child who rolls at seven months rather than six is on schedule. A child who is not rolling at nine is a sentence worth a phone call.",
      "What trips families up is treating the checklist as a race with a single winner. Children develop in bursts and plateaus, and the pattern matters more than any single month."]),
    ("Not yet vs. never",
     ["'Not yet' means the skill is late but arriving: your child is moving toward it, with or without prodding. 'Never' means the skill is not emerging at all: no attempts, no approximations, no progress over two months.",
      "The second one is the phone-call case. The first one is a conversation case. We have twenty free minutes for either, and we will tell you which it looks like."]),
    ("The five flags that deserve an early call",
     ["<ul><li>No babbling by nine months, or babbling that stopped</li><li>No pointing, waving, or other gestures by twelve months</li><li>Loss of words or skills at any age, ever</li><li>Not walking by eighteen months, or walking that appeared and vanished</li><li>A parent's gut that something is off, which research keeps validating at surprising rates</li></ul>",
      "Loss of skills is the one we will always prioritize. It is the rarest item on this list and the one that warrants a pediatrician conversation the same week."]),
    ("What a screen buys you",
     ["A twenty-minute screen with a pediatric clinician answers one of three ways: you're in the normal range, let's watch this specific thing together for eight weeks, or let's evaluate properly now. All three are useful answers, and none of them cost you anything but time."]),
  ])

guide("resource-insurance-rights.html", "Your insurance rights, in plain English",
  "What California law requires for pediatric therapy coverage, how appeals work, and the phrase that un-sticks claims.",
  [
    ("The short version",
     ["If your plan covers pediatric therapy at all, California's mental health and habilitative-services rules require it to cover medically necessary speech, OT, and PT for children, and to treat it the same way it treats any other medical specialty. 'Medical necessity' is determined by your treating clinician's documentation, not by the insurance company's preference for group over individual sessions.",
      "The part most families don't know: you can request the clinical criteria your plan uses, in writing, and they must provide it. Vague denials become much harder to write once the criteria are on record."]),
    ("The phrase that un-sticks claims",
     ["When a denial says 'not medically necessary,' the most effective appeal letter we've seen is one paragraph: a short description of the functional limitation in the child's own daily life, the clinician's recommendation, and the sentence 'Please provide the written medical-necessity criteria used for this determination.'",
      "It works because it forces the plan to either specify a criterion the care clearly meets or escalate the review. About half of first-level denials in our experience reverse at this stage."]),
    ("When to call for help",
     ["If a second-level appeal fails, the California Department of Managed Health Care runs a free Help Center that resolves plan disputes, and it has actual enforcement power. Every family we've sent there came back with an answer, usually within a month.",
      "Our office will draft the appeal letter with you, free, whether or not your child is our patient. Ask for Wren."]),
  ])

guide("resource-first-words.html", "Late talkers: the honest version",
  "What the research actually says about late talking, what screening buys you, and what 'wait and see' costs.",
  [
    ("The honest starting point",
     ["About 15% of toddlers are late talkers, and roughly half of them catch up without any therapy at all. That is the fact everyone quotes. The part usually left out: there is currently no way to tell, at twenty months, which half your child is in.",
      "The best-available predictors (comprehension, gestures, family history, the shape of the word attempts) are probabilistic, not diagnostic. A screen with a clinician weighs them in minutes; a forum thread weighs them in months."]),
    ("What 'wait and see' costs",
     ["For the child who would catch up anyway: mostly nothing, plus some anxiety. For the child who wouldn't: the most plastic language-learning months of their life, spent on a waiting list that keeps saying 'come back in six months.'",
      "The reason we screen at twenty months instead of thirty is not that every late talker needs therapy. It is that the screening itself is cheap, free here, and replaces the guesswork with a plan either way."]),
    ("What actually helps at home",
     ["The boring, evidence-backed version: talk during what the child is already looking at, use short grammatical sentences, expand what they say by one word, and read the same book twelve more times than feels reasonable. No flashcards, no educational apps, no subscription box.",
      "If someone sells you a program that promises to cure late talking, walk out. Language grows in relationship, and the only product that matters is the attention you already own."]),
  ])
