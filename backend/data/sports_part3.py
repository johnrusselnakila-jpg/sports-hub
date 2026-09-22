from .sports_part1 import add, tech, _fb, OFF

ITF = "International Tennis Federation (ITF)"
ITF_ED = "Consult the current ITF Rules of Tennis at itftennis.com"
rt = _fb(OFF, ITF, ITF_ED)
add(
    {
        "slug": "tennis",
        "name": "Tennis",
        "tagline": "A racquet sport scored in points, games, and sets, played on a marked rectangular court.",
        "overview": "Tennis is played in singles or doubles. Players hit a felt-covered ball over a net so the opponent cannot return it in play. Scoring (15, 30, 40, game) is distinctive. Grand Slam events may use different final-set tie-break policies.",
        "history": "Lawn tennis emerged in Britain in the 1870s. The ITF (formerly ILTF) governs the Rules of Tennis. Tennis returned to the Olympic programme in 1988.",
        "player_count": "Singles: one vs one. Doubles: two vs two.",
        "court_dimensions": "ITF court is 23.77 m long. Width is 8.23 m for singles and 10.97 m for doubles. Net height is 0.914 m at the centre. Surface (clay, grass, hard, indoor) changes bounce and movement.",
        "scoring_system": "A game is typically won by the first player to win four points with a margin of two (15, 30, 40, game; deuce/advantage). Sets are usually first to six games with a margin of two, with tie-breaks at 6–6 unless a competition specifies otherwise. Matches are best of three or five sets.",
        "governing_org": ITF,
        "featured": True,
        "popular": True,
        "icon": "sports_tennis",
        "accent_color": "#E9C46A",
        "categories": ["racquet-sports", "individual-sports", "outdoor-sports"],
        "positions": [
            ("Baseline player", "Competes mainly from behind the baseline."),
            ("Serve-and-volley", "A style that approaches the net after the serve."),
            ("Doubles net player", "In many doubles formations, one player covers the net."),
        ],
        "rules": [
            rt("Scoring", "Point names, deuce, advantage, and tie-break procedures are defined in the ITF Rules. Fast4, no-ad, and match tie-breaks appear in some competitions and must be announced in advance.", 1),
            rt("Serve", "The server starts from the right court for the first point of a game and alternates sides. The serve must land in the diagonally opposite service box. Foot faults, lets, and faults are defined in the Rules. Two serve attempts are allowed in standard scoring.", 2),
            rt("Let", "A serve that touches the net and lands in the correct service box is a let and is replayed in standard rules. Other lets exist for hindrance.", 3),
            rt("In and out", "A ball is in if it touches any part of the line. Players call their own lines in many recreational matches; officials call them in professional events.", 4),
            rt("Code and hindrance", "Intentional hindrance, abuse of balls or racquets, and time rules are covered by ITF Rules and event codes of conduct.", 5),
            rt("Winning conditions", "The player or pair who wins the required number of sets wins the match.", 6),
        ],
        "fouls": [
            ("Fault", "violation", "A serve that misses the service box or is a foot fault."),
            ("Double fault", "violation", "Two consecutive service faults, losing the point."),
            ("Foot fault", "violation", "Illegal foot position or movement during the serve as defined in the Rules."),
        ],
        "equipment": [
            ("Racquet", "Used to strike the ball.", "ITF publishes rules on racquet size, power, and extra devices. Recreational racquets should be intact.", "Stop using a cracked racquet. Consider eye protection in doubles if recommended by your club."),
            ("Tennis ball", "Pressurised or pressureless felt balls.", "ITF approved balls are classified by speed. Altitude and surface matter.", "Do not play with wet, dead, or bald balls on a crowded court."),
            ("Net", "Divides the court.", "0.914 m at the centre.", "Do not sit on the net. Check centre strap."),
            ("Court shoes", "Surface-specific outsoles (clay herringbone, hard-court, grass).", "Incorrect shoes increase slip risk.", "Do not wear running-only shoes on clay if the club forbids them."),
        ],
        "techniques": [
            tech("Serve", "Overhead serve placing the ball in the diagonal box.", ["Platform or pinpoint stance.", "Toss consistently in front.", "Pronate through contact as coached.", "Recover to a split step."], "Develop a reliable second serve before adding heavy first-serve power.", "Tossing behind the head; both feet leaving in a foot-fault pattern.", "Do not serve if people are walking behind the server.", 1),
            tech("Forehand", "Groundstroke on the dominant side.", ["Unit turn.", "Contact in front.", "Finish across or up depending on grip and spin."], "Start with a semi-western or eastern grip as a coach prefers.", "Late contact; opening the racquet face.", "Give partners space on the sideline.", 2),
            tech("Backhand", "One-handed or two-handed groundstroke on the non-dominant side.", ["Turn the shoulders.", "Step in or use an open stance as taught.", "Contact in front.", "Recover to the middle of your side."], "Two-handed backhands are common for beginners.", "Pulling up early; stalling with a slice every time without purpose.", "Watch for racquet path toward a doubles partner.", 3),
            tech("Volley", "A shot hit before the bounce, usually at net.", ["Split step.", "Punch with a short backswing.", "Keep the racquet head stable.", "Move through the shot."], "Start with mid-court feeding, not full smashes at the net player.", "Big swings at net; volleying off the back foot only.", "Do not volley from immediately on top of the net tape.", 4),
        ],
        "safety": [("Heat and surfaces", "safety", "Hard courts increase impact. Clay can be slippery when watered unevenly. Rest in heat.")],
        "terms": [
            ("Serve", "The stroke that starts the point."),
            ("Let", "A replayed point in listed cases, including some net serves."),
            ("Deuce", "The score when both players have won three points in a game (40–40) in standard scoring."),
            ("Tie-break", "A special game used to decide a set at 6–6 in many formats."),
            ("Ace", "A serve not touched by the receiver."),
            ("Break point", "A point that would win the receiver the game."),
        ],
        "faqs": [("What is a match tie-break?", "Some events replace a full third set with a tie-break (often to 10). It must be specified in the competition rules.")],
        "references": [(ITF, "Rules of Tennis", "Current edition — itftennis.com", "https://www.itftennis.com", "Grand Slam rulebooks may add procedures (final-set policy, review systems).")],
    }
)

