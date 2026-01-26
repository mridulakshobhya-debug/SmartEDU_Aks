from flask import Blueprint, request, jsonify

bp_auth = Blueprint("auth", __name__)

@bp_auth.route("/auth")
def auth():
    return jsonify({"message": "Auth route"})
