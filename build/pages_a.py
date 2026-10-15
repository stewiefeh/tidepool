import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import page, write, WAVE, WAVE_FLIP

# ---------------- INDEX ----------------
body = f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">A calm harbor for growing kids</span>
      <h1 class="mt-2">Therapy that moves at <span class="wave-word">your child's</span> pace.</h1>
      <p class="lede">Speech, occupational, feeding, and physical therapy for kids from birth through eighteen. Small clinic, six clinicians, and the shortest wait for a first visit in Santa Cruz County: two weeks or less.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="/getting-started.html">Book a free consult <span class="btn-arrow">→</span></a>
        <a class="btn btn-ghost" href="/services.html">Explore therapies</a>
      </div>
      <div class="hero-proof">
        <div><strong>6</strong> clinicians, all pediatric</div>
        <div><strong>≤2 wks</strong> to first visit</div>
        <div><strong>4–18</strong> ages we serve (plus Early Start)</div>
        <div><strong>2016</strong> est., locally owned</div>
      </div>
    </div>
    <div class="tidepool-scene" aria-hidden="true">
      <div class="pool-ring breath"></div>
      <div class="ring-2"></div>
      <div class="critter critter-1" data-drift>🦀</div>
      <div class="critter critter-2" data-drift>🐙</div>
      <div class="critter critter-3" data-drift>🐚</div>
      <div class="critter critter-4" data-drift>⭐</div>
    </div>
  </div>
</section>
{WAVE}
<section class="section section-tint">
  <div class="wrap">
    <div class="section-head center" data-reveal>
      <span class="kicker">Four therapies, one team</span>
      <h2>What we treat, and how we treat it</h2>
      <p>Every discipline shares one hallway, one chart, and one plan. If your child needs speech and occupational therapy, you will not be driving to two offices or repeating your story twice.</p>
    </div>
    <div class="card-grid">
      <a class="card" href="/speech-therapy.html" data-reveal style="--reveal-i:0">
        <div class="card-icon">💬</div>
        <h3>Speech &amp; language</h3>
        <p>First words to fluent conversations: articulation, late talkers, AAC devices, stuttering, and social language groups.</p>
        <span class="card-link">Speech therapy <span class="btn-arrow">→</span></span>
      </a>
      <a class="card" href="/occupational-therapy.html" data-reveal style="--reveal-i:1">
        <div class="card-icon">✋</div>
        <h3>Occupational therapy</h3>
        <p>Sensory regulation, fine motor skills, handwriting, dressing, and the everyday routines that make school mornings survivable.</p>
        <span class="card-link">Occupational therapy <span class="btn-arrow">→</span></span>
      </a>
      <a class="card" href="/feeding-therapy.html" data-reveal style="--reveal-i:2">
        <div class="card-icon">🥕</div>
        <h3>Feeding therapy</h3>
        <p>Picky eating, tube-to-table transitions, swallowing safety, and mealtimes that stop being a battleground.</p>
        <span class="card-link">Feeding therapy <span class="btn-arrow">→</span></span>
      </a>
      <a class="card" href="/physical-therapy.html" data-reveal style="--reveal-i:0">
        <div class="card-icon">🦵</div>
        <h3>Physical therapy</h3>
        <p>Crawling to coordination: gross motor milestones, toe-walking, torticollis, balance, and post-injury return to play.</p>
        <span class="card-link">Physical therapy <span class="btn-arrow">→</span></span>
      </a>
    </div>
  </div>
</section>
{WAVE_FLIP}
<section class="section">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="kicker">Getting started</span>
      <h2>Four steps from "I'm worried" to a plan</h2>
      <p>No referral required for a screening. No eleven-page intake packet before we ever meet you. Here is exactly how it works.</p>
    </div>
    <div class="pathway">
      <div class="path-step" data-reveal style="--reveal-i:0">
        <h3>Free 20-minute consult</h3>
        <p>A phone or video call with a clinician, not a call center. You describe what you're seeing; we tell you honestly whether an evaluation is needed.</p>
      </div>
      <div class="path-step" data-reveal style="--reveal-i:1">
        <h3>Evaluation visit</h3>
        <p>A 60-minute play-based session. We use standardized measures where they matter and observation everywhere else. You get a written report within five business days.</p>
      </div>
      <div class="path-step" data-reveal style="--reveal-i:2">
        <h3>Your child's plan</h3>
        <p>Goals written with you, not for you. Frequency, duration, and what progress looks like in four weeks, in plain language.</p>
      </div>
      <div class="path-step" data-reveal style="--reveal-i:3">
        <h3>Therapy, then transition</h3>
        <p>Weekly or twice-weekly sessions, re-checked every twelve weeks. The end goal is always the same: your child not needing us.</p>
      </div>
    </div>
    <p class="center mt-4"><a class="btn btn-primary" href="/getting-started.html">Start with step one</a></p>
  </div>
</section>
<section class="section section-sage">
  <div class="wrap">
    <div class="statement" data-reveal>
      <h2>We believe the waiting list is part of the problem.</h2>
      <p>The average wait for pediatric therapy in our county is four to seven months. Ours is two weeks. We hold clinician caseloads at two-thirds of industry norms, hire ahead of demand, and would rather say "our speech team is full, here's exactly when we can start" than park your child on a list and hope you forget about it.</p>
      <a class="btn btn-primary" href="/about.html">Read about our model</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="stat-band" data-reveal>
      <div class="stat-cell"><strong>1,240+</strong><span>evaluations since 2016</span></div>
      <div class="stat-cell"><strong>96%</strong><span>families returning or graduating care</span></div>
      <div class="stat-cell"><strong>11 days</strong><span>median wait to first visit</span></div>
      <div class="stat-cell"><strong>2/3</strong><span>standard caseload, per clinician</span></div>
    </div>
  </div>
</section>
<section class="section section-tint">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="kicker">Voices from the harbor</span>
      <h2>What families tell us</h2>
    </div>
    <div class="card-grid">
      <figure class="card" data-reveal style="--reveal-i:0">
        <p>"Our son went from three words at twenty months to telling his little sister to 'stop it, please' eight months later. The word 'please' nearly took longer than everything else."</p>
        <figcaption class="mt-2 chip chip-coral">Dana R., speech therapy parent</figcaption>
      </figure>
      <figure class="card" data-reveal style="--reveal-i:1">
        <p>"They explained the sensory plan to my mother-in-law in a way that ended the 'he just needs discipline' argument at Thanksgiving. Worth every copay for that alone."</p>
        <figcaption class="mt-2 chip chip-sage">Marcus T., OT parent</figcaption>
      </figure>
      <figure class="card" data-reveal style="--reveal-i:2">
        <p>"Meals used to take ninety minutes and end in tears, mine and hers. Six months of feeding therapy later, dinner is dinner. I still don't fully believe it."</p>
        <figcaption class="mt-2 chip">Priya S., feeding therapy parent</figcaption>
      </figure>
    </div>
  </div>
</section>
'''
write("index.html", page("index.html", "Pediatric therapy in Santa Cruz",
  "Speech, occupational, feeding, and physical therapy for kids birth to 18 in Santa Cruz, CA. First visit within two weeks. Free 20-minute consult.",
  body))