ITTF = "International Table Tennis Federation (ITTF)"
ITTF_ED = "Consult the current ITTF Statutes (Laws of Table Tennis) at ittf.com"
rtt = _fb(OFF, ITTF, ITTF_ED)
add(
    {
        "slug": "table-tennis",
        "name": "Table Tennis",
        "tagline": "A fast racquet sport played on a table with a lightweight ball and rally scoring.",
        "overview": "Table tennis (ping-pong in casual speech) is played singles or doubles. Players hit a ball over a net on a table so the opponent cannot return it legally. Service rules, including toss and hide-the-ball restrictions, are detailed in the ITTF Laws.",
        "history": "The sport developed from indoor lawn-tennis adaptations in England around the turn of the 20th century. The ITTF was founded in 1926. Table tennis has been Olympic since 1988.",
        "player_count": "Singles or doubles (two vs two). Team events use ordered matches according to competition regulations.",
        "court_dimensions": "The playing surface is 2.74 m long, 1.525 m wide, and 76 cm high. The net assembly is 15.25 cm high. Surrounding court space is specified for international events.",
        "scoring_system": "Rally scoring. Games are typically played to 11 points, must win by 2. Matches are usually best of 5 or 7 games at elite level. Service alternates every two points until 10–10, then every point.",
        "governing_org": ITTF,
        "featured": False,
        "popular": True,
        "icon": "sports_tennis",
        "accent_color": "#9B2226",
        "categories": ["racquet-sports", "individual-sports"],
        "positions": [("Shakehand player", "Holds the blade similar to a handshake — a common grip."), ("Penhold player", "Holds the blade like a pen — another established grip family.")],
        "rules": [
            rtt("Scoring", "A point is scored on every rally. Games to 11, win by 2, are standard. Match length is set by the competition.", 1),
            rtt("Serve", "The ball must be tossed from an open palm, near vertically, at least 16 cm, and struck behind the end line so that it bounces first on the server’s side then the receiver’s side. Hidden serves are illegal. Read the current Law wording.", 2),
            rtt("Doubles serve and receive", "Doubles has additional order-of-play and service-court (right half) requirements.", 3),
            rtt("Let", "A serve that touches the net assembly and is otherwise legal is a let. Other lets are listed in the Laws.", 4),
            rtt("Expedite", "If a game is too slow, expedite system rules can apply as written in the Laws.", 5),
            rtt("Winning conditions", "First to win the required number of games wins the match.", 6),
        ],
        "fouls": [
            ("Illegal serve", "violation", "Toss, hiding, or bounce-order faults."),
            ("Volley", "violation", "Striking the ball before it bounces on your side (except as the Laws allow in specific cases)."),
        ],
        "equipment": [
            ("Blade and rubber", "Racket covering must comply with ITTF approval for sanctioned events.", "Colours of the two sides are regulated (typically red and black).", "Do not use damaged rubber that could detach."),
            ("Ball", "Seamless polymer ball; 40+ mm is the current standard size used in ITTF events.", "Plastic 40+ replaced celluloid.", "Discard cracked balls."),
            ("Table and net", "2.74 × 1.525 m, 76 cm high; net 15.25 cm.", "Friction and bounce should be consistent.", "Secure wheels on rollaway tables so they cannot collapse."),
        ],
        "techniques": [
            tech("Serve", "Backspin, sidespin, and no-spin serves from a legal toss.", ["Open palm toss.", "Contact with a consistent brush or hit.", "Recover to a ready position."], "Practice a legal toss before adding heavy spin.", "Hiding the ball with the arm or shoulder — illegal in ITTF Laws.", "Ensure the toss cannot hit a nearby player.", 1),
            tech("Forehand drive", "A topspin attacking stroke.", ["Rotate the hips.", "Brush up and forward.", "Land the ball with depth."], "Start against a robot or consistent multi-ball feed.", "Wrist-only flicks with no legs.", "Give table corners space; do not crash into barriers at full speed until ready.", 2),
            tech("Push", "A backspin control shot, often short.", ["Angle the bat.", "Contact under the ball.", "Keep it low over the net."], "Learn to read backspin before looping everything.", "Popping the ball up; pushing every ball the same.", "Do not lean so far that you collide with the table edge.", 3),
        ],
        "safety": [("Table edges", "equipment", "Watch sharp corners. Secure folding tables in the open position.")],
        "terms": [
            ("Serve", "The stroke that starts the rally, with toss and bounce requirements."),
            ("Loop", "A heavy topspin attacking stroke."),
            ("Chop", "A defensive backspin stroke, often from farther back."),
            ("Let", "A rally that does not score, including some net serves."),
        ],
        "faqs": [("Why 11 points?", "ITTF changed from 21-point games to 11-point rally scoring in 2001. Recreational groups may still play older scoring by agreement.")],
        "references": [(ITTF, "Laws of Table Tennis (ITTF Statutes)", "Current edition — ittf.com", "https://www.ittf.com", "Racket covering lists and ball approvals are updated separately.")],
    }
)

