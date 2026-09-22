from .sports_part1 import add, tech, _fb

IBA = "International Boxing Association (IBA) / national boxing federations; Olympic boxing is governed under the IOC-recognised pathway"
AIBA_ED = "Consult the current official boxing technical & competition rules used by your national federation or event (IBA, World Boxing, or Olympic qualifying body as applicable)"
rbx = _fb("official_summary", "National boxing federation / event organiser", AIBA_ED)
add(
    {
        "slug": "boxing",
        "name": "Boxing",
        "tagline": "A combat sport of punching with gloved fists under strict round, weight, and safety rules.",
        "overview": (
            "Boxing is a combat sport in which two athletes punch with gloved fists while defending with the hands, shoulders, and footwork. "
            "Amateur/Olympic-style and professional boxing use different round structures, scoring, and medical protocols. "
            "This page is educational only. Sparring and competition require a qualified coach, medical clearance where required, and an approved venue."
        ),
        "history": (
            "Prizefighting has a long history. The Marquess of Queensberry Rules (1867) shaped modern gloved boxing. "
            "International amateur governance has changed over time (AIBA/IBA and newer Olympic-related bodies). Always check which organisation governs your event."
        ),
        "player_count": "Two boxers in the ring, plus referee, judges, and ringside medical personnel in sanctioned bouts. Seconds (corner) are limited by the event rules.",
        "court_dimensions": "Ring sizes are specified by the governing body (often a square between commonly used amateur and professional ranges). Recreational gyms vary. Confirm apron, rope count, and padding for the event.",
        "scoring_system": "Amateur-style bouts are commonly scored on a 10-point must system by judges, or as specified by the event. Knockouts, technical knockouts, disqualification, and walkovers are outcomes defined in the technical rules. Professional round counts differ (often 4–12 rounds).",
        "governing_org": "Event-dependent (national federation; IBA or other recognised boxing bodies; professional commissions)",
        "featured": False,
        "popular": True,
        "icon": "sports_mma",
        "accent_color": "#6D597A",
        "categories": ["combat-sports", "individual-sports"],
        "positions": [
            ("Orthodox stance", "Left foot and hand forward for a right-handed boxer — common description, not a rule."),
            ("Southpaw stance", "Right foot and hand forward."),
            ("Referee", "Enforces the rules, controls the bout, and works with the doctor."),
        ],
        "rules": [
            rbx("Rounds", "Amateur bouts typically use shorter rounds and fewer rounds than professional bouts. Exact duration, rest intervals, and tournament formats are in the event technical rules.", 1),
            rbx("Legal blows", "Punches with the knuckle surface of the closed glove to legal target areas are generally the only scoring blows. The head, neck, back, below the belt, and kidneys are protected by specific fouls listed in the rules.", 2),
            rbx("Weight classes", "Boxers compete in defined weight categories. Weigh-in procedures are mandatory in sanctioned events.", 3),
            rbx("Mandatory counts and eight count", "Knocked-down boxers are administered counts as specified. Standing eight counts may exist in some amateur rules and not others.", 4),
            rbx("Fouls", "Holding, hitting on the break, low blows, head-butting, and hitting after the bell are typical fouls. The referee may warn, deduct, or disqualify.", 5),
            rbx("Medical stoppage", "The referee or ringside doctor can stop a bout for safety. This overrides competitive preference.", 6),
            rbx("Winning conditions", "Decision on points, knockout, technical knockout, disqualification, retirement, or other outcomes listed in the rules.", 7),
        ],
        "fouls": [
            ("Low blow", "foul", "A punch below the belt line as defined by the referee and rules."),
            ("Holding", "foul", "Clinching without attempting to punch, or using the hold to prevent the opponent from punching, as judged."),
            ("Head-butt", "foul", "Using the head as an impact tool, whether or not intentional."),
            ("Stop contest", "signal", "The referee waves off the bout for safety or a finished count."),
        ],
        "equipment": [
            ("Gloves", "Padded gloves of a weight specified by the event (for example 10 oz, 12 oz, 16 oz in gyms).", "Competition glove weight is a rule item. Training gloves are often heavier.", "Do not spar in damaged or undersized gloves. Hand wraps should be applied as coached."),
            ("Headgear", "Used in many amateur and recreational sparring settings; not used in some elite/open-headgear rule sets.", "Must fit and remain secure.", "Headgear reduces cuts more than concussions. It is not a licence to hit harder."),
            ("Mouthguard", "Protects teeth and may reduce some oral injuries.", "Boil-and-bite or custom.", "Never spar without a mouthguard."),
            ("Groin protector", "Required in many rule sets.", "Must fit under the waistband as required.", "Check that it does not ride up."),
            ("Ring", "Ropes, canvas, and corner pads.", "Specification depends on the sanctioning body.", "Keep the canvas dry. No shoes with street dirt."),
        ],
        "techniques": [
            tech("Jab", "The lead-hand straight punch used to measure distance and set up other punches.", ["Hands up.", "Extend the lead hand without dropping the rear hand.", "Snap back to guard.", "Step when the coach teaches a step-jab."], "Shadow-box the jab before hitting a bag.", "Dropping the rear hand; lunging off-balance.", "Only hit bags, pads, or opponents under a coach. No unsupervised sparring.", 1),
            tech("Straight rear hand", "A power straight punch from the back hand (cross).", ["Rotate the back foot and hip.", "Keep the chin tucked.", "Return to guard immediately."], "Focus on balance, not maximum power.", "Falling forward; telegraphing by pulling back a long way.", "Stop if the wrist is not aligned. Wrist injuries are common with poor bag technique.", 2),
            tech("Guard and footwork", "Staying behind a high guard while moving to safe angles.", ["Feet shoulder-width as coached.", "Small steps.", "Do not cross the feet.", "Reset after combinations."], "Learn to move without lowering the hands.", "Standing square; walking straight backward in a straight line only.", "Sparring is optional and high-risk. Many beginners should stay on pads and bags longer.", 3),
        ],
        "safety": [
            ("Medical clearance", "injuries", "Get medical advice before combat sports if you have concussion history, bleeding disorders, or other conditions. Follow suspension periods after knockouts."),
            ("Sparring", "supervision", "Spar only with matched experience, a coach present, and agreed intensity. Stop at any concussion symptom."),
        ],
        "terms": [
            ("Jab", "Lead-hand straight punch."),
            ("Cross", "Rear-hand straight punch."),
            ("Clinched", "Holding at close range; the referee may break."),
            ("TKO", "Technical knockout — the bout is stopped because a boxer cannot continue safely."),
            ("10-point must", "A common judging system awarding 10 points to the round winner."),
        ],
        "faqs": [
            ("Is this a substitute for a boxing gym?", "No. Combat sports require in-person coaching, medical processes, and insurance/sanctioning that a website cannot provide."),
            ("Which rulebook should I use?", "Use the national federation or commission that sanctions your bout. Do not mix professional and amateur rules casually."),
        ],
        "references": [
            ("Event sanctioning body", "Technical & Competition Rules for the relevant boxing organisation", "Verify year and organisation before any bout", None, "International boxing governance has been in transition. Name the exact organisation on the bout contract."),
        ],
    }
)

