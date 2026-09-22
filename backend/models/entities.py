from datetime import datetime, timezone

from . import db


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    display_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="visitor")
    created_at = db.Column(db.DateTime(timezone=True), default=utcnow)

    def to_public(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "display_name": self.display_name,
            "role": self.role,
        }


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(80))
    sports = db.relationship(
        "Sport",
        secondary="sport_categories",
        back_populates="categories",
    )

    def to_dict(self, include_count: bool = False) -> dict:
        data = {
            "id": self.id,
            "slug": self.slug,
            "name": self.name,
            "description": self.description,
            "icon": self.icon,
        }
        if include_count:
            data["sport_count"] = len(self.sports)
        return data


sport_categories = db.Table(
    "sport_categories",
    db.Column("sport_id", db.Integer, db.ForeignKey("sports.id", ondelete="CASCADE"), primary_key=True),
    db.Column("category_id", db.Integer, db.ForeignKey("categories.id", ondelete="CASCADE"), primary_key=True),
)


class Sport(db.Model):
    __tablename__ = "sports"

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(255), nullable=False)
    overview = db.Column(db.Text, nullable=False)
    history = db.Column(db.Text, nullable=False)
    player_count = db.Column(db.Text, nullable=False)
    court_dimensions = db.Column(db.Text, nullable=False)
    scoring_system = db.Column(db.Text, nullable=False)
    governing_org = db.Column(db.String(255), nullable=False)
    featured = db.Column(db.Boolean, nullable=False, default=False)
    popular = db.Column(db.Boolean, nullable=False, default=False)
    icon = db.Column(db.String(80))
    accent_color = db.Column(db.String(16))
    created_at = db.Column(db.DateTime(timezone=True), default=utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=utcnow, onupdate=utcnow)

    categories = db.relationship("Category", secondary=sport_categories, back_populates="sports")
    rules = db.relationship("Rule", backref="sport", cascade="all, delete-orphan", order_by="Rule.sort_order")
    equipment = db.relationship("Equipment", backref="sport", cascade="all, delete-orphan", order_by="Equipment.sort_order")
    techniques = db.relationship("Technique", backref="sport", cascade="all, delete-orphan", order_by="Technique.sort_order")
    safety_guidelines = db.relationship("SafetyGuideline", backref="sport", cascade="all, delete-orphan", order_by="SafetyGuideline.sort_order")
    terminology = db.relationship("Term", backref="sport", cascade="all, delete-orphan")
    faqs = db.relationship("Faq", backref="sport", cascade="all, delete-orphan", order_by="Faq.sort_order")
    references = db.relationship("ReferenceSource", backref="sport", cascade="all, delete-orphan")
    positions = db.relationship("PlayerPosition", backref="sport", cascade="all, delete-orphan", order_by="PlayerPosition.sort_order")
    fouls = db.relationship("FoulViolation", backref="sport", cascade="all, delete-orphan", order_by="FoulViolation.sort_order")

    def to_summary(self) -> dict:
        return {
            "id": self.id,
            "slug": self.slug,
            "name": self.name,
            "tagline": self.tagline,
            "overview": self.overview[:220] + ("…" if len(self.overview) > 220 else ""),
            "featured": self.featured,
            "popular": self.popular,
            "icon": self.icon,
            "accent_color": self.accent_color,
            "governing_org": self.governing_org,
            "categories": [c.to_dict() for c in self.categories],
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

    def to_detail(self) -> dict:
        return {
            **self.to_summary(),
            "overview": self.overview,
            "history": self.history,
            "player_count": self.player_count,
            "court_dimensions": self.court_dimensions,
            "scoring_system": self.scoring_system,
            "rules": [r.to_dict() for r in self.rules],
            "equipment": [e.to_dict() for e in self.equipment],
            "techniques": [t.to_dict() for t in self.techniques],
            "safety_guidelines": [s.to_dict() for s in self.safety_guidelines],
            "terminology": [t.to_dict() for t in self.terminology],
            "faqs": [f.to_dict() for f in self.faqs],
            "references": [r.to_dict() for r in self.references],
            "positions": [p.to_dict() for p in self.positions],
            "fouls_violations": [f.to_dict() for f in self.fouls],
        }


class Rule(db.Model):
    __tablename__ = "rules"

    id = db.Column(db.Integer, primary_key=True)
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id", ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    sort_order = db.Column(db.Integer, nullable=False, default=0)
    content = db.Column(db.Text, nullable=False)
    content_type = db.Column(db.String(40), nullable=False, default="educational")
    source_org = db.Column(db.String(255))
    rule_edition = db.Column(db.String(255))

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "sport_id": self.sport_id,
            "sport_name": self.sport.name if self.sport else None,
            "sport_slug": self.sport.slug if self.sport else None,
            "title": self.title,
            "sort_order": self.sort_order,
            "content": self.content,
            "content_type": self.content_type,
            "source_org": self.source_org,
            "rule_edition": self.rule_edition,
        }


