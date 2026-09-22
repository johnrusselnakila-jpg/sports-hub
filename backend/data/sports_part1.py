from __future__ import annotations

DISCLAIMER = (
    "Educational summary only. Official playing rules are published by the listed "
    "governing organization and may differ by competition, age group, and edition. "
    "Always confirm the current official rulebook before officiating or competing."
)

EDU = "educational"
OFF = "official_summary"
TRAIN = "training"
SAFE = "safety"


def rule(title, content, source, edition, order, kind=OFF):
    return {
        "title": title,
        "content": f"{content}\n\n{DISCLAIMER}",
        "content_type": kind,
        "source_org": source,
        "rule_edition": edition,
        "sort_order": order,
    }


def tech(name, description, steps, tips, mistakes, safety, order):
    return {
        "name": name,
        "description": description,
        "steps": steps,
        "beginner_tips": tips,
        "common_mistakes": mistakes,
        "safety_reminders": safety,
        "sort_order": order,
    }


CATEGORIES = [
    {
        "slug": "team-sports",
        "name": "Team Sports",
        "description": "Sports played by organized sides working toward a shared score.",
        "icon": "groups",
    },
    {
        "slug": "individual-sports",
        "name": "Individual Sports",
        "description": "Sports where athletes primarily compete as individuals.",
        "icon": "person",
    },
    {
        "slug": "combat-sports",
        "name": "Combat Sports",
        "description": "Striking and martial arts sports with strict safety rules.",
        "icon": "sports_mma",
    },
    {
        "slug": "water-sports",
        "name": "Water Sports",
        "description": "Sports performed in or on water.",
        "icon": "pool",
    },
    {
        "slug": "racquet-sports",
        "name": "Racquet Sports",
        "description": "Sports played with a racquet, paddle, or similar implement.",
        "icon": "sports_tennis",
    },
    {
        "slug": "athletics",
        "name": "Athletics",
        "description": "Track and field running, jumping, and throwing events.",
        "icon": "directions_run",
    },
    {
        "slug": "outdoor-sports",
        "name": "Outdoor Sports",
        "description": "Sports commonly played outdoors or across varied terrain.",
        "icon": "terrain",
    },
]

GENERAL_SAFETY = [
    {
        "title": "Warm-up",
        "topic": "warm-up",
        "content": (
            "A general warm-up raises heart rate and prepares muscles and joints for activity. "
            "Typical sessions include light aerobic movement and mobility work for the body parts "
            "used in the sport. Warm-up length and intensity should match the session and the individual."
        ),
        "sort_order": 1,
    },
    {
        "title": "Cool-down",
        "topic": "cool-down",
        "content": (
            "A cool-down gradually reduces intensity after training or competition. Light movement "
            "and easy stretching are commonly used. This is educational guidance, not a medical protocol."
        ),
        "sort_order": 2,
    },
    {
        "title": "Proper equipment",
        "topic": "equipment",
        "content": (
            "Use equipment that fits, is in good condition, and matches the sport and playing surface. "
            "Protective gear should be worn as required by the activity and local rules. Replace damaged items."
        ),
        "sort_order": 3,
    },
    {
        "title": "Hydration",
        "topic": "hydration",
        "content": (
            "Drink fluids before, during, and after activity according to thirst, climate, and session length. "
            "Needs vary widely. People with medical conditions should follow advice from a qualified clinician."
        ),
        "sort_order": 4,
    },
    {
        "title": "Rest",
        "topic": "rest",
        "content": (
            "Rest and sleep support recovery. Sudden large increases in training load can raise injury risk. "
            "Plan rest days and listen to persistent pain rather than training through it."
        ),
        "sort_order": 5,
    },
    {
        "title": "Proper technique",
        "topic": "technique",
        "content": (
            "Sound technique reduces unnecessary strain. Learn skills from a qualified coach when possible. "
            "Training suggestions on this site are beginner-oriented and do not replace in-person coaching."
        ),
        "sort_order": 6,
    },
    {
        "title": "Recognizing injuries",
        "topic": "injuries",
        "content": (
            "Stop activity and seek appropriate care for chest pain, breathing difficulty, suspected concussion, "
            "uncontrolled bleeding, joint deformity, or pain that is sudden and severe. This is not a diagnosis tool."
        ),
        "sort_order": 7,
    },
    {
        "title": "When to stop playing",
        "topic": "stop",
        "content": (
            "Stop if you cannot move with control, feel dizzy, are unusually short of breath, or have pain that "
            "worsens with continued play. Returning too soon after injury can make it worse."
        ),
        "sort_order": 8,
    },
    {
        "title": "Qualified supervision",
        "topic": "supervision",
        "content": (
            "Children, beginners, and contact-sport athletes benefit from qualified coaching and appropriate "
            "officiating. Combat sports and swimming require trained supervision and venue safety procedures."
        ),
        "sort_order": 9,
    },
]