WT = "World Taekwondo (WT)"
WT_ED = "Consult the current WT Competition Rules & Interpretation"
rtk = _fb("official_summary", WT, WT_ED)
add(
    {
        "slug": "taekwondo",
        "name": "Taekwondo",
        "tagline": "A Korean martial art and Olympic sport emphasising kicking, with electronic scoring in elite WT kyorugi.",
        "overview": (
            "Taekwondo includes sparring (kyorugi), patterns (poomsae), and breaking. Olympic-style WT kyorugi uses weight classes, protective equipment, and often Protector and Scoring Systems (PSS). "
            "ITF and other organisations use different rules. This page focuses on commonly taught educational points and WT-style competition concepts."
        ),
        "history": "Modern taekwondo was organised in Korea in the mid-20th century, drawing on earlier Korean martial arts. It became a full Olympic sport in 2000 (after a demonstration history). World Taekwondo governs the Olympic kyorugi pathway.",
        "player_count": "Two contestants in a sparring bout, plus referee, judges, and a commission as specified. Poomsae may be individual or team.",
        "court_dimensions": "WT kyorugi typically uses an octagonal contest area on a matted field of play; exact sizes are in the current WT rules. Recreational dojangs use various mat sizes.",
        "scoring_system": "Punches and kicks to legal target areas score different points; turning kicks and kicks to the head score more in current WT kyorugi. Gam-jeom penalties award a point to the opponent. Best-of-three rounds has been used in recent WT rules — confirm the current edition.",
        "governing_org": WT,
        "featured": False,
        "popular": False,
        "icon": "sports_martial_arts",
        "accent_color": "#003566",
        "categories": ["combat-sports", "individual-sports"],
        "positions": [
            ("Kyorugi athlete", "Sparring competitor."),
            ("Poomsae athlete", "Patterns competitor."),
            ("Referee", "Manages the contest, penalties, and video replay requests as allowed."),
        ],
        "rules": [
            rtk("Contest format", "Recent WT kyorugi uses a best-of-three round format with point caps and round winners. Older single-match cumulative scoring still appears in some events. Read the edition adopted by your tournament.", 1),
            rtk("Legal techniques", "Fist techniques to the trunk and kicking techniques to trunk and head are the typical scoring tools, with glove/PSS validity rules. Attacks below the waist are not scoring WT kyorugi techniques.", 2),
            rtk("PSS and headgear", "Electronic body protectors and head PSS are used at many elite events. Valid contact thresholds are technical settings, not something to copy in a school gym.", 3),
            rtk("Penalties (gam-jeom)", "Falling, turning the back, holding, attacking after 'kalyeo', and other prohibited acts give a point to the opponent as listed.", 4),
            rtk("Winning conditions", "Win the required number of rounds, win by points difference (punch-out) if in force, or win by referee stoppage, withdrawal, or disqualification as specified.", 5),
        ],
        "fouls": [
            ("Gam-jeom", "foul", "A penalty point to the opponent for a prohibited act."),
            ("Attack after kalyeo", "foul", "Hitting after the referee breaks the contest."),
            ("Falling", "foul", "Going down can be penalised in WT kyorugi even without a kick, as currently written — confirm the edition."),
        ],
        "equipment": [
            ("Dobok", "The uniform.", "WT-approved doboks for sanctioned events.", "Sleeves and trousers should allow kicking without tearing."),
            ("Hogu (trunk protector)", "Protects the torso and often contains PSS sensors.", "Must fit the weight class as required.", "Do not spar full-contact without required protectors."),
            ("Head protector", "Protects the head; may include PSS.", "Secure chin strap.", "Does not prevent concussion. Control contact."),
            ("Mouthguard, groin guard, gloves, shin/instep", "Mandatory in many WT events.", "List is in the WT rules.", "Replace cracked mouthguards."),
            ("Mats", "Shock-absorbing field of play.", "Thickness specified for competitions.", "Tape seams. No gaps."),
        ],
        "techniques": [
            tech("Front kick (ap chagi)", "A snapping or pushing kick with the ball of the foot.", ["Chamber the knee.", "Extend without hyperextending the knee.", "Recoil.", "Replace the foot in stance."], "Hold a wall or a partner’s shoulder for balance at first.", "Leaning too far back; locking the knee violently.", "Kick pads, not people, until a coach structures contact. Control distance.", 1),
            tech("Roundhouse kick (dollyo chagi)", "The most common WT scoring kick to the hogu or head (head only when allowed and safe).", ["Pivot the standing foot.", "Chamber.", "Strike with the instep or ball as taught.", "Recover guard."], "Hit a paddle at mid-section height for a long time before head-height kicking.", "Not pivoting; kicking with a floppy foot.", "Head kicks are high-risk. Many beginners should not train head contact at all.", 2),
            tech("Guard and movement", "WT-style bouncing stance and checking distance.", ["Hands up.", "Small hops as coached.", "Do not cross the feet.", "Exit on an angle after kicking."], "Learn to check a pad before adding speed.", "Dropping hands after every kick; standing square.", "Stop when tired enough that you cannot protect your head.", 3),
        ],
        "safety": [
            ("Contact progression", "supervision", "Light technical sparring under a qualified instructor comes long before tournament contact."),
            ("Concussion", "injuries", "Any suspected concussion ends training that day. Follow medical advice for return."),
        ],
        "terms": [
            ("Kyorugi", "Sparring."),
            ("Poomsae", "Forms / patterns."),
            ("Hogu", "Trunk protector."),
            ("Gam-jeom", "Penalty."),
            ("Kalyeo", "Break / separate command."),
            ("Keuman", "End of the contest or round, as commanded."),
        ],
        "faqs": [
            ("WT vs ITF?", "Different organisations, patterns, and sparring rules. Do not assume Olympic WT rules apply in an ITF school."),
        ],
        "references": [
            (WT, "WT Competition Rules & Interpretation", "Current edition — worldtaekwondo.org", "https://www.worldtaekwondo.org", "Poomsae has a separate competition rules document."),
        ],
    }
)

