from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .entities import (  # noqa: E402
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
    User,
)

__all__ = [
    "db",
    "Bookmark",
    "Category",
    "Equipment",
    "Faq",
    "FoulViolation",
    "PlayerPosition",
    "ReferenceSource",
    "Rule",
    "SafetyGuideline",
    "Sport",
    "Technique",
    "Term",
    "User",
]
