from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.admin_service import AdminService
from services.feedback_service import FeedbackService
from utils.pagination import parse_pagination_args


bp = Blueprint("admin_api", __name__, url_prefix="/admin")


@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    password = (data.get("password") or "").strip()
    token = AdminService.authenticate(username, password)
    if not token:
        return jsonify({"msg": "invalid credentials"}), 401
    return jsonify({"token": token})


@bp.route("/feedback/list", methods=["GET"])
@jwt_required()
def feedback_list():
    page, size = parse_pagination_args(request.args)
    keyword = request.args.get("keyword") or None
    result = FeedbackService.list_feedback(page, size, keyword)
    return jsonify(result)
