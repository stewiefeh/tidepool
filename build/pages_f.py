import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import page, write, WAVE, WAVE_FLIP

# ---------------- INSURANCE ----------------
body = f'''
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Insurance &amp; rates</span>
    <h1 class="mt-2">Real numbers, before you spend a dollar.</h1>
    <p class="lede">We call your insurance while you wait and put the estimate in writing. The full rate table is public, because a family deciding about their child's therapy deserves to see the price before the phone call, not after.</p>
  </div>
</section>
{WAVE}
<section class="section">
  <div class="wrap two-col">
    <div data-reveal>
      <div class="section-head"><span class="kicker">In-network plans</span><h2>We're in-network with nine plans</h2></div>
      <table class="rate-table">
        <thead><tr><th>Plan type</th><th>Evaluation</th><th>Session</th><th>Your typical copay</th></tr></thead>
        <tbody>
          <tr><td>Anthem Blue Cross PPO</td><td class="num">$220</td><td class="num">$145</td><td class="num">$25–45</td></tr>
          <tr><td>Blue Shield PPO</td><td class="num">$220</td><td class="num">$145</td><td class="num">$25–45</td></tr>
          <tr><td>Cigna PPO</td><td class="num">$220</td><td class="num">$145</td><td class="num">$30–50</td></tr>
          <tr><td>Aetna PPO</td><td class="num">$220</td><td class="num">$145</td><td class="num">$25–45</td></tr>
          <tr><td>United Healthcare PPO</td><td class="num">$220</td><td class="num">$145</td><td class="num">$30–50</td></tr>
          <tr><td>Central Health Plan (Medi-Cal)</td><td class="num">$0</td><td class="num">$0</td><td class="num">$0</td></tr>
        </tbody>
      </table>
      <p class="rate-note">Rates shown are our contracted fees, not list prices. Copays vary by specific plan tier; the benefits check resolves yours to the dollar before anything is scheduled. We also accept HSA and FSA cards.</p>
      <div class="card mt-3">
        <h3>Out of network</h3>
        <p>We provide itemized superbills for any PPO plan. Before you commit, we will tell you our honest estimate of what your specific plan is likely to reimburse, based on the last dozen families who submitted to it. If the answer is "not much," we say so and talk about the self-pay path instead.</p>
      </div>
    </div>
    <div data-reveal style="--reveal-i:1">
      <div class="section-head"><span class="kicker">Self-pay</span><h2>Published self-pay rates</h2></div>
      <table class="rate-table">
        <thead><tr><th>Service</th><th>Rate</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>Screening consult (20 min)</td><td class="num">$0</td><td>Always free</td></tr>
          <tr><td>Full evaluation</td><td class="num">$325</td><td>Written report included</td></tr>
          <tr><td>Individual session (45 min)</td><td class="num">$165</td><td>Speech / OT / PT</td></tr>
          <tr><td>Feeding session (60 min)</td><td class="num">$195</td><td>SLP + OT co-treatment</td></tr>
          <tr><td>Group session</td><td class="num">$55</td><td>Per session, 4–6 week blocks</td></tr>
          <tr><td>Parent coaching add-on</td><td class="num">$0</td><td>Included in every plan</td></tr>
        </tbody>
      </table>
      <div class="card mt-3">
        <h3>The sliding scale</h3>
        <p>Four reduced-rate slots are reserved at all times, first-come, no documentation gauntlet. Ask for it by name at the consult. Nobody here will make you justify your finances to get your child seen.</p>
      </div>
      <div class="card mt-2">
        <h3>What we don't do</h3>
        <p>We don't run credit checks, don't charge no-show fees for cancellations made more than four hours ahead, and don't auto-charge a card on file. If a family's card declines, Wren calls and works out a plan before a session is ever cancelled over it.</p>
      </div>
    </div>
  </div>
</section>
<section class="section section-tint">
  <div class="wrap narrow center">
    <div class="statement" data-reveal>
      <h2>The benefits check is free and happens before anything is scheduled.</h2>
      <p>Give Wren your member ID and ten minutes. You get back: whether we're in-network for you, your exact copays, any visit limits your plan applies, and what the out-of-network route would look like if we're not. In writing. Then you decide.</p>
      <a class="btn btn-primary" href="/getting-started.html">Start the benefits check</a>
    </div>
  </div>
</section>
'''
write("insurance.html", page("insurance.html", "Insurance & Rates",
  "Public rate table and insurance information for Tidepool Pediatric Therapy: nine in-network plans, self-pay rates, sliding scale.",
  body))

