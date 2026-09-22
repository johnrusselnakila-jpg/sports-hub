import os

from dotenv import load_dotenv

load_dotenv()


def _env(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name, default)
    return value


class Settings:
    SECRET_KEY = _env("SECRET_KEY")
    JWT_SECRET_KEY = _env("JWT_SECRET_KEY") or _env("SECRET_KEY")
    DATABASE_URL = _env("DATABASE_URL")
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = "postgresql://" + DATABASE_URL[len("postgres://") :]
    FRONTEND_ORIGIN = _env("FRONTEND_ORIGIN", "*")
    ADMIN_EMAIL = _env("ADMIN_EMAIL", "admin@sportshub.local")
    ADMIN_PASSWORD = _env("ADMIN_PASSWORD")
    DEBUG = _env("FLASK_ENV", "production") == "development"

    @classmethod
    def validate(cls) -> None:
        missing = []
        if not cls.SECRET_KEY:
            missing.append("SECRET_KEY")
        if not cls.DATABASE_URL:
            missing.append("DATABASE_URL")
        if missing:
            raise RuntimeError(
                "Missing required environment variables: " + ", ".join(missing)
            )
