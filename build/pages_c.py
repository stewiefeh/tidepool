import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from framework import page, write, WAVE, WAVE_FLIP
from pages_b import service_body, service_hero

# ---------------- OT ----------------
body = service_body("Occupational therapy",
  f'''{service_hero("✋", "Occupational therapy", "Mastering the everyday: hands, senses, and routines.", "2–14", "")}
<section class="section"><div class="wrap"><div class="prose" data-reveal>
<p>Occupational therapy has the most misleading name in healthcare. For children, "occupation" means the job of being a kid: playing, drawing, dressing, eating lunch in a loud cafeteria, sitting through circle time. Our OTs treat the sensory and motor skills underneath those jobs.</p>
<p>Both of our occupational therapists are OTR/Ls with pediatric specialty practice, and our clinic rooms are built for this work: a sensory gym with a rock wall and swings, a fine-motor studio, and a quiet regulation room for kids who need the volume turned down before they can work.</p>
</div></div></section>''',
  [
    ("Sensory processing &amp; regulation", "Kids who seek intense input or collapse under ordinary input. We build a sensory diet the family can actually run, then fade our support as regulation becomes the child's own skill."),
    ("Fine motor &amp; hand skills", "Grasps, scissors, buttons, zippers, and the two-finger strength that handwriting borrows. Progress is measured in skills mastered, not minutes spent."),
    ("Handwriting", "Print and cursive remediation built on posture, pencil grip, and letter formation, with home programs that take five minutes, not an hour."),
    ("Self-care routines", "Dressing, tooth-brushing, toileting schedules, and morning routines that currently run the whole household. We re-engineer the routine, not the child."),
    ("Visual-motor &amp; coordination", "Ball skills, puzzles, copying from the board: the eye-hand teamwork that classroom work quietly assumes."),
    ("Parent coaching", "Every OT plan includes structured parent sessions, because regulation strategies delivered only in the clinic are strategies your child never uses anywhere else."),
  ],
  [
    "Meltdowns in predictable settings: stores, haircuts, car rides",
    "Tags, seams, or certain clothing textures are unbearable",
    "Your child avoids coloring, cutting, or utensils",
    "Handwriting is illegible and practice at home ends in tears",
    "Morning routine takes more than one adult to survive",
    "Your child crashes, bumps, and seeks rough play constantly",
  ],
  [
    "Ayres-informed sensory integration, applied within activity-based sessions",
    "The zones-of-regulation framework for self-awareness and vocabulary",
    "Handwriting Without Tears as our foundational handwriting curriculum",
    " Routine-based intervention for self-care: practice where the skill is needed",
  ],
  "/team.html")

write("occupational-therapy.html", page("occupational-therapy.html", "Occupational Therapy",
  "Pediatric occupational therapy in Santa Cruz: sensory regulation, fine motor, handwriting, self-care. Two OTR/Ls, sensory gym on site.",
  body))

