from extensions import db
from models.task import Task


class TaskService:
    @staticmethod
    def add_task(title, description=None):
        """添加新任务"""
        task = Task(title=title, description=description)
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def list_tasks():
        """列出所有任务"""
        tasks = Task.query.order_by(Task.create_time.desc()).all()
        return [
            {
                "id": t.id,
                "title": t.title,
                "description": t.description,
                "status": t.status,
                "create_time": t.create_time.isoformat(),
                "update_time": t.update_time.isoformat(),
            }
            for t in tasks
        ]

    @staticmethod
    def delete_task(task_id):
        """删除任务"""
        task = Task.query.get(task_id)
        if not task:
            return False
        db.session.delete(task)
        db.session.commit()
        return True