def _fb(kind, src, ed):
    def inner(title, content, order):
        return rule(title, content, src, ed, order, kind)

    return inner


SPORTS = []


def add(sport: dict) -> None:
    SPORTS.append(sport)


# --- Basketball ---
FIBA = "International Basketball Federation (FIBA)"
FIBA_ED = "Consult the current FIBA Official Basketball Rules at fiba.basketball"
rb = _fb(OFF, FIBA, FIBA_ED)
add(
    {
        "slug": "basketball",
        "name": "Basketball",
        "tagline": "A five-a-side game of passing, dribbling, and shooting at a raised hoop.",
        "overview": (
            "Basketball is a team sport in which two sides score by sending a ball through the opponent’s basket. "
            "Play combines running, jumping, passing, and shooting. This page explains commonly taught concepts "
            "for athletes, coaches, students, and beginners. Competition rules are set by the relevant governing body."
        ),
        "history": (
            "Basketball was created by James Naismith in 1891 in Springfield, Massachusetts, as an indoor activity "
            "using peach baskets. The sport spread through schools and clubs, then internationally. FIBA was formed "
            "in 1932 to govern international competition. Olympic basketball began in 1936 for men and 1976 for women."
        ),
        "player_count": (
            "International 5-on-5 basketball uses five players per team on the court, with substitutes on the bench. "
            "Other formats exist, including 3x3. Exact roster size depends on the competition."
        ),
        "court_dimensions": (
            "FIBA published court size for full 5-on-5 play is 28 metres long by 15 metres wide. The basket ring is "
            "3.05 metres above the floor. National high-school or recreational courts may differ. Confirm the venue spec "
            "for your league."
        ),
        "scoring_system": (
            "A field goal from outside the three-point line is worth 3 points, other field goals 2 points, and a free "
            "throw 1 point in standard 5-on-5 basketball. 3x3 uses a different scoring scale. Always check the event rules."
        ),
        "governing_org": FIBA,
        "featured": True,
        "popular": True,
        "icon": "sports_basketball",
        "accent_color": "#E85D04",
        "categories": ["team-sports"],
        "positions": [
            ("Point guard", "Often organizes the offense and handles the ball in the backcourt."),
            ("Shooting guard", "A perimeter player who typically looks for scoring chances off the catch or dribble."),
            ("Small forward", "A versatile wing who may score, defend, and rebound."),
            ("Power forward", "Usually plays closer to the basket, screening, rebounding, and scoring inside or at mid-range."),
            ("Center", "Typically the tallest player, defending the paint and finishing near the rim."),
        ],
        "rules": [
            rb("Players", "Each team has five players on the court in standard 5-on-5. Substitutions are made according to the competition’s substitution procedure.", 1),
            rb("Game duration", "FIBA 5-on-5 games are commonly organized as four quarters. Playing time, extra periods, and shot-clock length are defined in the official rules and can differ for age groups and 3x3.", 2),
            rb("Scoring", "Points are awarded for successful field goals and free throws. The value of a shot depends on where it was taken and whether it was a free throw.", 3),
            rb("Dribbling", "A player who is holding a live ball on the court must dribble in order to move with the ball, subject to traveling, double-dribble, and carrying restrictions in the official rules.", 4),
            rb("Traveling", "Traveling is an illegal movement of the pivot foot or taking steps without dribbling as defined by the rulebook. Exact pivot-foot interpretations are official-rule matters and can vary slightly by organization.", 5),
            rb("Fouls", "Personal fouls involve illegal contact. Team foul penalties, bonus free throws, unsportsmanlike/disqualifying fouls, and technical fouls are administered as written in the competition rules.", 6),
            rb("Substitutions", "Players enter and leave through the designated procedure, usually after the officials grant a substitution. Live-ball substitutions are not allowed in standard 5-on-5.", 7),
            rb("Timeouts", "Each team is allotted timeouts as specified by the competition. Timeout length and when they may be requested are official-rule items.", 8),
            rb("Violations", "Violations include traveling, double dribble, carrying, three-second, five-second, eight-second, and shot-clock violations, among others listed in the official rules. The usual result is a throw-in for the opponents.", 9),
            rb("Winning conditions", "The team with more points at the end of playing time wins. Tied games are typically resolved by extra periods, except where a competition specifies otherwise.", 10),
        ],
        "fouls": [
            ("Traveling", "violation", "Moving illegally with the ball without a legal dribble, as defined by the applicable rulebook."),
            ("Double dribble", "violation", "Ending a dribble and then starting another, or dribbling with two hands, as defined by the rules."),
            ("Carrying / palming", "violation", "Placing the hand under the ball and carrying it during the dribble in a way the rules prohibit."),
            ("Personal foul", "foul", "Illegal contact on an opponent. Penalties depend on whether the player was in the act of shooting and on team foul totals."),
            ("Charging", "foul", "An offensive player causing illegal contact with a legally set defender."),
            ("Blocking", "foul", "A defender causing illegal contact while not in a legal guarding position."),
            ("Technical foul", "foul", "A foul related to behaviour or remaining in the game procedure rather than play contact. Penalties are specified by the official rules."),
            ("Stop clock / timeout signal", "signal", "Officials use standardized signals for scoring, fouls, violations, and time-outs. Learn the current FIBA or local association signal chart."),
        ],
        "equipment": [
            ("Basketball", "The ball used to score and pass.", "FIBA men’s size 7 and women’s size 6 are common international sizes; youth sizes differ. Confirm the competition specification.", "Use a ball in good condition with adequate grip. Do not play with a severely worn or over-inflated ball."),
            ("Basketball hoop", "The target through which points are scored.", "Ring 3.05 m above the floor in standard 5-on-5; 3x3 and mini-basketball may differ.", "Ensure the ring and net are securely mounted."),
            ("Backboard", "Supports the ring and is used for bank shots.", "Transparent rectangular backboards are standard in many competitions.", "Stay clear of the support structure during play."),
            ("Basketball court", "The playing area with boundary lines, key, and three-point line.", "FIBA 5-on-5: 28 m × 15 m is the published full-size court.", "Keep the surface dry and free of obstacles."),
            ("Player shoes", "Provide traction and support for cutting and jumping.", "Court shoes with non-marking soles are typical indoors.", "Replace shoes with worn outsoles to reduce slipping."),
            ("Uniform", "Identifies team and number.", "Jersey and shorts meeting competition colour and number rules.", "Wear numbers assigned by the team; remove jewellery if required by the rules."),
        ],
        "techniques": [
            tech(
                "Dribbling",
                "Bouncing the ball with one hand to move while in possession.",
                ["Keep the head up.", "Push the ball with the pads of the fingers.", "Protect the ball with the body when a defender is close.", "Change hands and pace to keep control."],
                "Start stationary, then add walking and jogging. Practice both hands.",
                "Watching the ball the entire time; slapping at the ball; traveling as you start.",
                "Do not dribble into other groups in a crowded gym. Wear court-appropriate shoes.",
                1,
            ),
            tech(
                "Passing",
                "Sending the ball to a teammate with a chest, bounce, or overhead pass.",
                ["See the target.", "Step toward the receiver.", "Finish with thumbs down or toward the target depending on the pass.", "Follow the pass with your eyes."],
                "Use a bounce pass when a defender’s hands are high.",
                "Telegraphing every pass; passing to a covered teammate.",
                "Avoid throwing at a teammate’s face or into traffic at full speed until control is consistent.",
                2,
            ),
            tech(
                "Shooting",
                "Sending the ball toward the basket with a balanced shooting motion.",
                ["Square up or use a consistent stance.", "Elbow under the ball.", "Extend toward the target and finish with a relaxed wrist.", "Hold the follow-through."],
                "Start close to the basket. Form matters more than range at first.",
                "Fading off-balance; pushing with two hands equally; no follow-through.",
                "Do not shoot while landing on another player’s foot. Space the court in practice.",
                3,
            ),
            tech(
                "Layups",
                "A close-range shot usually off one foot after a dribble or gather.",
                ["Approach at a controlled angle.", "Pick up the ball with a legal gather.", "Take the allowed steps as taught for your rule set.", "Lay the ball off the backboard or over the front of the rim."],
                "Practice from both sides. Use the backboard square as a target.",
                "Taking extra steps; jumping off the wrong foot; rushing under traffic.",
                "Do not jump into a defender who is already set. Teach legal gather steps with a coach.",
                4,
            ),
            tech(
                "Defense",
                "Guarding an opponent to prevent easy catches, drives, and shots.",
                ["Stay between the opponent and the basket when on-ball.", "Keep a balanced stance.", "Move the feet rather than reaching first.", "See ball and your player."],
                "Slide laterally in short drills before adding full-speed 1-on-1.",
                "Reaching for steals off-balance; standing upright; ball-watching.",
                "Do not undercut a shooter in the air. Play the ball legally.",
                5,
            ),
            tech(
                "Rebounding",
                "Securing the ball after a missed shot.",
                ["Find an opponent and establish position without pushing through the back.", "Jump through the ball.", "Chin the ball and pivot to outlet."],
                "Assume every shot will miss. Box out before looking for the ball.",
                "Watching the ball without contacting an opponent legally; bringing the ball down loosely.",
                "Land in control. Do not climb over a player’s back.",
                6,
            ),
        ],
        "safety": [
            ("Court safety", "equipment", "Check that baskets are padded as required, the floor is dry, and unused balls are off the court."),
            ("Landing space", "technique", "Give shooters and rebounders room to land. Under-cutting a jumping player is dangerous."),
        ],
        "terms": [
            ("Traveling", "A violation involving illegal movement of the pivot foot or steps without a legal dribble, as defined by the applicable rules."),
            ("Double dribble", "Starting a second dribble after ending the first, or dribbling with two hands."),
            ("Key / paint", "The restricted area near the basket, also called the lane."),
            ("Shot clock", "The time a team has to attempt a shot that hits the ring, as set by the competition."),
            ("Assist", "A pass that leads directly to a made field goal, in common statistical usage."),
            ("Fast break", "A quick offensive attack before the defense is set."),
            ("Man-to-man", "A team defense in which players primarily guard assigned opponents."),
            ("Zone", "A team defense in which players guard areas."),
        ],
        "faqs": [
            ("How many players are on the court?", "Five per team in standard 5-on-5. 3x3 uses three per team."),
            ("Is traveling the same in every league?", "The concept is similar, but interpretations and wording differ among FIBA, NBA, WNBA, NCAA, and school associations. Use your competition’s rulebook."),
            ("What is the three-point line?", "A arc beyond which a made field goal is worth three points in 5-on-5. Distance differs by organization and age group."),
        ],
        "references": [
            (FIBA, "Official Basketball Rules", "Current edition — verify year on fiba.basketball", "https://www.fiba.basketball", "Use the edition adopted by your event. Do not treat this website as the rulebook."),
            (FIBA, "3x3 Official Rules", "Current edition", "https://fiba3x3.com", "3x3 scoring and timing differ from 5-on-5."),
        ],
    }
)