# ---------------- FEEDING ----------------
body = service_body("Feeding therapy",
  f'''{service_hero("🥕", "Feeding therapy", "Turning meals back into meals.", "0.5–12", "")}
<section class="section"><div class="wrap"><div class="prose" data-reveal>
<p>Feeding is the most physically complicated thing a child does all day: thirty-one muscles coordinating in a precise sequence, dozens of times, while sitting still. When any part of that chain struggles, families feel it three times a day.</p>
<p>Our feeding program is led by an SLP with board certification in swallowing and feeding and an OT with postgraduate feeding training, working together. That pairing matters: swallowing is a sensorimotor skill, and the child who cannot tolerate new textures and the child who cannot safely move a bolus are often the same child.</p>
</div></div></section>''',
  [
    ("Picky vs. problem eating", "We use the evidence-based distinction: a picky eater omits foods, a problem eater omits whole groups and drops previously accepted foods. Different problems, different plans."),
    ("Swallowing safety", "Clinical feeding evaluations with aspiration risk screening, coordination with your pediatrician, and when needed referral for instrumental studies."),
    ("Tube-to-table transitions", "Weaning plans built with your medical team, paced to your child's cues. Slow is fast in this work."),
    ("Mealtime behavior &amp; routines", "The battle at the table is usually a solved problem wearing a different costume. We fix the routine, the seating, and the pressure, then the eating follows."),
    ("Oral-motor skill work", "Chewing patterns, cup and straw drinking, and the oral coordination that solids quietly require."),
    ("Group: Food Explorers", "An eight-week group where four kids eat alongside each other. Peer modeling moves acceptance faster than any adult bribe we have ever tried."),
  ],
  [
    "Your child eats fewer than twenty foods and dropping more",
    "Meals regularly last longer than forty minutes",
    "Gagging, coughing, or choking during or after eating",
    "Growth concerns raised by your pediatrician",
    "A feeding tube is in place and the goal is oral eating",
    "Family meals have become a daily negotiation you keep losing",
  ],
  [
    "The Sequential Oral Sensory (SOS) approach for acquisition and expansion",
    "Responsive feeding principles: the child decides whether and how much",
    "Instrumental-study referral pathway with three local hospital partners",
    " Family meals coached in real time, including the siblings at the table",
  ],
  "/team.html")

write("feeding-therapy.html", page("feeding-therapy.html", "Feeding Therapy",
  "Feeding therapy for picky eating, swallowing safety, and tube-to-table transitions in Santa Cruz. SLP + OT co-treatment model.",
  body))

# ---------------- PT ----------------
body = service_body("Physical therapy",
  f'''{service_hero("🦵", "Physical therapy", "Milestones, movement, and confidence on the playground.", "0–18", "")}
<section class="section"><div class="wrap"><div class="prose" data-reveal>
<p>Pediatric physical therapy looks like play because that is how children learn movement: by playing hard and often. Underneath the games is a clinical eye watching quality, symmetry, and progression.</p>
<p>Our PT lead is a board-certified pediatric clinical specialist (PCS) with sixteen years across early intervention, NICU follow-up, and school-age orthopedics. The rest of the team carries that standard.</p>
</div></div></section>''',
  [
    ("Baby milestones", "Tummy time troubles, rolling, sitting, crawling, and first steps. Early intervention works, and the earlier visit is the easier fix."),
    ("Torticollis &amp; plagiocephaly", "Head-turn preference and flat spots, treated with positioning, stretching, and home programming that fits into diaper changes, not separate appointments."),
    ("Toe-walking &amp; gait", "Idiopathic toe-walking, in-toeing, and awkward gait patterns, assessed honestly: some resolve alone, and we will tell you when watching is the right treatment."),
    ("Coordination &amp; balance", "The child who falls harder and more often than peers, or avoids climbing equipment everyone else uses."),
    ("Return to play", "Post-injury and post-cast programs for school-age athletes and playground casualties, rebuilt to full confidence rather than bare tolerance."),
    ("Hypermobility &amp; posture", "Joint hypermobility, low muscle tone, and the posture habits that follow them, with strengthening programs kids actually complete."),
  ],
  [
    "Your baby is not rolling by six months or sitting by nine",
    "A strong head-turn preference or a flattening spot on the skull",
    "Toe-walking persisting past age three",
    "Your school-age child avoids stairs, bikes, or playground equipment",
    "Returning to sport after a sprain or fracture",
    "Grandma says 'he'll grow out of it' and your gut disagrees",
  ],
  [
    "Early intervention referral pathway, including county Regional Center coordination",
    "Standardized milestone measures at every visit, trended across time",
    "Home programs embedded in existing routines: bath time, diaper changes, playground trips",
    " Honest observation periods where treatment would add nothing but cost",
  ],
  "/team.html")

write("physical-therapy.html", page("physical-therapy.html", "Physical Therapy",
  "Pediatric physical therapy in Santa Cruz: milestones, torticollis, toe-walking, coordination, return to play. Board-certified PCS on staff.",
  body))
