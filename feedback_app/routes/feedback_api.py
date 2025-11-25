import logging
from flask import Blueprint, request, jsonify

from feedback_app.services import FeedbackService
from feedback_app.utils import validate_feedback_payload

bp = Blueprint("feedback_api", __name__, url_prefix="/api/feedback")
logger = logging.getLogger(__name__)


@bp.route("/add", methods=["POST"])
def add_feedback():
    data = request.get_json(silent=True) or {}
    
    logger.info(f"收到新反馈请求 - IP: {request.remote_addr}")
    
    errors = validate_feedback_payload(data)
    if errors:
        logger.warning(f"反馈验证失败 - 错误: {errors}, IP: {request.remote_addr}")
        return jsonify({"msg": "invalid", "errors": errors}), 400
    
    content = data.get("content")
    contact = data.get("contact")
    ip = request.headers.get("X-Forwarded-For") or request.headers.get("X-Real-IP") or request.remote_addr
    
    logger.info(f"添加反馈 - 内容长度: {len(content)}, 联系方式: {contact}, IP: {ip}")
    
    fb = FeedbackService.add_feedback(content, contact, ip)
    
    logger.info(f"反馈添加成功 - ID: {fb.id}, IP: {ip}")
    
    return jsonify({"msg": "success", "id": fb.id})

