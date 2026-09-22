from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from models import (
    Bookmark,
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
    db,
)
from services.auth import admin_required, require_fields, slugify

admin_bp = Blueprint("admin", __name__)
bookmarks_bp = Blueprint("bookmarks", __name__)


def _commit(entity, code=200):
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict() if hasattr(entity, "to_dict") else entity.to_detail()), code


def _sport(sport_id: int) -> Sport | None:
    return Sport.query.get(sport_id)


@admin_bp.post("/sports")
@admin_required
def create_sport():
    data = request.get_json(silent=True) or {}
    error = require_fields(data, ["name", "tagline", "overview", "history", "player_count", "court_dimensions", "scoring_system", "governing_org"])
    if error:
        return jsonify({"error": error}), 400
    sport = Sport(
        slug=data.get("slug") or slugify(data["name"]),
        name=data["name"].strip(),
        tagline=data["tagline"],
        overview=data["overview"],
        history=data["history"],
        player_count=data["player_count"],
        court_dimensions=data["court_dimensions"],
        scoring_system=data["scoring_system"],
        governing_org=data["governing_org"],
        featured=bool(data.get("featured", False)),
        popular=bool(data.get("popular", False)),
        icon=data.get("icon"),
        accent_color=data.get("accent_color"),
    )
    if Sport.query.filter_by(slug=sport.slug).first():
        return jsonify({"error": "A sport with that slug already exists."}), 409
    slugs = data.get("categories") or []
    if slugs:
        sport.categories = Category.query.filter(Category.slug.in_(slugs)).all()
    db.session.add(sport)
    db.session.commit()
    return jsonify(sport.to_detail()), 201


@admin_bp.put("/sports/<int:sport_id>")
@admin_required
def update_sport(sport_id: int):
    sport = _sport(sport_id)
    if not sport:
        return jsonify({"error": "Sport not found."}), 404
    data = request.get_json(silent=True) or {}
    for field in [
        "name",
        "tagline",
        "overview",
        "history",
        "player_count",
        "court_dimensions",
        "scoring_system",
        "governing_org",
        "icon",
        "accent_color",
        "slug",
    ]:
        if field in data and data[field] not in (None, ""):
            setattr(sport, field, data[field])
    if "featured" in data:
        sport.featured = bool(data["featured"])
    if "popular" in data:
        sport.popular = bool(data["popular"])
    if "categories" in data:
        slugs = data["categories"] or []
        sport.categories = Category.query.filter(Category.slug.in_(slugs)).all()
    db.session.commit()
    return jsonify(sport.to_detail())


@admin_bp.delete("/sports/<int:sport_id>")
@admin_required
def delete_sport(sport_id: int):
    sport = _sport(sport_id)
    if not sport:
        return jsonify({"error": "Sport not found."}), 404
    db.session.delete(sport)
    db.session.commit()
    return jsonify({"ok": True})


@admin_bp.post("/categories")
@admin_required
def create_category():
    data = request.get_json(silent=True) or {}
    error = require_fields(data, ["name", "description"])
    if error:
        return jsonify({"error": error}), 400
    category = Category(
        slug=data.get("slug") or slugify(data["name"]),
        name=data["name"].strip(),
        description=data["description"],
        icon=data.get("icon"),
    )
    return _commit(category, 201)


@admin_bp.put("/categories/<int:category_id>")
@admin_required
def update_category(category_id: int):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found."}), 404
    data = request.get_json(silent=True) or {}
    for field in ["name", "description", "icon", "slug"]:
        if field in data and data[field] not in (None, ""):
            setattr(category, field, data[field])
    db.session.commit()
    return jsonify(category.to_dict())


@admin_bp.delete("/categories/<int:category_id>")
@admin_required
def delete_category(category_id: int):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found."}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({"ok": True})


def _child_create(model, fields, extra=None):
    data = request.get_json(silent=True) or {}
    error = require_fields(data, fields)
    if error:
        return jsonify({"error": error}), 400
    if not Sport.query.get(data["sport_id"]):
        return jsonify({"error": "Sport not found."}), 404
    payload = {k: data.get(k) for k in data.keys() if hasattr(model, k)}
    if extra:
        payload.update(extra(data))
    entity = model(**payload)
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.to_dict()), 201


def _child_update(model, entity_id):
    entity = model.query.get(entity_id)
    if not entity:
        return jsonify({"error": "Not found."}), 404
    data = request.get_json(silent=True) or {}
    for key, value in data.items():
        if hasattr(entity, key) and key != "id":
            setattr(entity, key, value)
    db.session.commit()
    return jsonify(entity.to_dict())


def _child_delete(model, entity_id):
    entity = model.query.get(entity_id)
    if not entity:
        return jsonify({"error": "Not found."}), 404
    db.session.delete(entity)
    db.session.commit()
    return jsonify({"ok": True})


@admin_bp.post("/rules")
@admin_required
def create_rule():
    return _child_create(Rule, ["sport_id", "title", "content"])


@admin_bp.put("/rules/<int:item_id>")
@admin_required
def update_rule(item_id: int):
    return _child_update(Rule, item_id)