# --- Volleyball ---
FIVB = "Fédération Internationale de Volleyball (FIVB)"
FIVB_ED = "Consult the current FIVB Official Volleyball Rules at fivb.com"
rv = _fb(OFF, FIVB, FIVB_ED)
add(
    {
        "slug": "volleyball",
        "name": "Volleyball",
        "tagline": "Six players a side, three contacts, and a ball that cannot rest in the hands.",
        "overview": (
            "Volleyball is a net sport in which teams send the ball over the net so that it lands on the opponent’s court "
            "or cannot be returned legally. Indoor volleyball is typically 6 vs 6. Beach volleyball is 2 vs 2 with different rules."
        ),
        "history": (
            "William G. Morgan created volleyball (originally Mintonette) in 1895 in Massachusetts. The FIVB was founded in 1947. "
            "Indoor volleyball became an Olympic sport in 1964; beach volleyball was added in 1996."
        ),
        "player_count": "Indoor: six players on court per team, plus substitutes according to the competition. Beach: two players per team with no substitutions in standard FIVB beach play.",
        "court_dimensions": "Indoor FIVB court is 18 m × 9 m, divided by a net. Antennae mark the crossing space. Net height differs for men, women, and some age groups. Confirm the event spec.",
        "scoring_system": "Rally scoring is used in current FIVB indoor rules: a point is scored on every rally. Matches are commonly best of five sets, with set point totals defined in the official rules (including a possible fifth set to a lower number).",
        "governing_org": FIVB,
        "featured": True,
        "popular": True,
        "icon": "sports_volleyball",
        "accent_color": "#F4A261",
        "categories": ["team-sports"],
        "positions": [
            ("Setter", "Runs the offense and usually delivers the attacking pass (the set)."),
            ("Outside hitter", "Attacks mainly from the left side; often a primary passer."),
            ("Opposite", "Attacks from the right side; may also set in some systems."),
            ("Middle blocker", "Blocks in the middle and attacks quick sets."),
            ("Libero", "A defensive specialist with substitution and attacking restrictions defined in the rules."),
            ("Defensive specialist", "A back-row defender who is not a libero."),
        ],
        "rules": [
            rv("Players", "Six players occupy rotational positions. Serving order and rotation faults are defined in the official rules. The libero has unique substitution clothing and playing restrictions.", 1),
            rv("Scoring and sets", "Rally point scoring. Most indoor matches are best of five. The exact points required to win a set and the two-point margin are in the current FIVB rules.", 2),
            rv("Contacts", "A team is allowed up to three contacts to return the ball, with blocking exceptions described in the rules. Consecutive contacts by the same player are restricted except in listed cases (for example some first contacts).", 3),
            rv("Serve", "The serve puts the ball in play from the service zone. Foot faults, screening, and toss rules are official-rule items. Let serves that touch the net may remain in play under current indoor rules — confirm the edition in use.", 4),
            rv("Net play", "Players may not touch the net in a way that interferes, as defined by the rules. Reaching beyond the net is limited, especially when blocking or attacking.", 5),
            rv("Rotation", "After winning the right to serve, indoor teams rotate clockwise. Being out of rotational order is a fault.", 6),
            rv("Libero", "The libero cannot complete an attack hit from anywhere if the ball is entirely above net height at contact, among other restrictions. See the official text.", 7),
            rv("Substitutions", "The number and procedure for substitutions are limited by the competition rules.", 8),
            rv("Faults", "Four hits, double contact (when not allowed), catch/throw, net faults, attack-line faults for back-row players, and service faults are among common violations.", 9),
            rv("Winning conditions", "A team wins the match by winning the required number of sets. Default formats can differ for pool play or timed recreational games.", 10),
        ],
        "fouls": [
            ("Four hits", "violation", "The team contacts the ball four times before returning it (with blocking exceptions)."),
            ("Double contact", "violation", "A player contacts the ball twice in succession when not allowed."),
            ("Catch or throw", "violation", "The ball is caught and/or thrown rather than hit."),
            ("Rotation fault", "violation", "Players are not in correct rotational order at the service hit."),
            ("Net fault", "violation", "Illegal contact with the net as defined by the current rules."),
            ("Referee ball in/out", "signal", "Referees use hand signals for in, out, touch, double, four hits, and net. Use the FIVB signal chart."),
        ],
        "equipment": [
            ("Volleyball", "The ball used for serve, pass, set, and attack.", "Indoor and beach balls differ in circumference, weight, and surface. Use the type required by the event.", "Inflate to the specified pressure. Wet beach balls change flight."),
            ("Net and antennae", "Divide the court and mark the crossing space.", "Net height is specified by gender and age group in the official rules.", "Secure posts. Pad poles in training gyms."),
            ("Court", "Playing surface with attack lines and service zones.", "18 m × 9 m indoor FIVB court.", "Keep the floor dry. Beach courts need level sand free of debris."),
            ("Knee pads", "Optional protection for passing and diving.", "Sizing should allow kneeling without sliding off.", "Do not rely on pads to make unsafe dives on hard floors."),
            ("Indoor shoes", "Traction for jumping and lateral movement.", "Non-marking gum rubber is common.", "Replace worn soles."),
        ],
        "techniques": [
            tech("Serving", "Putting the ball in play with an underhand, overhand, float, or jump serve.", ["Start in the service zone.", "Toss consistently.", "Contact the back of the ball.", "Move immediately into court after a legal serve."], "Master a standing float before jump serving.", "Tossing too far forward; stepping on the end line early.", "Do not serve until the receiving team is ready in recreational play. Clear the space behind the server.", 1),
            tech("Passing", "Usually a forearm pass (bump) to the setter.", ["Platform with flat forearms.", "Angle the platform; do not swing wildly.", "Move the feet to the ball.", "Call 'mine' when appropriate."], "Start with easy tosses. Watch the server’s toss.", "Swinging the arms from the shoulders; passing off the wrists.", "Keep thumbs aligned to reduce wrist strain. Progress diving gradually.", 2),
            tech("Setting", "A overhead pass that places the ball for an attacker.", ["Get under the ball.", "Hands form a window above the forehead.", "Extend the legs and arms together.", "Finish toward the target."], "Practice catch-and-throw only as a teaching drill, then move to a quick set contact.", "Holding the ball; setting from the hips; looking only at one attacker.", "Avoid hyperextending fingers. Stop if a finger joint is painful.", 3),
            tech("Spiking", "An attack hit, usually jumped, directed into the opponent’s court.", ["Approach.", "Jump vertically.", "Contact above the head with a fast arm swing.", "Land on both feet when possible."], "Hit lines and seam first, not just power.", "Early jump; hitting the net; no block awareness.", "Do not practice spiking without a clear landing area. Teach landing mechanics.", 4),
            tech("Blocking", "Jumping at the net to intercept an attack.", ["Read the setter.", "Penetrate hands across the net when the rules allow.", "Press the ball down or channel it.", "Land and turn to cover."], "Start with timing against a tossed ball.", "Reaching into the net; jumping late; leaving large seams.", "Keep fingers spread but not hyperextended into the attacker’s arm.", 5),
            tech("Digging", "An emergency pass of a hard-driven ball.", ["Low ready position.", "Read the hitter’s shoulder.", "Platform or emergency hand contact.", "Turn the ball high toward the court."], "Learn pancake and sprawl only after basic passing is stable.", "Standing upright; swinging at the ball; closing the eyes.", "Progress floor skills on a clean surface. Use knee pads on hard courts if needed.", 6),
        ],
        "safety": [("Net posts", "equipment", "Pad posts and avoid chasing balls into bleachers.")],
        "terms": [
            ("Serve", "The action that puts the ball in play."),
            ("Ace", "A serve that results directly in a point."),
            ("Set", "Typically the second contact, placing the ball for an attack."),
            ("Spike / attack hit", "A hit directed into the opponent’s court, often jumped."),
            ("Libero", "A defensive specialist with unique substitution rules."),
            ("Rotation", "The required order of players, advancing when the team gains the serve."),
            ("Side out", "Historically winning the right to serve; in rally scoring, also used informally when the receiving team wins the rally."),
        ],
        "faqs": [
            ("Can the serve touch the net?", "Under current FIVB indoor rules a serve that touches the net and continues into the opponent’s court may be in play. Confirm the edition used by your league."),
            ("How many times can a team touch the ball?", "Up to three contacts to return it, with blocking exceptions. See official text."),
        ],
        "references": [
            (FIVB, "Official Volleyball Rules", "Current edition — verify at fivb.com", "https://www.fivb.com", "Indoor, beach, and sitting volleyball have separate documents."),
        ],
    }
)
