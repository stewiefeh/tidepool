import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import page, write, WAVE, WAVE_FLIP

# ---------------- ABOUT ----------------
body = f'''
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">About the clinic</span>
    <h1 class="mt-2">Built around the wait, not the waitlist.</h1>
    <p class="lede">Tidepool opened in 2016 because our founder, Marisol Vance, was tired of telling worried parents "four to six months." Everything about the clinic, the caseload caps, the shared chart, the kitchen suite, traces back to that one sentence she kept saying.</p>
  </div>
</section>
{WAVE}
<section class="section section-tint">
  <div class="wrap two-col">
    <div class="prose" data-reveal>
      <h2>The caseload math</h2>
      <p>The industry norm for a pediatric therapist is a caseload of 60 to 80 children. Our cap is two-thirds of that: 40 to 53. It costs us revenue every month and buys us three things: clinicians who stay (zero turnover in three years), sessions that start on time, and the two-week wait.</p>
      <p>When a discipline fills up, we say so on this site and on the phone. We hire ahead of demand rather than rationing access to it. Speech is currently our fullest schedule; PT usually has room within days.</p>
      <h2>One chart, really one</h2>
      <p>Most "multidisciplinary" clinics run four schedules in four systems and a phone tree between them. Ours runs one. When your child's SLP notices a sensory regulation pattern mid-session, your OT sees the note the same afternoon, not after the next case conference.</p>
      <h2>The kitchen suite</h2>
      <p>Our feeding program's best tool is a working kitchen with a family table. Real meals, real siblings when they come along, real cleanup. Therapy that only survives in a clinic room isn't therapy; it's performance.</p>
    </div>
    <div data-reveal style="--reveal-i:1">
      <div class="card">
        <h3>The harbor, room by room</h3>
        <ul class="check-list mt-1">
          <li>The sensory gym: rock wall, two swings, mats rated for exactly the crashes kids attempt</li>
          <li>Two fine-motor studios with adjustable-height tables for wheelchair users</li>
          <li>The regulation room: dimmed lights, soft floor, zero demands until the child is ready</li>
          <li>The kitchen suite for feeding therapy and real family meals</li>
          <li>Four treatment rooms, one observation window each, coffee for parents</li>
        </ul>
      </div>
      <div class="card mt-2">
        <h3>By the numbers</h3>
        <ul class="check-list mt-1">
          <li>Founded 2016, locally owned, no private equity</li>
          <li>1,240+ evaluations completed since opening</li>
          <li>96% of families return or graduate from care</li>
          <li>11-day median wait to first visit, county-wide median: 19 weeks</li>
        </ul>
      </div>
    </div>
  </div>
</section>
{WAVE_FLIP}
<section class="section">
  <div class="wrap">
    <div class="statement" data-reveal>
      <h2>Our promise, on the record</h2>
      <p>We will tell you honestly when your child needs therapy and honestly when they don't. We will never hold a spot hostage to urgency you don't feel. We will show you the progress graph, not just describe it. And we will work toward your child not needing us, because that is the only ending worth billing for.</p>
      <a class="btn btn-primary" href="/getting-started.html">Take the first step</a>
    </div>
  </div>
</section>
'''
write("about.html", page("about.html", "About",
  "Tidepool Pediatric Therapy: locally owned since 2016, caseload caps, one shared chart, and a two-week wait in Santa Cruz.",
  body))