@admin_bp.delete("/rules/<int:item_id>")
@admin_required
def delete_rule(item_id: int):
    return _child_delete(Rule, item_id)


@admin_bp.post("/equipment")
@admin_required
def create_equipment():
    return _child_create(Equipment, ["sport_id", "name", "purpose"])


@admin_bp.put("/equipment/<int:item_id>")
@admin_required
def update_equipment(item_id: int):
    return _child_update(Equipment, item_id)


@admin_bp.delete("/equipment/<int:item_id>")
@admin_required
def delete_equipment(item_id: int):
    return _child_delete(Equipment, item_id)


@admin_bp.post("/techniques")
@admin_required
def create_technique():
    return _child_create(Technique, ["sport_id", "name", "description"])


@admin_bp.put("/techniques/<int:item_id>")
@admin_required
def update_technique(item_id: int):
    return _child_update(Technique, item_id)


@admin_bp.delete("/techniques/<int:item_id>")
@admin_required
def delete_technique(item_id: int):
    return _child_delete(Technique, item_id)


@admin_bp.post("/references")
@admin_required
def create_reference():
    return _child_create(ReferenceSource, ["sport_id", "organization", "title"])


@admin_bp.put("/references/<int:item_id>")
@admin_required
def update_reference(item_id: int):
    return _child_update(ReferenceSource, item_id)


@admin_bp.delete("/references/<int:item_id>")
@admin_required
def delete_reference(item_id: int):
    return _child_delete(ReferenceSource, item_id)


@admin_bp.post("/terminology")
@admin_required
def create_term():
    return _child_create(Term, ["sport_id", "term", "definition"])


@admin_bp.put("/terminology/<int:item_id>")
@admin_required
def update_term(item_id: int):
    return _child_update(Term, item_id)


@admin_bp.delete("/terminology/<int:item_id>")
@admin_required
def delete_term(item_id: int):
    return _child_delete(Term, item_id)


@admin_bp.post("/faqs")
@admin_required
def create_faq():
    return _child_create(Faq, ["sport_id", "question", "answer"])


@admin_bp.put("/faqs/<int:item_id>")
@admin_required
def update_faq(item_id: int):
    return _child_update(Faq, item_id)


@admin_bp.delete("/faqs/<int:item_id>")
@admin_required
def delete_faq(item_id: int):
    return _child_delete(Faq, item_id)


@admin_bp.post("/positions")
@admin_required
def create_position():
    return _child_create(PlayerPosition, ["sport_id", "name", "description"])


@admin_bp.put("/positions/<int:item_id>")
@admin_required
def update_position(item_id: int):
    return _child_update(PlayerPosition, item_id)


@admin_bp.delete("/positions/<int:item_id>")
@admin_required
def delete_position(item_id: int):
    return _child_delete(PlayerPosition, item_id)


@admin_bp.post("/fouls")
@admin_required
def create_foul():
    return _child_create(FoulViolation, ["sport_id", "name", "description"])


@admin_bp.put("/fouls/<int:item_id>")
@admin_required
def update_foul(item_id: int):
    return _child_update(FoulViolation, item_id)


@admin_bp.delete("/fouls/<int:item_id>")
@admin_required
def delete_foul(item_id: int):
    return _child_delete(FoulViolation, item_id)


@admin_bp.post("/safety")
@admin_required
def create_safety():
    data = request.get_json(silent=True) or {}
    error = require_fields(data, ["title", "content", "topic"])
    if error:
        return jsonify({"error": error}), 400
    item = SafetyGuideline(
        sport_id=data.get("sport_id"),
        title=data["title"],
        content=data["content"],
        topic=data["topic"],
        sort_order=int(data.get("sort_order") or 0),
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201


@admin_bp.put("/safety/<int:item_id>")
@admin_required
def update_safety(item_id: int):
    return _child_update(SafetyGuideline, item_id)


@admin_bp.delete("/safety/<int:item_id>")
@admin_required
def delete_safety(item_id: int):
    return _child_delete(SafetyGuideline, item_id)


@bookmarks_bp.get("")
@jwt_required()
def list_bookmarks():
    user_id = int(get_jwt_identity())
    items = Bookmark.query.filter_by(user_id=user_id).all()
    return jsonify({"bookmarks": [b.to_dict() for b in items]})


@bookmarks_bp.post("")
@jwt_required()
def add_bookmark():
    user_id = int(get_jwt_identity())
    data = request.get_json(silent=True) or {}
    sport_id = data.get("sport_id")
    if not sport_id or not Sport.query.get(sport_id):
        return jsonify({"error": "Valid sport_id required."}), 400
    existing = Bookmark.query.filter_by(user_id=user_id, sport_id=sport_id).first()
    if existing:
        return jsonify(existing.to_dict())
    item = Bookmark(user_id=user_id, sport_id=sport_id)
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201


@bookmarks_bp.delete("/<int:sport_id>")
@jwt_required()
def remove_bookmark(sport_id: int):
    user_id = int(get_jwt_identity())
    item = Bookmark.query.filter_by(user_id=user_id, sport_id=sport_id).first()
    if not item:
        return jsonify({"error": "Bookmark not found."}), 404
    db.session.delete(item)
    db.session.commit()
    return jsonify({"ok": True})
