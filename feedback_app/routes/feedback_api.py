from flask import Blueprint, request, jsonify

from feedback_app.services import FeedbackService
from feedback_app.utils import validate_feedback_payload

bp = Blueprint("feedback_api", __name__, url_prefix="/api/feedback")


@bp.route("/add", methods=["POST"])
def add_feedback():
    data = request.get_json(silent=True) or {}
    errors = validate_feedback_payload(data)
    if errors:
        return jsonify({"msg": "invalid", "errors": errors}), 400
    content = data.get("content")
    contact = data.get("contact")
    ip = request.headers.get("X-Forwarded-For") or request.headers.get("X-Real-IP") or request.remote_addr
    fb = FeedbackService.add_feedback(content, contact, ip)
    return jsonify({"msg": "success", "id": fb.id})