WA = "World Aquatics (formerly FINA)"
WA_ED = "Consult the current World Aquatics Competition Regulations"
rsw = _fb(OFF, WA, WA_ED)
add(
    {
        "slug": "swimming",
        "name": "Swimming",
        "tagline": "Racing and skill swimming in pool or open water, using recognised strokes.",
        "overview": "Competitive pool swimming includes freestyle, backstroke, breaststroke, butterfly, individual medley, and relays. World Aquatics publishes competition regulations. Recreational swimming is also a life skill. Water safety and qualified supervision are essential.",
        "history": "Organised swimming competitions expanded in the 19th century. FINA was founded in 1908 and rebranded as World Aquatics. Swimming has been on the Olympic programme since 1896 with evolving stroke rules.",
        "player_count": "Pool racing is individual or relay (typically four swimmers). Water polo, artistic swimming, and diving are separate aquatic disciplines.",
        "court_dimensions": "Olympic pool: 50 m long (long course). Short course: 25 m. World Aquatics specifies lane width, depth recommendations, and timing equipment for sanctioned events. Many community pools differ.",
        "scoring_system": "Races are decided by time (or finish order). False starts are governed by the one-start rule in many World Aquatics events. Relays have takeover rules. Open-water events have their own field-of-play and feeding rules.",
        "governing_org": WA,
        "featured": True,
        "popular": True,
        "icon": "pool",
        "accent_color": "#0077B6",
        "categories": ["water-sports", "individual-sports"],
        "positions": [
            ("Freestyle specialist", "Usually swims front crawl in freestyle events."),
            ("Stroke specialist", "Focuses on backstroke, breaststroke, or butterfly."),
            ("IM swimmer", "Competes in individual medley: fly, back, breast, free in that order."),
            ("Relay lead / anchor", "Starts or finishes a relay; takeover timing is critical."),
        ],
        "rules": [
            rsw("Strokes", "Each stroke has legal kick, arm, and turning requirements. Breaststroke and butterfly are especially technical in the rulebook. Officials judge legality.", 1),
            rsw("Starts", "Forward starts from blocks for free, breast, fly, and IM; backstroke starts in the water. False-start policy is specified in the regulations.", 2),
            rsw("Turns and finishes", "Touch requirements differ by stroke (two-hand touches for breast and fly in standard rules). Backstroke finishes and turning flags are official-rule items.", 3),
            rsw("Lanes", "Swimmers must remain in their lane. Interference can lead to disqualification.", 4),
            rsw("Relays", "Early takeovers are judged by timing pads and officials. Exchange technique should be practiced with a coach.", 5),
            rsw("Winning conditions", "Fastest legal time wins. Dead-heat policies are in the regulations.", 6),
        ],
        "fouls": [
            ("False start", "violation", "Leaving early, subject to the event’s start rule."),
            ("Stroke infraction", "violation", "Illegal kick, pull, or turn for that stroke."),
            ("Early takeover", "violation", "Relay swimmer leaves before the incoming touch."),
        ],
        "equipment": [
            ("Swimsuit", "Must meet coverage and fabric rules in sanctioned events (including World Aquatics approvals for elite tech suits).", "Club training suits differ from race suits.", "Do not dive in ill-fitting gear that can slip."),
            ("Cap and goggles", "Reduce drag and protect eyes.", "Anti-fog goggles should fit the eye socket without extreme tightness.", "Practice removing goggles if they flood; never swim with broken glass lenses."),
            ("Starting block", "Used for forward starts in competition.", "Height and track-start wedges are specified for elite pools.", "Do not play on blocks. Only dive where depth is known and supervision is present."),
            ("Lane ropes", "Reduce waves and mark lanes.", "Wave-eating designs in competition pools.", "Do not hang on lane ropes during sprint sets if it endangers others."),
        ],
        "techniques": [
            tech("Freestyle (front crawl)", "Alternating arms with a flutter kick, breathing to the side.", ["Horizontal body.", "High elbow recovery as coached.", "Rotate to breathe without lifting the head straight up.", "Steady kick."], "Learn side breathing in a shallow teaching area first.", "Crossing the centre line with the pull; holding the breath too long.", "Never swim alone. Know the depth. No diving into shallow water.", 1),
            tech("Backstroke", "Supine flutter kick with alternating arms.", ["Hips up.", "Straight-line head.", "Continuous kick.", "Use flags to judge the wall."], "Count strokes from the flags to the wall.", "Sitting in the water; looking at the feet.", "Be aware of walls and other swimmers when on your back.", 2),
            tech("Breaststroke", "Legal whip kick and simultaneous arm pull with a glide phase as taught.", ["Set up the kick with feet turned out.", "Shoot the arms forward.", "Time the breath with the pull.", "Glide briefly."], "A coach should check kick legality early.", "Scissors kick; dropping the hips.", "Breaststroke kick can stress knees; stop if the inner knee hurts sharply.", 3),
            tech("Butterfly", "Undulating stroke with a dolphin kick and simultaneous arms.", ["Chest press initiates the wave.", "Kick twice per cycle as commonly taught.", "Recover arms low over the water.", "Breathe forward without lifting too high."], "Learn dolphin kick on its own before full stroke.", "Too much undulation; pausing the kick.", "This is a demanding stroke. Build volume gradually under coaching.", 4),
        ],
        "safety": [
            ("Supervision", "supervision", "Children and weak swimmers need constant qualified supervision. Fences, lifeguards, and depth markings save lives."),
            ("Depth and diving", "safety", "Feet-first entry unless the depth is confirmed safe for diving and a supervisor allows it."),
        ],
        "terms": [
            ("Freestyle", "In competition, any stroke may be used in a freestyle event; front crawl is usual."),
            ("IM", "Individual medley: butterfly, backstroke, breaststroke, freestyle in that order."),
            ("Split", "A segment time, such as 50 m splits in a 200 m race."),
            ("DQ", "Disqualification for a rule infraction."),
        ],
        "faqs": [
            ("Can I swim alone if I am experienced?", "Even strong swimmers can have medical events. Swim where there is supervision or a buddy. This site cannot assess your risk."),
            ("Are tech suits required?", "No. They are regulated in elite racing and unnecessary for most learners."),
        ],
        "references": [
            (WA, "World Aquatics Competition Regulations (Swimming)", "Current edition — worldaquatics.com", "https://www.worldaquatics.com", "Open water, artistic swimming, water polo, and diving have separate sections."),
        ],
    }
)

