from flask import Blueprint, jsonify, request

from models import Category, SafetyGuideline, Sport
from services.search import search_content

public_bp = Blueprint("public", __name__)


def _sport_by_id_or_slug(value: str) -> Sport | None:
    if value.isdigit():
        sport = Sport.query.get(int(value))
        if sport:
            return sport
    return Sport.query.filter_by(slug=value).first()


@public_bp.get("/health")
def health():
    return jsonify({"status": "ok", "service": "sports-hub"})


@public_bp.get("/sports")
def list_sports():
    query = Sport.query
    category = request.args.get("category")
    if category:
        query = query.join(Sport.categories).filter(
            (Category.slug == category) | (Category.name.ilike(category))
        )
    if request.args.get("featured") == "true":
        query = query.filter_by(featured=True)
    if request.args.get("popular") == "true":
        query = query.filter_by(popular=True)
    sports = query.order_by(Sport.name.asc()).all()
    return jsonify({"sports": [s.to_summary() for s in sports]})


@public_bp.get("/sports/<value>")
def get_sport(value: str):
    sport = _sport_by_id_or_slug(value)
    if not sport:
        return jsonify({"error": "Sport not found."}), 404
    return jsonify(sport.to_detail())


@public_bp.get("/categories")
def list_categories():
    categories = Category.query.order_by(Category.name.asc()).all()
    return jsonify({"categories": [c.to_dict(include_count=True) for c in categories]})


@public_bp.get("/categories/<slug>/sports")
def sports_in_category(slug: str):
    category = Category.query.filter_by(slug=slug).first()
    if not category:
        return jsonify({"error": "Category not found."}), 404
    sports = sorted(category.sports, key=lambda s: s.name)
    return jsonify({"category": category.to_dict(), "sports": [s.to_summary() for s in sports]})


@public_bp.get("/rules/<sport_id>")
def rules_for_sport(sport_id: str):
    sport = _sport_by_id_or_slug(sport_id)
    if not sport:
        return jsonify({"error": "Sport not found."}), 404
    return jsonify({"sport": sport.to_summary(), "rules": [r.to_dict() for r in sport.rules]})


@public_bp.get("/equipment/<sport_id>")
def equipment_for_sport(sport_id: str):
    sport = _sport_by_id_or_slug(sport_id)
    if not sport:
        return jsonify({"error": "Sport not found."}), 404
    return jsonify({"sport": sport.to_summary(), "equipment": [e.to_dict() for e in sport.equipment]})


@public_bp.get("/techniques/<sport_id>")
def techniques_for_sport(sport_id: str):
    sport = _sport_by_id_or_slug(sport_id)
    if not sport:
        return jsonify({"error": "Sport not found."}), 404
    return jsonify({"sport": sport.to_summary(), "techniques": [t.to_dict() for t in sport.techniques]})


@public_bp.get("/safety")
def safety():
    general = SafetyGuideline.query.filter_by(sport_id=None).order_by(SafetyGuideline.sort_order).all()
    sport_id = request.args.get("sport")
    sport_items = []
    if sport_id:
        sport = _sport_by_id_or_slug(sport_id)
        if sport:
            sport_items = [s.to_dict() for s in sport.safety_guidelines]
    return jsonify({"general": [g.to_dict() for g in general], "sport": sport_items})


@public_bp.get("/recent")
def recent():
    sports = Sport.query.order_by(Sport.updated_at.desc()).limit(6).all()
    return jsonify({"sports": [s.to_summary() for s in sports]})


@public_bp.get("/search")
def search():
    payload = search_content(request.args.get("q", ""))
    if not payload["results"] and len(payload.get("query", "")) >= 2:
        payload["message"] = "No results found. Try another sport, rule, term, or technique."
    return jsonify(payload)


@public_bp.get("/site/about")
def about():
    return jsonify(
        {
            "name": "Sports Hub",
            "tagline": "Everything Athletes Need in One Place",
            "purpose": (
                "Sports Hub is an educational platform that makes sports information easier to access. "
                "It explains sports, rules, equipment, techniques, terminology, and safety in plain language "
                "for athletes, coaches, students, enthusiasts, and beginners."
            ),
            "audience": [
                "Athletes",
                "Coaches",
                "Students",
                "Sports enthusiasts",
                "Beginners",
            ],
            "features": [
                "Sport guides with a consistent structure",
                "Search across rules, terms, equipment, and techniques",
                "Category filters",
                "Beginner training explanations",
                "General safety information",
                "Local bookmarks (browser storage)",
                "Administrator tools to keep sources current",
            ],
            "disclaimer": (
                "Sports Hub is not an official rulebook, medical service, or coaching certification. "
                "Official rules may vary by governing organisation, competition, age group, and edition. "
                "Training notes are educational suggestions, not a substitute for a qualified coach. "
                "Safety notes are general and not personal medical advice."
            ),
        }
    )
