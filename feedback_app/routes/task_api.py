from flask import Blueprint, request, jsonify

from feedback_app.services import TaskService

bp = Blueprint("task_api", __name__, url_prefix="/api")


@bp.route("/tasks", methods=["GET"])
def list_tasks():
    """列出所有任务"""
    tasks = TaskService.list_tasks()
    return jsonify({"msg": "success", "data": tasks})


@bp.route("/tasks", methods=["POST"])
def add_task():
    """新增任务"""
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    
    if not title:
        return jsonify({"msg": "invalid", "errors": ["标题不能为空"]}), 400
    
    description = data.get("description")
    task = TaskService.add_task(title, description)
    
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
    success = TaskService.delete_task(task_id)
    
    if not success:
        return jsonify({"msg": "error", "errors": ["任务不存在"]}), 404
    
    return jsonify({"msg": "success"}), 200