WA_ATH = "World Athletics"
WA_ATH_ED = "Consult the current World Athletics Technical Rules"
ra = _fb(OFF, WA_ATH, WA_ATH_ED)
add(
    {
        "slug": "athletics",
        "name": "Athletics",
        "tagline": "Track and field: running, jumping, throwing, and combined events.",
        "overview": "Athletics includes sprints, middle and long distance, hurdles, relays, jumps, throws, race walking, and combined events (heptathlon/decathlon). World Athletics publishes technical rules. School events may use simplified or national-association rules.",
        "history": "Track and field has ancient Olympic roots and a modern revival from the late 19th century. World Athletics (formerly IAAF, founded 1912) is the international governing body.",
        "player_count": "Most events are individual. Relays use teams (commonly 4). Combined events accumulate points across multiple disciplines.",
        "court_dimensions": "A standard outdoor running track is 400 m in lane 1. Field event runways, circles, and landing areas have World Athletics specifications. Indoor tracks are often 200 m.",
        "scoring_system": "Running events: fastest legal time. Jumps and throws: best valid mark, with attempt allotments. Combined events: points tables published by World Athletics.",
        "governing_org": WA_ATH,
        "featured": True,
        "popular": True,
        "icon": "directions_run",
        "accent_color": "#D62828",
        "categories": ["athletics", "individual-sports", "outdoor-sports"],
        "positions": [
            ("Sprinter", "Competes in 100–400 m and related relays/hurdles."),
            ("Distance runner", "800 m and longer, including steeplechase and road events."),
            ("Jumper", "High jump, pole vault, long jump, or triple jump."),
            ("Thrower", "Shot, discus, hammer, or javelin."),
        ],
        "rules": [
            ra("False starts", "World Athletics uses a one-false-start disqualification rule in many elite competitions. Youth or school rules may differ — confirm locally.", 1),
            ra("Lane running", "Some events require staying in lane. Running on the inside line can be measured as a lane violation.", 2),
            ra("Relay zones", "Baton must be passed within the takeover zone. Acceleration zones exist as specified.", 3),
            ra("Field attempts", "Each event defines a number of trials, time allowed to start an attempt, and what constitutes a foul (for example, beyond the take-off board in long jump).", 4),
            ra("Implements", "Weight and specification of throwing implements vary by age and gender groups as published in the rules.", 5),
            ra("Winning conditions", "Best legal performance wins. Ties have event-specific tie-break procedures.", 6),
        ],
        "fouls": [
            ("False start", "violation", "Leaving the blocks early under the competition’s start rule."),
            ("Foot fault / no-jump", "violation", "Take-off beyond the board or other jump fouls."),
            ("Sector foul", "violation", "Throw landing outside the landing sector."),
        ],
        "equipment": [
            ("Spikes", "Event-specific shoes; spike length is regulated by surface and World Athletics/school rules.", "Do not use long spikes on surfaces that forbid them.", "Spike plates can injure; walk carefully off the track."),
            ("Starting blocks", "Used in sprint starts.", "Must be set in the lane without obstructing others.", "Do not leave blocks on the track."),
            ("Throwing implements", "Shot, discus, javelin, hammer meeting weight specs.", "Certified implements for competition.", "Never throw without a clear sector and supervision."),
            ("Landing mats / pits", "Protect jumpers.", "Pole vault and high jump mats must meet competition specs at sanctioned meets.", "Do not jump if mats are insufficient."),
        ],
        "techniques": [
            tech("Sprint start", "Block start and drive phase.", ["Set blocks with a coach.", "Brace the arms.", "Drive low, then rise gradually."], "Practice without blocks first.", "Standing up instantly; false-starting from nerves.", "Only use blocks on a proper track with instruction.", 1),
            tech("Relay baton pass", "Incoming and outgoing runners matching speed in the zone.", ["Outgoing runner starts on cue.", "Hand/target as coached (upsweep/downsweep).", "Do not look back in visual-pass sprints unless coached to."], "Walk-through the zone many times.", "Leaving too early; slowing to pass.", "Drop drills should not be done in live traffic lanes.", 2),
            tech("Long jump approach", "Controlled run-up and take-off near the board.", ["Consistent stride pattern.", "Penultimate stride preparation.", "Take off and land in the pit."], "Measure the run-up. Do not move the board mark casually.", "Fouling by overreaching on the last step.", "Pits must be raked and deep enough. No jumping into shallow sand.", 3),
        ],
        "safety": [("Throwing sector", "supervision", "Throwing events require a closed sector, officials, and no crossing behind the thrower.")],
        "terms": [
            ("Personal best (PB)", "An athlete’s best legal mark."),
            ("False start", "An illegal start."),
            ("Foul", "An invalid field-event attempt."),
            ("Split", "An intermediate time."),
        ],
        "faqs": [("Do school meets use World Athletics rules?", "Often a national schools association rulebook is used. Ask the meet director.")],
        "references": [(WA_ATH, "World Athletics Technical Rules", "Current edition — worldathletics.org", "https://worldathletics.org", "Competition and advertising rules are separate documents.")],
    }
)