WBSC = "World Baseball Softball Confederation (WBSC)"
MLB_NOTE = "Major League Baseball publishes its own Official Baseball Rules; many national federations use WBSC or adapted amateur codes."
rbb = _fb("official_summary", WBSC, "Consult current WBSC Baseball Rules and/or the Official Baseball Rules used by your league")
add(
    {
        "slug": "baseball",
        "name": "Baseball",
        "tagline": "A bat-and-ball game of innings, strikes, and nine defensive positions.",
        "overview": "Baseball is a team sport in which the offensive team tries to score runs by touching home plate after advancing around bases. The defensive team pitches and fields to record outs. Professional (MLB), WBSC, NCAA, and youth codes (Little League, etc.) differ in mound distance, pitch-count, and extra-inning rules.",
        "history": "Baseball evolved from older bat-and-ball games in the United States in the 19th century. MLB’s Official Baseball Rules are a major reference. WBSC governs international baseball and softball together.",
        "player_count": "Nine defensive players in standard baseball (some youth leagues use 10). Line-ups list a batting order; extra hitters / DH rules vary by league.",
        "court_dimensions": "A 90-foot (27.43 m) square diamond is standard for adult baseball. Pitching distance is 60 feet 6 inches (18.44 m) in standard adult rules. Outfield fences vary by park. Youth diamonds are smaller.",
        "scoring_system": "A run scores when a runner legally touches home. A game is typically 9 innings (7 in some levels). The team with more runs after regulation innings wins; extra innings follow league rules (including possible ‘start on second’ variants).",
        "governing_org": WBSC,
        "featured": False,
        "popular": True,
        "icon": "sports_baseball",
        "accent_color": "#BC4749",
        "categories": ["team-sports", "outdoor-sports"],
        "positions": [
            ("Pitcher", "Delivers the pitch from the mound."),
            ("Catcher", "Receives pitches and manages the plate."),
            ("First / second / third base", "Infielders at the bases."),
            ("Shortstop", "Infielder between second and third."),
            ("Left / centre / right field", "Outfielders."),
            ("Designated hitter", "A hitter who bats in place of a fielder, where the league allows."),
        ],
        "rules": [
            rbb("Innings and outs", "Each half-inning ends after three outs. Nine innings is standard adult length; many amateur games use seven.", 1),
            rbb("Strikes and balls", "A strike is a pitch in the strike zone taken, a swing-and-miss, or a foul (with foul-bunt and two-strike foul exceptions). Four balls award a walk. Definitions of the strike zone differ slightly by code.", 2),
            rbb("Fair and foul", "A batted ball’s fair/foul status depends on where it settles or is first touched relative to the foul lines, as detailed in the rules.", 3),
            rbb("Force and tag plays", "Runners may be forced to advance; other outs require a tag of the runner or the base as specified.", 4),
            rbb("Pitching", "Legal delivery, balks (in codes that use them), and pitch-clock / pitch-count rules are league-specific. Youth pitch-count limits are safety rules — follow them.", 5),
            rbb("Winning conditions", "Most runs after the scheduled innings, with extra-inning procedures as published for that league.", 6),
        ],
        "fouls": [
            ("Balk", "violation", "An illegal motion by a pitcher with runners on base, in codes that include balks."),
            ("Interference", "violation", "Offensive or defensive interference as defined, including runner interference with a batted ball."),
            ("Foul ball", "violation", "A batted ball that is not fair; usually a strike unless already two strikes (with exceptions)."),
        ],
        "equipment": [
            ("Ball", "Leather-covered baseball.", "Circumference and weight specified by the code.", "Do not use a ball with a broken cover."),
            ("Bat", "Wood in many professional settings; metal/composite in many amateur leagues with BBCOR or other standards.", "Length/weight limits by age group.", "Cracked bats must be removed immediately."),
            ("Helmet", "Required for batters and runners in amateur play; professional use also standard.", "NOCSAE-certified helmets in many youth leagues.", "Helmets must fit. Face guards may be required for some ages."),
            ("Glove", "Position-specific gloves/mitts.", "Catcher and first-base mitts differ.", "Do not leave a glove as a trip hazard on the field."),
            ("Catcher’s gear", "Mask, chest protector, shin guards.", "Required in amateur baseball.", "Throat guards as required by the league."),
        ],
        "techniques": [
            tech("Throwing", "Overhand throw with a four-seam grip for many infield throws.", ["Grip across seams for a four-seamer.", "Step toward the target.", "Follow through.", "Receive with two hands when possible."], "Short-toss before long throws.", "Side-arming from a poor setup every time; throwing across a dropped elbow when fatigued.", "Stop at elbow or shoulder pain. Youth pitchers must follow pitch-count rest rules.", 1),
            tech("Batting", "A balanced swing at pitches in the zone.", ["Athletic stance.", "See the ball.", "Rotate hips.", "Finish in control."], "Tee work and front toss before live batting practice.", "Stepping in the bucket; swinging at everything.", "Helmets on. No one stands in the throwing lane behind the batter.", 2),
            tech("Fielding grounders", "Moving to the ball and a reliable funnel to the throw.", ["Get in front when possible.", "Two hands.", "Find the grip.", "Throw with the feet underneath."], "Start with rolled balls.", "Sitting back on the heels; looking up too soon.", "Do not field with a knee on a hard infield without progression. Watch for bad hops.", 3),
        ],
        "safety": [
            ("Batting practice", "supervision", "Use L-screens. Nobody walks behind a hitter or in the path of a live throw."),
            ("Pitch counts", "safety", "Youth arm injuries are associated with overuse. Follow official pitch-count and rest tables for the association."),
        ],
        "terms": [
            ("Strike", "A counted pitch against the batter as defined by balls/strikes rules."),
            ("Ball", "A pitch not a strike, not swung at."),
            ("Walk (BB)", "Batter awarded first after four balls."),
            ("Force out", "An out recorded by tagging a base to which a runner is forced."),
            ("Inning", "A unit of play in which each team has a turn on offense until three outs."),
        ],
        "faqs": [
            ("Is a foul with two strikes an out?", "A foul ball with two strikes is generally not a third strike unless it is a bunt or a foul tip caught by the catcher, depending on the exact rule. Read your code."),
        ],
        "references": [
            (WBSC, "WBSC Baseball Rules", "Current edition — wbsc.org", "https://www.wbsc.org", "Many North American leagues instead apply MLB Official Baseball Rules or a youth association book."),
            ("MLB", "Official Baseball Rules", "Current season", "https://www.mlb.com", "Professional procedures (pitch clock, extra innings) may not apply to amateur baseball."),
        ],
    }
)