class Equipment(db.Model):
    __tablename__ = "equipment"

    id = db.Column(db.Integer, primary_key=True)
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id", ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    purpose = db.Column(db.Text, nullable=False)
    specifications = db.Column(db.Text)
    safety_considerations = db.Column(db.Text)
    icon = db.Column(db.String(80))
    sort_order = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "sport_id": self.sport_id,
            "sport_name": self.sport.name if self.sport else None,
            "sport_slug": self.sport.slug if self.sport else None,
            "name": self.name,
            "purpose": self.purpose,
            "specifications": self.specifications,
            "safety_considerations": self.safety_considerations,
            "icon": self.icon,
            "sort_order": self.sort_order,
        }


class Technique(db.Model):
    __tablename__ = "techniques"

    id = db.Column(db.Integer, primary_key=True)
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id", ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    steps = db.Column(db.JSON, nullable=False, default=list)
    beginner_tips = db.Column(db.Text)
    common_mistakes = db.Column(db.Text)
    safety_reminders = db.Column(db.Text)
    sort_order = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "sport_id": self.sport_id,
            "sport_name": self.sport.name if self.sport else None,
            "sport_slug": self.sport.slug if self.sport else None,
            "name": self.name,
            "description": self.description,
            "steps": self.steps or [],
            "beginner_tips": self.beginner_tips,
            "common_mistakes": self.common_mistakes,
            "safety_reminders": self.safety_reminders,
            "sort_order": self.sort_order,
        }


class SafetyGuideline(db.Model):
    __tablename__ = "safety_guidelines"

    id = db.Column(db.Integer, primary_key=True)
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id", ondelete="CASCADE"), nullable=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    topic = db.Column(db.String(80), nullable=False)
    sort_order = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "sport_id": self.sport_id,
            "sport_name": self.sport.name if self.sport else None,
            "title": self.title,
            "content": self.content,
            "topic": self.topic,
            "sort_order": self.sort_order,
        }


class Term(db.Model):
    __tablename__ = "terminology"

    id = db.Column(db.Integer, primary_key=True)
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id", ondelete="CASCADE"), nullable=False)
    term = db.Column(db.String(160), nullable=False)
    definition = db.Column(db.Text, nullable=False)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "sport_id": self.sport_id,
            "sport_name": self.sport.name if self.sport else None,
            "sport_slug": self.sport.slug if self.sport else None,
            "term": self.term,
            "definition": self.definition,
        }


class Faq(db.Model):
    __tablename__ = "faqs"

    id = db.Column(db.Integer, primary_key=True)
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id", ondelete="CASCADE"), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    sort_order = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "sport_id": self.sport_id,
            "question": self.question,
            "answer": self.answer,
            "sort_order": self.sort_order,
        }


class ReferenceSource(db.Model):
    __tablename__ = "references_sources"

    id = db.Column(db.Integer, primary_key=True)
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id", ondelete="CASCADE"), nullable=True)
    organization = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    edition_year = db.Column(db.String(80))
    url = db.Column(db.Text)
    notes = db.Column(db.Text)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "sport_id": self.sport_id,
            "sport_name": self.sport.name if self.sport else None,
            "organization": self.organization,
            "title": self.title,
            "edition_year": self.edition_year,
            "url": self.url,
            "notes": self.notes,
        }


class PlayerPosition(db.Model):
    __tablename__ = "player_positions"

    id = db.Column(db.Integer, primary_key=True)
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id", ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(160), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sort_order = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "sport_id": self.sport_id,
            "name": self.name,
            "description": self.description,
            "sort_order": self.sort_order,
        }


class FoulViolation(db.Model):
    __tablename__ = "fouls_violations"

    id = db.Column(db.Integer, primary_key=True)
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id", ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(160), nullable=False)
    description = db.Column(db.Text, nullable=False)
    kind = db.Column(db.String(40), nullable=False, default="violation")
    sort_order = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "sport_id": self.sport_id,
            "name": self.name,
            "description": self.description,
            "kind": self.kind,
            "sort_order": self.sort_order,
        }


class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    sport_id = db.Column(db.Integer, db.ForeignKey("sports.id", ondelete="CASCADE"), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=utcnow)

    sport = db.relationship("Sport")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "sport_id": self.sport_id,
            "sport": self.sport.to_summary() if self.sport else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
