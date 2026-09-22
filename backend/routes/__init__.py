from .admin import admin_bp, bookmarks_bp
from .auth import auth_bp
from .public import public_bp

__all__ = ["admin_bp", "auth_bp", "bookmarks_bp", "public_bp"]