rsb = _fb("official_summary", WBSC, "Consult current WBSC Softball Rules (and your national/association book: USA Softball, Softball Australia, etc.)")
add(
    {
        "slug": "softball",
        "name": "Softball",
        "tagline": "A bat-and-ball sport related to baseball, with a larger ball and a shorter diamond; fastpitch and slowpitch differ.",
        "overview": "Softball includes fastpitch (including Olympic-style) and slowpitch recreational codes. The ball is larger than a baseball, the field is smaller, and pitching is underarm. Do not mix fastpitch and slowpitch rules.",
        "history": "Softball originated in the United States in the late 19th century as an indoor/accessible bat-and-ball game. WBSC governs international softball. Women’s fastpitch has been on and off the Olympic programme.",
        "player_count": "Fastpitch typically uses 9 defensive players (some youth/slowpitch use 10 with a short fielder). Batting orders and extra hitters/DP-FLEX rules are code-specific.",
        "court_dimensions": "A common adult fastpitch diamond uses 60-foot (18.29 m) bases. Pitching distance varies by code and age (often 43 feet / 13.11 m for adult women in international fastpitch — confirm the current book). Outfield fences vary.",
        "scoring_system": "Runs score by legally touching home. Games are often 7 innings. Run-ahead (mercy) rules are common in amateur play. International tie-breakers may start runners on base — check the event.",
        "governing_org": WBSC,
        "featured": False,
        "popular": False,
        "icon": "sports_baseball",
        "accent_color": "#F4A261",
        "categories": ["team-sports", "outdoor-sports"],
        "positions": [
            ("Pitcher", "Underarm fastpitch or slowpitch delivery, depending on the code."),
            ("Catcher", "Receives pitches; equipment requirements are strict in fastpitch."),
            ("Infielders and outfielders", "Similar names to baseball; slowpitch may add a rover/short fielder."),
            ("DP/FLEX", "A fastpitch line-up option allowing a designated player and a flexible fielder, as defined in the rules."),
        ],
        "rules": [
            rsb("Fastpitch vs slowpitch", "Pitch trajectory, stealing, bunting, and scoring rules differ completely between the codes. Use the correct rulebook.", 1),
            rsb("Innings", "Seven innings is common. International events may use time plus innings.", 2),
            rsb("Pitching (fastpitch)", "A legal windmill or other allowed underarm delivery with a step and pivot as defined. Illegal pitches have prescribed penalties.", 3),
            rsb("Look-back / runners", "Fastpitch has runner lead-off and look-back rules that baseball players often misapply. Read the softball-specific text.", 4),
            rsb("Winning conditions", "More runs after regulation, with tie-break and run-ahead rules as published.", 5),
        ],
        "fouls": [
            ("Illegal pitch", "violation", "A delivery that does not meet the pitching rule; results vary by code (ball, delayed dead ball, etc.)."),
            ("Leaving early", "violation", "A runner leaving the base before the pitch is released, in codes that forbid leads."),
        ],
        "equipment": [
            ("Softball", "Larger circumference than a baseball; optic yellow common.", "12-inch adult; 11-inch youth common. Compression specs exist for slowpitch.", "Do not mix baseballs into softball drills unexpectedly."),
            ("Bat", "Must be on the association’s approved list (for example USA Softball / WBSC stamps).", "Using a non-approved bat can be an ejection in sanctioned play.", "Inspect for dents and rattle."),
            ("Fielder’s mask", "Increasingly required or recommended for infielders in fastpitch because of pitch speed.", "Follow your association.", "A mask is not optional if your league mandates it."),
            ("Catcher’s gear", "Helmet-mask, chest, shins; throat protection as required.", "NOCSAE standards in many regions.", "Fastpitch pitching speed makes this essential."),
        ],
        "techniques": [
            tech("Underarm pitch (fastpitch intro)", "A circular windmill delivery taught only by a qualified pitching coach.", ["Learn the snap and stride without full speed.", "Keep the arm path consistent.", "Finish in a fielding position."], "Many beginners should not jump to full windmill. Sequence matters.", "Wrist lag that stresses the shoulder; bowling with a bent elbow incorrectly.", "Pitch-count and rest still matter. Stop at sharp pain.", 1),
            tech("Slap hitting (fastpitch)", "A left-handed running slash or slap used against fastpitch speed.", ["Timing with the pitcher.", "Contact while moving as coached.", "First-step to first base."], "Optional advanced skill. Square-up hitting comes first for most.", "Leaving the box early illegally.", "Helmets on. Do not practice slaps with an unprotected pitcher close.", 2),
        ],
        "safety": [("Infield reaction", "equipment", "Consider masks for corner infielders in fastpitch. No practice without a catcher in gear when pitching live.")],
        "terms": [
            ("Fastpitch", "A code with a fast underarm pitch, stealing, and bunting generally allowed."),
            ("Slowpitch", "A code with an arcing pitch and usually no stealing/bunting."),
            ("Illegal pitch", "A pitching-rule violation."),
            ("Look-back rule", "A fastpitch runner rule after the pitcher has the ball in the circle."),
        ],
        "faqs": [("Can baseball players play softball with the same rules?", "No. Distances, pitching, and runner rules differ. Learn the softball book.")],
        "references": [
            (WBSC, "WBSC Softball Rules", "Current edition — wbsc.org", "https://www.wbsc.org", "National associations (USA Softball, etc.) publish widely used amateur codes."),
        ],
    }
)

