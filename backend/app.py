from datetime import timedelta
from pathlib import Path

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Settings
from models import db
from routes import admin_bp, auth_bp, bookmarks_bp, public_bp

def _web_dir() -> Path | None:
    here = Path(__file__).resolve().parent
    for candidate in (here / "web", here.parent / "frontend" / "build" / "web"):
        if (candidate / "index.html").exists():
            return candidate
    return None


def create_app() -> Flask:
    Settings.validate()
    web_dir = _web_dir()
    static_folder = str(web_dir) if web_dir else None
    app = Flask(__name__, static_folder=static_folder, static_url_path="")
    app.config["SECRET_KEY"] = Settings.SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = Settings.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = Settings.JWT_SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12)

    db.init_app(app)
    JWTManager(app)

    origins = Settings.FRONTEND_ORIGIN
    if origins == "*":
        CORS(app, resources={r"/api/*": {"origins": "*"}})
    else:
        allowed = [o.strip() for o in origins.split(",") if o.strip()]
        CORS(app, resources={r"/api/*": {"origins": allowed}}, supports_credentials=True)

    app.register_blueprint(public_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(bookmarks_bp, url_prefix="/api/bookmarks")

    @app.errorhandler(404)
    def not_found(_e):
        from flask import request

        if request.path.startswith("/api/"):
            return jsonify({"error": "Not found."}), 404
        if web_dir is not None:
            return send_from_directory(web_dir, "index.html")
        return jsonify({"error": "Not found."}), 404

    @app.route("/")
    def root():
        if web_dir is not None:
            return send_from_directory(web_dir, "index.html")
        return jsonify(
            {
                "name": "Sports Hub API",
                "tagline": "Everything Athletes Need in One Place",
                "docs": "/api/health",
            }
        )

    with app.app_context():
        db.create_all()
        from models import Sport

        if Sport.query.count() == 0 and Settings.ADMIN_PASSWORD:
            from seed import seed

            seed()

    return app


app = create_app()

if __name__ == "__main__":
    import os

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=Settings.DEBUG)
