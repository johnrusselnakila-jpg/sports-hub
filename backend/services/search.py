from sqlalchemy import or_

from models import Equipment, Rule, SafetyGuideline, Sport, Technique, Term


def search_content(query: str, limit: int = 40) -> dict:
    q = (query or "").strip()
    if len(q) < 2:
        return {"query": q, "results": [], "message": "Enter at least 2 characters."}

    like = f"%{q}%"
    results = []

    sports = Sport.query.filter(
        or_(Sport.name.ilike(like), Sport.tagline.ilike(like), Sport.overview.ilike(like), Sport.history.ilike(like))
    ).all()
    for sport in sports:
        results.append(
            {
                "type": "sport",
                "title": sport.name,
                "snippet": sport.tagline,
                "sport_slug": sport.slug,
                "sport_name": sport.name,
            }
        )

    terms = Term.query.filter(or_(Term.term.ilike(like), Term.definition.ilike(like))).limit(limit).all()
    for term in terms:
        results.append(
            {
                "type": "term",
                "title": term.term,
                "snippet": term.definition[:240],
                "sport_slug": term.sport.slug,
                "sport_name": term.sport.name,
            }
        )

    rules = Rule.query.filter(or_(Rule.title.ilike(like), Rule.content.ilike(like))).limit(limit).all()
    for rule in rules:
        results.append(
            {
                "type": "rule",
                "title": rule.title,
                "snippet": rule.content[:240],
                "sport_slug": rule.sport.slug,
                "sport_name": rule.sport.name,
            }
        )

    equipment = Equipment.query.filter(
        or_(Equipment.name.ilike(like), Equipment.purpose.ilike(like), Equipment.specifications.ilike(like))
    ).limit(limit).all()
    for item in equipment:
        results.append(
            {
                "type": "equipment",
                "title": item.name,
                "snippet": item.purpose[:240],
                "sport_slug": item.sport.slug,
                "sport_name": item.sport.name,
            }
        )

    techniques = Technique.query.filter(
        or_(Technique.name.ilike(like), Technique.description.ilike(like), Technique.beginner_tips.ilike(like))
    ).limit(limit).all()
    for technique in techniques:
        results.append(
            {
                "type": "technique",
                "title": technique.name,
                "snippet": technique.description[:240],
                "sport_slug": technique.sport.slug,
                "sport_name": technique.sport.name,
            }
        )

    safety = SafetyGuideline.query.filter(
        or_(SafetyGuideline.title.ilike(like), SafetyGuideline.content.ilike(like))
    ).limit(limit).all()
    for item in safety:
        results.append(
            {
                "type": "safety",
                "title": item.title,
                "snippet": item.content[:240],
                "sport_slug": item.sport.slug if item.sport else None,
                "sport_name": item.sport.name if item.sport else "General safety",
            }
        )

    # Stable de-duplication by type+title+sport
    unique = []
    seen = set()
    for row in results:
        key = (row["type"], row["title"], row.get("sport_slug"))
        if key in seen:
            continue
        seen.add(key)
        unique.append(row)

    return {"query": q, "count": len(unique), "results": unique[:limit]}
