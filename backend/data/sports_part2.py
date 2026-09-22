from .sports_part1 import CATEGORIES, GENERAL_SAFETY, SPORTS, add, tech, _fb, DISCLAIMER, OFF, EDU

FIFA = "Fédération Internationale de Football Association (FIFA)"
FIFA_ED = "Consult the current IFAB Laws of the Game at theifab.com (IFAB writes the Laws; FIFA is a member)"
IFAB = "International Football Association Board (IFAB)"
rf = _fb(OFF, IFAB, FIFA_ED)

add(
    {
        "slug": "football",
        "name": "Football",
        "tagline": "The world’s most played 11-a-side game, governed by the IFAB Laws of the Game.",
        "overview": (
            "Association football (soccer) is a field sport in which two teams try to put the ball into the opponent’s goal "
            "without using hands or arms, except for the goalkeeper in their penalty area. Recreational formats may use smaller "
            "sides. This page is educational; match officials apply the IFAB Laws of the Game and competition regulations."
        ),
        "history": (
            "Modern association football was codified in England in the 19th century. FIFA was founded in 1904. The Laws of the Game "
            "are maintained by The IFAB. The FIFA World Cup began in 1930. Women’s World Cup competition began in 1991."
        ),
        "player_count": "Eleven players per team on the field of play, including a goalkeeper, in standard 11-a-side. Substitutes are listed on the team sheet according to competition rules.",
        "court_dimensions": "The IFAB Laws specify a rectangular field with ranges for length and width, plus penalty area, goal area, centre circle, and goal sizes. Professional pitches are often about 105 m × 68 m, but the Laws allow a range. Confirm the venue.",
        "scoring_system": "A goal is scored when the whole of the ball passes over the goal line, between the posts and under the bar, provided no offence was committed by the scoring team. The team scoring more goals wins. Competition rules cover extra time and kicks from the penalty mark.",
        "governing_org": FIFA,
        "featured": True,
        "popular": True,
        "icon": "sports_soccer",
        "accent_color": "#2A9D8F",
        "categories": ["team-sports", "outdoor-sports"],
        "positions": [
            ("Goalkeeper", "The only player who may handle the ball in their own penalty area, subject to the Laws."),
            ("Centre-back", "A central defender protecting the penalty area."),
            ("Full-back / wing-back", "A wide defender who may also support attack."),
            ("Central midfielder", "Links defense and attack; roles vary by formation."),
            ("Winger", "A wide attacker providing width and crosses or inside runs."),
            ("Striker / centre-forward", "A primary goal-scoring forward."),
        ],
        "rules": [
            rf("Players", "A match is played by two teams, each with not more than eleven players including a goalkeeper. A match may not start or continue if either team has fewer than seven players, according to the Laws.", 1),
            rf("Duration", "A standard match is two equal halves of 45 minutes, plus allowance for time lost. Competition rules may specify different durations for youth or futsal-style events — those are separate codes.", 2),
            rf("Scoring", "A goal is scored when the whole ball crosses the goal line between the posts and under the crossbar, with no offence by the scoring team.", 3),
            rf("Ball in and out of play", "The ball is out of play when it has wholly crossed the goal line or touchline, or when the referee has stopped play.", 4),
            rf("Offside", "A player in an offside position at the moment the ball is played by a teammate may be penalised only if involved in active play, as detailed in Law 11. This is one of the most interpretation-sensitive laws.", 5),
            rf("Fouls and misconduct", "Direct and indirect free kicks, penalty kicks, and disciplinary sanctions (yellow/red cards) are defined in Law 12. Careless, reckless, or excessive force distinctions matter.", 6),
            rf("Handling", "Deliberate hand/arm contact is an offence as defined in the current Law 12 wording, which has been revised in recent editions. Read the current IFAB text.", 7),
            rf("Restarts", "Kick-off, throw-in, goal kick, corner kick, dropped ball, free kick, and penalty kick each have placement and procedure rules.", 8),
            rf("Substitutions", "The number of substitutions and whether concussion substitutes are allowed depend on competition rules within the Laws’ framework.", 9),
            rf("Winning conditions", "The team scoring more goals wins. Draws may stand, or competitions may use extra time and/or kicks from the penalty mark.", 10),
        ],
        "fouls": [
            ("Offside", "violation", "Being involved in active play from an offside position when the ball is played by a teammate, as defined in Law 11."),
            ("Handling", "foul", "An illegal hand/arm contact as currently defined by IFAB."),
            ("Tripping / kicking", "foul", "Careless, reckless, or excessive contact offences in Law 12."),
            ("Advantage", "signal", "The referee may play advantage and signal accordingly."),
            ("Yellow / red card", "signal", "Cautions and send-offs are shown with cards."),
        ],
        "equipment": [
            ("Football", "The ball used for play.", "Size 5 is standard for adult 11-a-side; youth sizes 3–4 are common. Circumference and pressure are specified in the Laws.", "Do not use a ball that is waterlogged or dangerously under/over inflated."),
            ("Goals", "The target for scoring.", "Posts and crossbar dimensions are specified in the Laws.", "Anchor portable goals. Never climb on goals."),
            ("Shin guards", "Compulsory equipment for players.", "Must provide a reasonable degree of protection and be covered by socks, per the Laws.", "Use guards that actually cover the shin."),
            ("Boots", "Footwear with suitable studs or soles for the surface.", "Studs must not be dangerous.", "Match stud type to grass, turf, or indoor courts."),
            ("Uniform", "Shirt, shorts, socks; goalkeeper distinct colours.", "Numbers and advertising follow competition regulations.", "No jewellery if it is dangerous, as determined under the Laws."),
        ],
        "techniques": [
            tech("Passing", "Sending the ball to a teammate with the inside, outside, or laces of the foot.", ["Look up.", "Plant the non-kicking foot.", "Strike through the ball toward the target.", "Follow the pass into space when appropriate."], "Start with inside-foot short passes.", "Leaning back and lofting accidentally; passing to a marked teammate’s feet only.", "Do not practice full-power shots toward unprotected teammates at close range.", 1),
            tech("Dribbling", "Moving with close control of the ball.", ["Keep the ball within playing distance.", "Use both feet.", "Change pace and direction.", "Keep the head up between touches."], "Use cones at walking speed first.", "Kicking the ball too far ahead; looking only at the ball.", "Watch for other groups sharing the field.", 2),
            tech("Shooting", "Attempting to score with a controlled strike.", ["Square hips toward the target when possible.", "Strike the middle or upper half for a driven shot.", "Keep the head steady.", "Follow through toward the goal."], "Accuracy before power. Practice from 8–12 metres first.", "Leaning back; rushing the plant foot.", "Goalkeepers in shooting drills need proper gloves and awareness.", 3),
            tech("Receiving", "Controlling a pass with foot, thigh, or chest (not arm).", ["Move into the line of the ball.", "Cushion the first touch.", "Direct the ball into space away from pressure."], "Call for the ball. Take a touch that sets up the next action.", "Stopping the ball dead under pressure; using the arm to trap.", "Do not jump with raised elbows near an opponent’s head.", 4),
            tech("Defending", "Delaying, covering, and tackling within the Laws.", ["Jockey rather than dive in.", "Show the attacker one way if coached to.", "Tackle the ball when you can play it.", "Recover toward the goal if beaten."], "Learn side-on stance and patience.", "Diving into tackles from behind; pulling shirts.", "Slide tackles belong in coached settings with clear rules. Avoid studs-up contact.", 5),
        ],
        "safety": [("Goal safety", "equipment", "Weighted or anchored goals only. Check for loose nets and broken posts.")],
        "terms": [
            ("Offside", "A Law 11 concept involving position and involvement in active play."),
            ("Advantage", "Allowing play to continue when a stoppage would punish the non-offending team."),
            ("Set piece", "A restart such as a free kick, corner, or throw-in."),
            ("Clean sheet", "Informal: a match without conceding a goal."),
            ("Through ball", "A pass into space behind the defensive line."),
        ],
        "faqs": [
            ("Why do some leagues use VAR?", "Video assistant referees are a competition tool described in IFAB protocols. Not all levels use them."),
            ("Is heading banned for children?", "Some national associations restrict heading in youth training. Follow your association’s guidance, not this site."),
        ],
        "references": [
            (IFAB, "Laws of the Game", "Current season edition — verify at theifab.com", "https://www.theifab.com", "The IFAB publishes the Laws. Competition regulations (substitutes, extra time) sit on top of the Laws."),
            (FIFA, "FIFA Laws and competition regulations", "See fifa.com", "https://www.fifa.com", "FIFA competitions apply IFAB Laws plus tournament regulations."),
        ],
    }
)

