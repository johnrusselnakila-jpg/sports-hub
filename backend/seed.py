"""Load categories, sports, and an admin user. Run from the backend directory."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import Settings
from data import CATEGORIES, GENERAL_SAFETY, SPORTS
from models import (
    Category,
    Equipment,
    Faq,
    FoulViolation,
    PlayerPosition,
    ReferenceSource,
    Rule,
    SafetyGuideline,
    Sport,
    Technique,
    Term,
    User,
    db,
)
from services.auth import hash_password


def get_or_create_category(item: dict) -> Category:
    existing = Category.query.filter_by(slug=item["slug"]).first()
    if existing:
        existing.name = item["name"]
        existing.description = item["description"]
        existing.icon = item.get("icon")
        return existing
    category = Category(**item)
    db.session.add(category)
    return category


def upsert_sport(payload: dict, categories_by_slug: dict[str, Category]) -> None:
    sport = Sport.query.filter_by(slug=payload["slug"]).first()
    fields = [
        "name",
        "tagline",
        "overview",
        "history",
        "player_count",
        "court_dimensions",
        "scoring_system",
        "governing_org",
        "featured",
        "popular",
        "icon",
        "accent_color",
    ]
    if not sport:
        sport = Sport(slug=payload["slug"])
        db.session.add(sport)
    for field in fields:
        setattr(sport, field, payload[field])
    sport.categories = [categories_by_slug[slug] for slug in payload.get("categories", []) if slug in categories_by_slug]
    db.session.flush()

    Rule.query.filter_by(sport_id=sport.id).delete()
    Equipment.query.filter_by(sport_id=sport.id).delete()
    Technique.query.filter_by(sport_id=sport.id).delete()
    SafetyGuideline.query.filter_by(sport_id=sport.id).delete()
    Term.query.filter_by(sport_id=sport.id).delete()
    Faq.query.filter_by(sport_id=sport.id).delete()
    ReferenceSource.query.filter_by(sport_id=sport.id).delete()
    PlayerPosition.query.filter_by(sport_id=sport.id).delete()
    FoulViolation.query.filter_by(sport_id=sport.id).delete()

    for index, (name, description) in enumerate(payload.get("positions", []), start=1):
        db.session.add(PlayerPosition(sport_id=sport.id, name=name, description=description, sort_order=index))

    for item in payload.get("rules", []):
        db.session.add(Rule(sport_id=sport.id, **item))

    for index, row in enumerate(payload.get("equipment", []), start=1):
        name, purpose, specs, safety = row
        db.session.add(
            Equipment(
                sport_id=sport.id,
                name=name,
                purpose=purpose,
                specifications=specs,
                safety_considerations=safety,
                sort_order=index,
            )
        )

    for item in payload.get("techniques", []):
        db.session.add(Technique(sport_id=sport.id, **item))

    for index, (title, topic, content) in enumerate(payload.get("safety", []), start=1):
        db.session.add(
            SafetyGuideline(sport_id=sport.id, title=title, topic=topic, content=content, sort_order=index)
        )

    for term, definition in payload.get("terms", []):
        db.session.add(Term(sport_id=sport.id, term=term, definition=definition))

    for index, (question, answer) in enumerate(payload.get("faqs", []), start=1):
        db.session.add(Faq(sport_id=sport.id, question=question, answer=answer, sort_order=index))

    for org, title, edition, url, notes in payload.get("references", []):
        db.session.add(
            ReferenceSource(
                sport_id=sport.id,
                organization=org,
                title=title,
                edition_year=edition,
                url=url,
                notes=notes,
            )
        )

    for index, (name, kind, description) in enumerate(payload.get("fouls", []), start=1):
        db.session.add(
            FoulViolation(sport_id=sport.id, name=name, kind=kind, description=description, sort_order=index)
        )


def seed() -> None:
    db.create_all()
    categories = {item["slug"]: get_or_create_category(item) for item in CATEGORIES}
    db.session.flush()

    SafetyGuideline.query.filter_by(sport_id=None).delete()
    for item in GENERAL_SAFETY:
        db.session.add(SafetyGuideline(sport_id=None, **item))

    for sport in SPORTS:
        upsert_sport(sport, categories)

    admin_email = (Settings.ADMIN_EMAIL or "admin@sportshub.local").strip().lower()
    admin_password = Settings.ADMIN_PASSWORD
    if not admin_password:
        raise SystemExit("Set ADMIN_PASSWORD in the environment before seeding.")
    admin = User.query.filter_by(email=admin_email).first()
    if not admin:
        admin = User(email=admin_email, display_name="Sports Hub Admin", role="admin")
        db.session.add(admin)
    admin.password_hash = hash_password(admin_password)
    admin.role = "admin"
    db.session.commit()
    print(f"Seeded {len(SPORTS)} sports. Admin: {admin_email}")


if __name__ == "__main__":
    from app import app

    with app.app_context():
        seed()