# ---------------- GETTING STARTED ----------------
body = f'''
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Getting started</span>
    <h1 class="mt-2">Twenty minutes to an honest answer.</h1>
    <p class="lede">The free consult is a call with a clinician, not a sales script. It exists to answer the question every parent arrives with: does my child actually need this?</p>
  </div>
</section>
{WAVE}
<section class="section">
  <div class="wrap two-col">
    <div data-reveal>
      <div class="form-card">
        <h2>Request your free consult</h2>
        <p style="color:var(--ink-soft)" class="mt-1">Demo form: this site is a portfolio piece, so nothing is transmitted anywhere and no personal data is stored.</p>
        <form class="form-grid mt-2" data-demo>
          <div><label for="gs-name">Your name</label><input id="gs-name" type="text" required autocomplete="name"></div>
          <div><label for="gs-child">Child's first name &amp; age</label><input id="gs-child" type="text" placeholder="e.g. Leo, 3"></div>
          <div><label for="gs-email">Email</label><input id="gs-email" type="email" required autocomplete="email"></div>
          <div><label for="gs-phone">Phone</label><input id="gs-phone" type="tel" autocomplete="tel"></div>
          <div class="full"><label for="gs-area">What area concerns you most?</label>
            <select id="gs-area"><option>Speech &amp; language</option><option>Occupational therapy / sensory</option><option>Feeding &amp; mealtimes</option><option>Physical therapy / movement</option><option>Not sure yet, that's the point of the consult</option></select></div>
          <div class="full"><label for="gs-notes">Tell us what you're seeing</label><textarea id="gs-notes" placeholder="A few sentences is plenty. What happens, how often, and what you've already tried."></textarea></div>
          <div class="full"><button class="btn btn-primary" type="submit">Request consult <span class="btn-arrow">→</span></button>
          <p class="form-note">We reply within one business day, usually the same afternoon.</p></div>
        </form>
      </div>
    </div>
    <div data-reveal style="--reveal-i:1">
      <div class="section-head"><span class="kicker">What happens next</span><h2>The four steps</h2></div>
      <div class="pathway" style="grid-template-columns:1fr">
        <div class="path-step"><h3>Free consult (20 min)</h3><p>Phone or video, your choice. A clinician listens and gives you an honest read.</p></div>
        <div class="path-step"><h3>Benefits check (same day)</h3><p>We call your insurance while you wait and tell you exactly what evaluation and sessions would cost you.</p></div>
        <div class="path-step"><h3>Evaluation (60 min)</h3><p>Play-based, standardized where it counts. Written report within five business days.</p></div>
        <div class="path-step"><h3>First therapy week</h3><p>Usually within eleven days of the evaluation. Same clinician every visit from here on.</p></div>
      </div>
    </div>
  </div>
</section>
<section class="section section-tint">
  <div class="wrap narrow">
    <div class="section-head" data-reveal><span class="kicker">Before you call anyone</span><h2>Questions worth asking any clinic</h2></div>
    <div class="prose" data-reveal>
      <p>Even if you don't choose us, ask these:</p>
      <ul>
        <li>What is the actual wait for a first evaluation, in weeks?</li>
        <li>Will my child see the same clinician every visit? What happens when they leave?</li>
        <li>How many children are on my therapist's caseload?</li>
        <li>Do you share notes across disciplines, and how fast?</li>
        <li>What does my family pay after insurance, in dollars, for evaluation and for each session?</li>
      </ul>
      <p>Any clinic that answers all five in specific numbers is a reasonable choice. The ones that don't have a reason.</p>
    </div>
  </div>
</section>
'''
write("getting-started.html", page("getting-started.html", "Getting Started",
  "Book a free 20-minute consult with a Tidepool clinician. Four steps from first call to first therapy week, with a benefits check the same day.",
  body))