AMF_FIFA_FUTSAL = "FIFA (Futsal Laws of the Game)"
FUTSAL_ED = "Consult the current FIFA Futsal Laws of the Game"
rfu = _fb(OFF, AMF_FIFA_FUTSAL, FUTSAL_ED)
add(
    {
        "slug": "futsal",
        "name": "Futsal",
        "tagline": "Five-a-side indoor football with a low-bounce ball and unlimited rolling substitutes in many competitions.",
        "overview": "Futsal is the FIFA-coded indoor format of football played 5 vs 5 on a court. It emphasizes close control, quick combination play, and a distinct set of Laws from 11-a-side football.",
        "history": "Futsal developed in South America in the 1930s. FIFA later published dedicated Futsal Laws of the Game. The sport has world championships separate from 11-a-side football.",
        "player_count": "Five players per team on the court, including a goalkeeper. Flying goalkeepers and unlimited substitutions are features of the FIFA futsal Laws — confirm the current text.",
        "court_dimensions": "FIFA Futsal Laws specify a rectangular court with ranges for international and non-international matches, plus penalty marks and substitution zones. Recreational gym sizes vary.",
        "scoring_system": "A goal is scored when the whole ball crosses the goal line between the posts and under the bar, with no offence by the scoring team. Accumulated fouls can lead to direct free kicks without a wall, as defined in the Laws.",
        "governing_org": "FIFA",
        "featured": False,
        "popular": True,
        "icon": "sports_soccer",
        "accent_color": "#1D3557",
        "categories": ["team-sports"],
        "positions": [
            ("Goalkeeper", "May use hands in their own penalty area; can also join play as a fifth outfield player when the Laws allow."),
            ("Fixo (defender)", "Often a deeper court player in common tactical language."),
            ("Ala", "A wide or half-space midfielder/attacker in common tactical language."),
            ("Pivot", "A forward reference player, often with back to goal."),
        ],
        "rules": [
            rfu("Players", "Five players including a goalkeeper. Minimum numbers to continue are defined in the Futsal Laws.", 1),
            rfu("Duration", "Typically two equal periods (commonly 20 minutes stopped-clock at higher levels). Exact timing, timeouts, and kick-ins depend on the current Laws and competition.", 2),
            rfu("Kick-in", "When the ball crosses the touch line, play restarts with a kick-in, not a throw-in.", 3),
            rfu("Accumulated fouls", "After a set number of fouls in a period, further fouls can result in a direct free kick without a wall from the second penalty mark or as specified.", 4),
            rfu("Substitutions", "Rolling substitutions through the substitution zone are a hallmark of futsal. Procedure faults can be penalised.", 5),
            rfu("Back-pass to goalkeeper", "Restrictions on the goalkeeper handling a deliberate kick from a teammate exist similarly in spirit to outdoor football; read the futsal-specific wording.", 6),
            rfu("Winning conditions", "Most goals wins. Extra time and penalties follow competition rules.", 7),
        ],
        "fouls": [
            ("Kick-in fault", "violation", "Incorrect placement or delay on a kick-in."),
            ("Accumulated foul", "foul", "Counts toward the team total that can trigger a no-wall direct free kick."),
        ],
        "equipment": [
            ("Futsal ball", "Lower bounce than a size 5 outdoor ball.", "Size and bounce tests are specified in the Futsal Laws.", "Use a futsal ball on courts; outdoor balls bounce too high."),
            ("Court shoes", "Non-marking indoor shoes.", "Flat gum rubber typical.", "No metal studs indoors."),
            ("Shin guards", "Required as in football.", "Covered by socks.", "Must actually protect the shin."),
        ],
        "techniques": [
            tech("Sole control", "Stopping and dragging the ball with the sole.", ["Cushion with the sole.", "Keep the ball close.", "Drag into space away from pressure."], "Walk-through sole rolls before adding speed.", "Standing on the ball; losing vision.", "Keep heads up in crowded gyms.", 1),
            tech("Wall pass", "Quick combination off a teammate.", ["Pass and move.", "Give an angle.", "Play first time when the ball is clean."], "Start 3-player give-and-go drills.", "Passing into a teammate’s feet with a defender already there.", "Control indoor speed near walls.", 2),
        ],
        "safety": [("Indoor surfaces", "equipment", "Watch for wall proximity, basketball poles, and wet patches.")],
        "terms": [
            ("Kick-in", "Restart from the touch line with the foot."),
            ("Power play / flying goalkeeper", "Using the goalkeeper as an extra court player. Restrictions apply."),
            ("Pivot", "Tactical term for a reference forward."),
        ],
        "faqs": [("Is futsal the same as indoor soccer?", "No. Many ‘indoor soccer’ leagues use different balls, walls, and rules. FIFA futsal is a specific code.")],
        "references": [
            ("FIFA", "Futsal Laws of the Game", "Current edition — verify on fifa.com", "https://www.fifa.com", "Do not apply 11-a-side Laws unchanged to futsal."),
        ],
    }
)

