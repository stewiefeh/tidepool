import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import page, write, WAVE, WAVE_FLIP

POSTS = [
    ("journal-waitlists.html", "The waiting list is not a queue. It's a business decision.",
     "Nov 4, 2026", "Clinic thinking", "var(--coral)",
     "Every pediatric therapy clinic in the country could shrink its waitlist this quarter. None of them will. Not because they can't: because the waitlist is load-bearing.",
     [("Where the months come from",
       ["A four-month wait is what you get when one therapist carries seventy children and the schedule admits thirty new kids a month while graduating five. The math never lies, but it is usually called 'high demand' as if the schedule were weather.",
        "The uncomfortable version: the waitlist is profitable. It fills the pipeline, justifies expansion capital, and converts urgency into pricing power. Parents desperate at month four accept whatever slot appears at month five."]),
      ("What the cap actually costs us",
       ["Our caseload cap of two-thirds industry norm costs the clinic roughly a fifth of its theoretical revenue every month. It buys: an eleven-day median wait, zero turnover in three years, and the ability to say no to a referral we can't serve in two weeks instead of saying 'we'll call you.'",
        "We're a small clinic, so nobody has to take our model seriously at scale. But the excuse that it's impossible collapses the moment you look at any mid-size clinic's books: the money for shorter waits exists. It's simply currently earmarked for growth."]),
      ("The version I'd defend in an argument",
       ["A waitlist longer than four weeks for pediatric therapy should be embarrassing to the practice publishing it, the way a restaurant that can't seat anyone on a Tuesday is embarrassing. Demand for child development services is not a mystery to be managed; it is a service obligation to be planned around."])]),
    ("journal-screens.html", "Your child doesn't need a diagnosis to need a screen",
     "Oct 21, 2026", "Parent guidance", "var(--lagoon)",
     "The most common sentence we hear is some version of 'I don't want to label my child.' Here's the thing: a screen doesn't label anyone. It measures.",
     [("Labels vs. measurements",
       ["A screen produces a measurement: your child produces twelve words, uses four gestures, walks at fourteen months. A measurement has a place on a curve and a next step, and none of that requires anyone to write a diagnosis on a form.",
        "Diagnoses arrive from physicians and psychologists after real evaluation, and they come with their own purposes: school services, insurance coverage, community. But the screen that starts the whole process is just a well-trained pair of eyes and twenty minutes."]),
      ("The trap of waiting for certainty",
       ["Parents often wait for a diagnosis before seeking help, and clinicians sometimes wait for parents to be ready. The result is a loop where a two-year-old's language delay is discussed for a year and treated for a year, when it could have been screened in a week and treated from month three.",
        "The advice we give: don't wait for the label to get the measurement. The measurement is free here, it's free at First 5 screening events, and it's free anywhere a pediatric clinician answers the phone."]),
      ("What 'watchful waiting' should mean",
       ["Done right, watchful waiting is an active protocol: specific behaviors to watch, a specific re-check date, a specific threshold that ends the watching. Done wrong, it's a polite no.",
        "If someone tells you to 'wait and see,' ask what you're watching for and when you'll talk again. If there's no answer, you didn't get clinical advice; you got a brush-off."])]),
    ("journal-pronouns.html", "What the child who refuses therapy taught our whole clinic",
     "Oct 7, 2026", "Practice notes", "var(--sage-deep)",
     "Three years ago a four-year-old named Sam spent two entire sessions facing the wall. Today Sam is the reason every new family gets matched by fit, not by calendar.",
     [("The wall and the wall chart",
       ["Sam's first SLP did everything by the book: toys chosen from an assessment of interests, a visual schedule, a first-then board. Sam declined all of it and faced the wall. The notes said 'low engagement, monitor.'",
        "The second SLP spent the first session drawing whales. Not offering to draw whales: drawing them, narrating nothing, inviting nothing. By minute thirty Sam was drawing the whale's spout. By session four Sam was negotiating the number of whales. By session eight, Sam was narrating the whales, and the words had started."]),
      ("What we changed",
       ["We stopped asking 'what does the child like?' on intake forms and started asking 'what does the child do when nobody is asking anything of them?' That question has produced more first-session breakthroughs than any protocol we've bought.",
        "It also changed our hiring: we now watch candidates run a no-demand session. The clinicians who can sit comfortably in silence while a child investigates the room are the ones who keep families with us for years."]),
      ("The part parents should know",
       ["If your child's first session looks like nothing happened, ask what your clinician was doing. If they can tell you exactly what they were doing and what they'll try next, trust it. If they say 'we'll see how it goes,' ask more questions."])]),
]

body = f'''
<section class="hero"><div class="wrap narrow">
  <span class="eyebrow">Journal</span>
  <h1 class="mt-2">Notes from the harbor.</h1>
  <p class="lede">Clinic thinking, parent guidance, and the occasional argument we're willing to have in public. Written by the people who do the work, not a content team.</p>
</div></section>
{WAVE}
<section class="section section-tint"><div class="wrap"><div class="post-grid">
'''
for i, (slug, title, date, tag, color, dek, _sections) in enumerate(POSTS):
    body += f'''<a class="post-card" href="/{slug}" data-reveal style="--reveal-i:{i%3}">
  <div class="post-band"></div>
  <div class="post-body">
    <span class="post-meta">{tag} · {date}</span>
    <h3>{title}</h3>
    <p>{dek}</p>
  </div>
</a>
'''
body += f'''</div></div></section>
{WAVE_FLIP}
<section class="section"><div class="wrap narrow center">
  <div class="statement" data-reveal>
    <h2>Want the next one when it lands?</h2>
    <p>We email new journal posts about twice a month, plus the occasional honest note on waitlists or milestones. No marketing sequence, no "5 tips" listicles. Demo note: this portfolio site's signup is illustrative only.</p>
    <form class="form-grid" style="grid-template-columns:1fr auto;gap:0.6rem;max-width:28rem;margin-inline:auto" data-demo>
      <label class="visually-hidden" for="nl-email">Email</label>
      <input id="nl-email" type="email" placeholder="you@example.com" required>
      <button class="btn btn-primary" type="submit">Subscribe</button>
    </form>
  </div>
</div></section>
'''
write("journal.html", page("journal.html", "Journal",
  "Notes from the Tidepool harbor: essays on therapy waitlists, developmental screening, and clinical practice by our clinicians.",
  body))

for i, (slug, title, date, tag, color, dek, sections) in enumerate(POSTS):
    secs = ""
    for h, ps in sections:
        body_html = "".join(f"<p>{p}</p>" for p in ps)
        secs += f"<h2>{h}</h2>{body_html}"
    others = "".join(
        f'<a class="post-card" href="/{o[0]}" data-reveal><div class="post-band"></div><div class="post-body"><span class="post-meta">{o[3]} · {o[2]}</span><h3>{o[1]}</h3></div></a>'
        for o in POSTS if o[0] != slug)
    b = f'''
<section class="hero"><div class="wrap narrow">
  <span class="eyebrow">{tag} · {date}</span>
  <h1 class="mt-2" style="font-size:var(--step-3)">{title}</h1>
  <p class="lede">{dek}</p>
</div></section>
{WAVE}
<section class="section section-tint"><div class="wrap"><div class="prose">{secs}</div></div></section>
<section class="section"><div class="wrap">
  <div class="section-head center" data-reveal><span class="kicker">Keep reading</span><h2>More from the journal</h2></div>
  <div class="post-grid">{others}</div>
</div></section>
'''
    write(slug, page(slug, title, f"{title}: a journal essay from Tidepool Pediatric Therapy ({tag}, {date}).", b))
