import logging
from flask import Blueprint, request, jsonify

from feedback_app.services import TaskService

bp = Blueprint("task_api", __name__, url_prefix="/api")
logger = logging.getLogger(__name__)


@bp.route("/tasks", methods=["GET"])
def list_tasks():
    """列出所有任务"""
    logger.info(f"查询任务列表 - IP: {request.remote_addr}")
    
    tasks = TaskService.list_tasks()
    
    logger.info(f"任务列表查询完成 - 返回 {len(tasks)} 条记录")
    
    return jsonify({"msg": "success", "data": tasks})


@bp.route("/tasks", methods=["POST"])
def add_task():
    """新增任务"""
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    
    logger.info(f"收到新增任务请求 - 标题: {title}, IP: {request.remote_addr}")
    
    if not title:
        logger.warning(f"任务新增失败 - 标题为空, IP: {request.remote_addr}")
        return jsonify({"msg": "invalid", "errors": ["标题不能为空"]}), 400
    
    description = data.get("description")
    task = TaskService.add_task(title, description)
    
    logger.info(f"任务新增成功 - ID: {task.id}, 标题: {title}, IP: {request.remote_addr}")
    
    return jsonify({
        "msg": "success",
        "data": {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "create_time": task.create_time.isoformat(),
        }
    }), 201


@bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """删除任务"""
    logger.info(f"收到删除任务请求 - ID: {task_id}, IP: {request.remote_addr}")
    
    success = TaskService.delete_task(task_id)
    
    if not success:
        logger.warning(f"任务删除失败 - ID: {task_id} 不存在, IP: {request.remote_addr}")
        return jsonify({"msg": "error", "errors": ["任务不存在"]}), 404
    
    logger.info(f"任务删除成功 - ID: {task_id}, IP: {request.remote_addr}")
    
    return jsonify({"msg": "success"}), 200