BWF = "Badminton World Federation (BWF)"
BWF_ED = "Consult the current BWF Statutes, Section 4 – Laws of Badminton"
rbw = _fb(OFF, BWF, BWF_ED)
add(
    {
        "slug": "badminton",
        "name": "Badminton",
        "tagline": "A racquet sport played with a shuttlecock that must be struck before it hits the floor.",
        "overview": "Badminton is played in singles and doubles. Players hit a shuttlecock over a net so that it lands in the opponent’s court. Rally scoring is used under current BWF Laws.",
        "history": "The modern sport was codified in 19th-century England, with roots in earlier battledore and shuttlecock games. The BWF (formerly IBF) governs world badminton. It has been an Olympic sport since 1992.",
        "player_count": "Singles: one vs one. Doubles: two vs two. Mixed doubles pairs one man and one woman.",
        "court_dimensions": "BWF court is 13.40 m long. Width is 6.10 m for doubles and 5.18 m for singles. Net height is 1.55 m at the posts and 1.524 m at the centre. Service courts are marked separately for singles and doubles.",
        "scoring_system": "Rally point scoring to 21 points per game in standard BWF scoring, must win by 2 points, with a cap described in the Laws (commonly 30). Matches are typically best of three games. Confirm the current Laws and any para-badminton variations.",
        "governing_org": BWF,
        "featured": False,
        "popular": True,
        "icon": "sports_tennis",
        "accent_color": "#6A994E",
        "categories": ["racquet-sports", "individual-sports"],
        "positions": [
            ("Singles player", "Covers the full singles court."),
            ("Doubles front", "Often takes net interception after the serve/return in many systems."),
            ("Doubles back", "Often takes rearside attacking smash opportunities in many systems."),
        ],
        "rules": [
            rbw("Scoring", "A point is scored on every rally. Standard games are played to 21 with a two-point margin and a specified maximum. Best of three games is standard at elite level.", 1),
            rbw("Serve", "The serve must be hit in an upward direction, with additional limits on shuttle and racquet height at contact as written in the current Laws (service laws have been updated; read the current text). The server and receiver stand in diagonally opposite service courts.", 2),
            rbw("Service courts", "Singles and doubles use different service court widths. After the serve, players may hit from anywhere on their side.", 3),
            rbw("Faults", "The shuttle landing outside, failing to go over the net, a player touching the net, or hitting the shuttle twice are among faults. See Laws for the full list.", 4),
            rbw("Lets", "A let is called in listed situations, such as an unforeseen disturbance, and the rally is replayed.", 5),
            rbw("Winning conditions", "The first player or pair to win the required number of games wins the match.", 6),
        ],
        "fouls": [
            ("Service fault", "violation", "Serve not meeting height, direction, or court requirements."),
            ("Net fault", "violation", "Touching the net or invading the opponent’s court illegally."),
            ("Shuttle out", "violation", "Shuttle lands outside the designated court for that rally."),
        ],
        "equipment": [
            ("Racquet", "Used to hit the shuttle.", "Weight and string tension vary; there is no single mandatory racquet spec for recreation.", "Inspect for cracked frames. Eye protection is a personal/club choice especially in doubles."),
            ("Shuttlecock", "Feather or synthetic projectile.", "BWF events specify approved shuttles. Speed (pace) is chosen for temperature and altitude.", "Feather shuttles break; discard damaged shuttles that fly unpredictably."),
            ("Net", "Divides the court.", "1.55 m at posts, 1.524 m at centre per Laws.", "Secure posts. Do not lean on the net."),
            ("Non-marking shoes", "Indoor court traction.", "Gum rubber typical.", "No outdoor shoes on dedicated courts."),
        ],
        "techniques": [
            tech("Serve", "High serve, low serve, flick, and drive are common patterns.", ["Stand in the correct service court.", "Hit under the current height law.", "Direct the shuttle to the target service court.", "Recover to a ready stance."], "Start with a consistent low doubles serve and a high singles serve.", "Serving from the wrong court; rushing the toss.", "Do not serve until the receiver is ready in recreational play.", 1),
            tech("Clear", "A high shot to the back court.", ["Rotate the shoulders.", "Contact high.", "Finish the throwing action."], "Use clears to create time in singles.", "Contacting too low; under-hitting to mid-court.", "Watch for others behind the baseline when practicing clears.", 2),
            tech("Drop shot", "A steep or tumbling shot that falls just over the net.", ["Disguise with the same preparation as a clear.", "Slice or block as coached.", "Move forward after the shot."], "Practice from a full overhead action so it is not obvious.", "Telegraphing by stopping the swing early every time.", "Do not reach into the net.", 3),
            tech("Smash", "A steep downward attacking hit.", ["Scissor or jump only when landing space is clear.", "Hit down with rotation.", "Follow toward the net."], "Accuracy to the sidelines before maximum power.", "Smashes into the net; poor recovery.", "Land on both feet when possible. Stop if a landing feels unstable.", 4),
            tech("Net shot", "A tight tumbling shot at the net.", ["Lunge with a stable knee.", "Soft racquet face.", "Keep the head of the racquet above the tape when possible."], "Start from a still shuttle fed by a partner.", "Hitting the tape too hard; lunging past the net.", "Do not plant the knee violently on hard floors without progression.", 5),
        ],
        "safety": [("Court traffic", "technique", "Call the shuttle. Doubles partners should avoid racquet clashes at the centre.")],
        "terms": [
            ("Serve", "The stroke that starts the rally, with specific legality requirements."),
            ("Clear", "A high shot to the rear court."),
            ("Drop", "A shot that falls steeply just over the net."),
            ("Smash", "A downward attacking overhead."),
            ("Drive", "A flat, fast shot."),
            ("Let", "A replayed rally in listed circumstances."),
        ],
        "faqs": [("Why did service laws change?", "BWF introduced a fixed service height law for many events. Recreational clubs may still use older interpretations. Check your competition.")],
        "references": [(BWF, "Laws of Badminton", "Current BWF Statutes Section 4 — verify at corporate.bwfbadminton.com", "https://corporate.bwfbadminton.com", "Para-badminton and air badminton have related but separate documents.")],
    }
)