# ---------------- FAQ ----------------
body = f'''
<section class="hero">
  <div class="wrap narrow">
    <span class="eyebrow">FAQ</span>
    <h1 class="mt-2">Questions parents actually ask.</h1>
    <p class="lede">Grouped by what's on your mind. If your question isn't here, <a href="/contact.html">ask us directly</a>; the answer becomes a new entry.</p>
  </div>
</section>
{WAVE}
<section class="section section-tint">
  <div class="wrap narrow">
    <h2 class="mt-2" data-reveal>The process</h2>
    <div class="faq-list faq-group mt-2">
      <details class="faq-item"><summary>Do we need a pediatrician referral? <span class="faq-caret">+</span></summary><div class="faq-body"><p>No. California is a direct-access state for therapy evaluations. Some insurance plans do require a physician referral for reimbursement; our benefits check tells you before anything is scheduled, and we help you get the paperwork moving the same week.</p></div></details>
      <details class="faq-item"><summary>How fast can we start? <span class="faq-caret">+</span></summary><div class="faq-body"><p>Median wait from first call to first visit is eleven days. Speech runs fullest (two weeks is common there); PT often has room within days. If a discipline is full, we tell you the real number and hold nothing hostage.</p></div></details>
      <details class="faq-item"><summary>What happens at the evaluation? <span class="faq-caret">+</span></summary><div class="faq-body"><p>A 60-minute play-based session with standardized measures where they matter. Parents stay in the room. You leave with our initial read the same day and a written report within five business days.</p></div></details>
      <details class="faq-item"><summary>Will my child always see the same therapist? <span class="faq-caret">+</span></summary><div class="faq-body"><p>Yes, by design. Rapport is the first intervention. Our clinician turnover in the last three years is zero, and if that ever changes mid-plan, you get two weeks of overlapping handoff sessions, not a surprise phone call.</p></div></details>
    </div>
    <h2 class="mt-4" data-reveal>Money &amp; insurance</h2>
    <div class="faq-list faq-group mt-2">
      <details class="faq-item"><summary>Do you take my insurance? <span class="faq-caret">+</span></summary><div class="faq-body"><p>We're in-network with nine plans (full list on the <a href="/insurance.html">insurance page</a>). Out of network, we provide a superbill you can submit for reimbursement, and we'll tell you honestly what the likely recovery rate is before you spend a dollar.</p></div></details>
      <details class="faq-item"><summary>What will this actually cost us? <span class="faq-caret">+</span></summary><div class="faq-body"><p>After the benefits check you get a written estimate: evaluation cost, per-session cost, and your expected annual total at the recommended frequency. No surprise line items. The full rate table is public on the insurance page.</p></div></details>
      <details class="faq-item"><summary>Do you offer a sliding scale? <span class="faq-caret">+</span></summary><div class="faq-body"><p>Yes. Four reduced-rate slots are reserved at all times, no documentation gauntlet, first-come. Ask for it by name; nobody here will make you justify your finances.</p></div></details>
    </div>
    <h2 class="mt-4" data-reveal>Therapy itself</h2>
    <div class="faq-list faq-group mt-2">
      <details class="faq-item"><summary>How long until we see progress? <span class="faq-caret">+</span></summary><div class="faq-body"><p>Plan reviews happen every twelve weeks with the progress graph on the table. Many families see meaningful change inside eight, but we won't promise a timeline we don't control. What we control is measurement: if the line is flat, the plan changes.</p></div></details>
      <details class="faq-item"><summary>Can I watch sessions? <span class="faq-caret">+</span></summary><div class="faq-body"><p>Not just can: should. Every room has an observation window, and every plan includes structured parent coaching. A therapy model that hides the method from the family can't work at home, so we don't use it.</p></div></details>
      <details class="faq-item"><summary>My child has a diagnosis. Does that change anything? <span class="faq-caret">+</span></summary><div class="faq-body"><p>It shapes the plan, not the welcome. We work with autistic children, kids with Down syndrome, cerebral palsy, prematurity histories, and every undiagnosed worry that brings a family through the door. The evaluation tells us where to start; the child tells us the rest.</p></div></details>
      <details class="faq-item"><summary>What ages do you serve? <span class="faq-caret">+</span></summary><div class="faq-body"><p>Birth through eighteen, including Early Start referrals for infants and toddlers. Our youngest clients come in for milestone checks; our oldest for return-to-play programs after injuries.</p></div></details>
    </div>
  </div>
</section>
'''
write("faq.html", page("faq.html", "FAQ",
  "Frequently asked questions about therapy at Tidepool Pediatric Therapy: referrals, wait times, insurance, costs, and what sessions look like.",
  body))