# ---------------- CONTACT ----------------
body = f'''
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h1 class="mt-2">Come find the harbor.</h1>
    <p class="lede">412 Harbor Lane, Santa Cruz, CA 95060. Two blocks from the wharf, parking in the lot behind the building, stroller ramp at the side door.</p>
    <div class="hero-proof mt-2">
      <div><strong>(831) 555-0142</strong>&nbsp;Mon–Fri 8–6, Sat 9–1</div>
      <div><strong>hello@tidepoolcare.example</strong>&nbsp;replies within one business day</div>
      <div><strong>Wheelchair</strong>&nbsp;accessible throughout</div>
    </div>
  </div>
</section>
{WAVE}
<section class="section">
  <div class="wrap two-col">
    <div data-reveal>
      <div class="form-card">
        <h2>Send us a note</h2>
        <p style="color:var(--ink-soft)" class="mt-1">Demo form: nothing is transmitted and nothing is stored.</p>
        <form class="form-grid mt-2" data-demo>
          <div><label for="c-name">Your name</label><input id="c-name" type="text" required></div>
          <div><label for="c-email">Email</label><input id="c-email" type="email" required></div>
          <div class="full"><label for="c-topic">Topic</label>
            <select id="c-topic"><option>Booking a consult</option><option>Insurance question</option><option>Careers</option><option>Something else</option></select></div>
          <div class="full"><label for="c-msg">Message</label><textarea id="c-msg" required></textarea></div>
          <div class="full"><button class="btn btn-primary" type="submit">Send <span class="btn-arrow">→</span></button></div>
        </form>
      </div>
    </div>
    <div data-reveal style="--reveal-i:1">
      <div class="card">
        <h3>Hours</h3>
        <table class="rate-table mt-1">
          <tbody>
            <tr><td>Monday – Thursday</td><td class="num">8:00 – 6:00</td></tr>
            <tr><td>Friday</td><td class="num">8:00 – 5:00</td></tr>
            <tr><td>Saturday</td><td class="num">9:00 – 1:00</td></tr>
            <tr><td>Sunday</td><td class="num">Closed</td></tr>
          </tbody>
        </table>
        <p class="rate-note">Early-morning and after-school slots go fastest; they open about six weeks out.</p>
      </div>
      <div class="card mt-2">
        <h3>Finding us</h3>
        <p><strong>Driving:</strong> Beach Street to Harbor Lane; the lot behind our building has eleven spaces and four are wide stalls.</p>
        <p class="mt-1"><strong>Bus:</strong> Route 19 stops at Harbor &amp; 2nd, a two-minute walk.</p>
        <p class="mt-1"><strong>Strollers &amp; wheelchairs:</strong> side-door ramp off the parking lot; all rooms and restrooms are accessible.</p>
      </div>
    </div>
  </div>
</section>
'''
write("contact.html", page("contact.html", "Contact & Directions",
  "Contact Tidepool Pediatric Therapy: 412 Harbor Lane, Santa Cruz. Hours, directions, parking, and a demo contact form.",
  body))

# ---------------- CAREERS ----------------
body = f'''
<section class="hero">
  <div class="wrap narrow">
    <span class="eyebrow">Careers</span>
    <h1 class="mt-2">The caseload cap is the job description.</h1>
    <p class="lede">We cap caseloads at two-thirds of industry norms, pay above market, and bill for forty-five minutes of your attention, not your evenings. Zero turnover in three years is the proof, not the promise.</p>
  </div>
</section>
{WAVE}
<section class="section section-tint">
  <div class="wrap two-col">
    <div class="prose" data-reveal>
      <h2>What working here is like</h2>
      <ul class="check-list mt-2">
        <li>Caseload of 40–53 active kids, never 70+</li>
        <li>Admin time is scheduled and paid, not squeezed into lunch</li>
        <li>One shared chart across disciplines; no re-entering your own notes into three systems</li>
        <li>Annual CEU budget that actually covers conference travel every other year</li>
        <li>Supervision and mentorship hours on the clock for CFs and new grads</li>
        <li>Four-day week option at 0.8 FTE with benefits</li>
      </ul>
      <p class="mt-2">Compensation: salaried, published bands by role and licensure, posted in every job listing. We don't do "competitive salary" as a way of hiding a number.</p>
    </div>
    <div data-reveal style="--reveal-i:1">
      <div class="card">
        <h3>Open roles</h3>
        <p><strong>Speech-Language Pathologist (CCC-SLP)</strong><br>Full-time · posted Oct 2026 · we are actively hiring for this one, speech is our fullest schedule.</p>
        <p class="mt-2"><strong>Occupational Therapy Assistant (COTA/L)</strong><br>Part-time, Tue/Thu · working alongside Alma in the fine-motor studio.</p>
        <p class="mt-3">No other roles are open right now. We keep this page honest: when nothing is open, we say nothing is open, and when you're considering a clinic, we suggest you treat a careers page full of always-open listings as the red flag it usually is.</p>
        <p class="mt-2"><strong>How to apply:</strong> send a note and a resume to <a href="mailto:careers@tidepoolcare.example">careers@tidepoolcare.example</a>. A human reads it, usually the same week.</p>
      </div>
    </div>
  </div>
</section>
'''
write("careers.html", page("careers.html", "Careers",
  "Careers at Tidepool Pediatric Therapy: caseload caps, paid admin time, published salary bands. Current openings: SLP and COTA/L.",
  body))