UCI = "Union Cycliste Internationale (UCI)"
UCI_ED = "Consult the current UCI Cycling Regulations"
rcy = _fb("official_summary", UCI, UCI_ED)
add(
    {
        "slug": "cycling",
        "name": "Cycling",
        "tagline": "Racing and riding bicycles on road, track, mountain, BMX, and other UCI disciplines.",
        "overview": (
            "Cycling includes road racing, time trials, track, mountain bike (XCO, downhill), BMX, cyclocross, and recreational riding. "
            "UCI publishes extensive regulations per discipline. Road rules for bunch racing (drafting, feeding, helmets) differ from time trials and from traffic law. "
            "On public roads, traffic law always applies."
        ),
        "history": "Bicycle racing organised in the late 19th century. The UCI was founded in 1900. Road cycling’s Grand Tours and World Championships are flagship events. Mountain bike and BMX joined the Olympic programme later.",
        "player_count": "Individual time trials are solo. Road bunch races and most MTB/BMX events are mass-start. Team time trials and team pursuit have set team sizes in UCI regulations.",
        "court_dimensions": "Not a court sport. Road courses are event-specific. Track (velodrome) geometry is regulated for UCI events. BMX tracks and MTB courses are built to discipline standards.",
        "scoring_system": "Stage races use time general classification, plus possible points and mountains classifications. One-day races are decided by finish order or time. Track events each have their own scoring (sprint, keirin, omnium, madison, pursuit).",
        "governing_org": UCI,
        "featured": False,
        "popular": True,
        "icon": "directions_bike",
        "accent_color": "#FFB703",
        "categories": ["outdoor-sports", "individual-sports"],
        "positions": [
            ("Road racer", "Competes in bunch races, classics, or stage races."),
            ("Time trialist", "Rides alone against the clock (or in a TTT)."),
            ("Track sprinter / endurance", "Velodrome specialists."),
            ("MTB / BMX rider", "Off-road or gate-start specialists."),
        ],
        "rules": [
            rcy("Helmets", "Approved helmets are required in UCI events. Recreational riders should still wear a helmet; some jurisdictions require it by law.", 1),
            rcy("Drafting", "Drafting is integral to road bunch racing but forbidden in individual time trials except in listed circumstances. Holding a car or another rider is illegal.", 2),
            rcy("Equipment", "Bicycle dimensions, wheels, helmets, and positions (especially TT and track) are tightly regulated. Recreational bikes need not meet TT rules but must be safe.", 3),
            rcy("Conduct", "Dangerous riding, irregular sprinting, and discarding equipment unsafely can be sanctioned. Commissaires apply the regulations and race bible.", 4),
            rcy("Winning conditions", "First across the line, lowest cumulative time, or event-specific points, as published.", 5),
        ],
        "fouls": [
            ("Illegal drafting (TT)", "violation", "Taking shelter behind another rider or vehicle in an individual time trial."),
            ("Dangerous riding", "foul", "Moving irregularly in a sprint or endangering others."),
            ("Littering outside zones", "violation", "Discarding bottles/musettes outside designated zones in races that use them."),
        ],
        "equipment": [
            ("Bicycle", "Must be in safe working order; UCI events add dimensional rules.", "Brakes, headset, and wheels checked before group rides.", "Do not ride with a cracked frame or failing brakes."),
            ("Helmet", "Impact protection.", "CPSC/EN and UCI-approved as applicable.", "Replace after a crash or when expired by maker guidance."),
            ("Lights and visibility", "Required by law in many places at night.", "Front white, rear red as locally specified.", "Group rides at dusk need lights even if not a race."),
            ("Gloves, glasses, shoes", "Comfort and protection.", "Clipless pedals need practice in a safe area.", "Unclip practice on grass before traffic."),
        ],
        "techniques": [
            tech("Group riding", "Holding a straight line, overlapping wheels cautiously, and communicating.", ["Look past the rider in front.", "Hold your line.", "Call holes and slowing.", "Do not slam on the brakes without warning."], "Start at the back of a slow group.", "Half-wheeling; overlapping then swerving.", "Road riding is traffic. Obey lights. This is not closed-course advice for public roads.", 1),
            tech("Braking and cornering", "Modulating brakes before the turn, then releasing to grip.", ["Brake in a straight line when possible.", "Outside foot down as commonly taught for some corners.", "Look through the turn.", "Outside pedal pressure as coached."], "Practice on a closed empty lot, not in traffic.", "Grabbing only the front brake suddenly; coasting with the inside pedal down on a lean.", "Wet paint and metal are slippery. Reduce speed before you need to.", 2),
            tech("Cadence and gears", "Choosing a sustainable cadence rather than grinding a huge gear.", ["Shift before the hill steepens.", "Keep a smooth pedal stroke.", "Don’t cross-chain if it rubs badly."], "A coach or experienced rider can help set gear range.", "Stomping a gear that stalls the knee.", "Stop if the knee has sharp pain. Bike fit is individual — see a fitter for persistent issues.", 3),
        ],
        "safety": [
            ("Traffic", "safety", "On public roads you are a vehicle plus a vulnerable road user. Lights, positioning, and predictable behaviour matter more than race tactics."),
            ("Group crash risk", "supervision", "Bunch riding multiplies crash risk. New riders should avoid fast bunches and races until skills are stable."),
        ],
        "terms": [
            ("Drafting / slipstream", "Riding in reduced air resistance behind another rider."),
            ("Peloton", "The main bunch in a road race."),
            ("Time trial (TT)", "A solo or team race against the clock."),
            ("Commissaire", "A cycling race official."),
            ("General classification (GC)", "Overall time ranking in a stage race."),
        ],
        "faqs": [
            ("Do UCI rules apply on a bike path?", "No. Traffic law and local path rules apply. UCI rules apply to sanctioned events."),
        ],
        "references": [
            (UCI, "UCI Cycling Regulations", "Current edition — uci.org", "https://www.uci.org", "Each discipline (road, track, MTB, BMX, CX) has its own parts. Event technical guides add course-specific rules."),
        ],
    }
)
