from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from models import User, db
from services.auth import hash_password, require_fields, verify_password

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    error = require_fields(data, ["email", "password"])
    if error:
        return jsonify({"error": error}), 400
    email = data["email"].strip().lower()
    user = User.query.filter_by(email=email).first()
    if not user or not verify_password(data["password"], user.password_hash):
        return jsonify({"error": "Invalid email or password."}), 401
    token = create_access_token(identity=str(user.id), additional_claims={"role": user.role, "email": user.email})
    return jsonify({"access_token": token, "user": user.to_public()})


@auth_bp.post("/register")
def register():
    data = request.get_json(silent=True) or {}
    error = require_fields(data, ["email", "password", "display_name"])
    if error:
        return jsonify({"error": error}), 400
    email = data["email"].strip().lower()
    if "@" not in email or "." not in email.split("@")[-1]:
        return jsonify({"error": "Enter a valid email address."}), 400
    if len(data["password"]) < 8:
        return jsonify({"error": "Password must be at least 8 characters."}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "An account with that email already exists."}), 409
    user = User(
        email=email,
        password_hash=hash_password(data["password"]),
        display_name=str(data["display_name"]).strip()[:120],
        role="visitor",
    )
    db.session.add(user)
    db.session.commit()
    token = create_access_token(identity=str(user.id), additional_claims={"role": user.role, "email": user.email})
    return jsonify({"access_token": token, "user": user.to_public()}), 201


@auth_bp.get("/me")
@jwt_required()
def me():
    user = User.query.get(int(get_jwt_identity()))
    if not user:
        return jsonify({"error": "User not found."}), 404
    return jsonify({"user": user.to_public()})
