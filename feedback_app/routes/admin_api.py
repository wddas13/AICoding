import logging
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from feedback_app.services import AdminService, FeedbackService
from feedback_app.utils import parse_pagination_args

bp = Blueprint("admin_api", __name__, url_prefix="/admin")
logger = logging.getLogger(__name__)


@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    password = (data.get("password") or "").strip()
    
    logger.info(f"管理员登录尝试 - 用户名: {username}, IP: {request.remote_addr}")
    
    token = AdminService.authenticate(username, password)
    if not token:
        logger.warning(f"管理员登录失败 - 用户名: {username}, IP: {request.remote_addr}")
        return jsonify({"msg": "invalid credentials"}), 401
    
    logger.info(f"管理员登录成功 - 用户名: {username}, IP: {request.remote_addr}")
    return jsonify({"token": token})


@bp.route("/feedback/list", methods=["GET"])
@jwt_required()
def feedback_list():
    page, size = parse_pagination_args(request.args)
    keyword = request.args.get("keyword") or None
    
    logger.info(f"查询反馈列表 - page: {page}, size: {size}, keyword: {keyword}")
    
    result = FeedbackService.list_feedback(page, size, keyword)
    
    logger.info(f"反馈列表查询完成 - 返回 {len(result.get('items', []))} 条记录")
    
    return jsonify(result)
