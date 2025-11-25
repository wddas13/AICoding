import logging
from feedback_app.extensions import db
from feedback_app.models import Task

logger = logging.getLogger(__name__)


class TaskService:
    @staticmethod
    def add_task(title, description=None):
        """添加新任务"""
        try:
            logger.info(f"[TaskService] 开始添加任务 - 标题: {title}")
            
            task = Task(title=title, description=description)
            db.session.add(task)
            db.session.commit()
            
            logger.info(f"[TaskService] 任务添加成功 - ID: {task.id}, 标题: {title}")
            return task
        except Exception as e:
            logger.error(f"[TaskService] 任务添加失败 - 标题: {title}, 错误: {str(e)}")
            db.session.rollback()
            raise

    @staticmethod
    def list_tasks():
        """列出所有任务"""
        try:
            logger.debug("[TaskService] 开始查询任务列表")
            
            tasks = Task.query.order_by(Task.create_time.desc()).all()
            
            logger.info(f"[TaskService] 任务列表查询成功 - 共 {len(tasks)} 条记录")
            
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
        except Exception as e:
            logger.error(f"[TaskService] 任务列表查询失败 - 错误: {str(e)}")
            raise

    @staticmethod
    def delete_task(task_id):
        """删除任务"""
        try:
            logger.info(f"[TaskService] 开始删除任务 - ID: {task_id}")
            
            task = Task.query.get(task_id)
            if not task:
                logger.warning(f"[TaskService] 任务不存在 - ID: {task_id}")
                return False
            
            task_title = task.title
            db.session.delete(task)
            db.session.commit()
            
            logger.info(f"[TaskService] 任务删除成功 - ID: {task_id}, 标题: {task_title}")
            return True
        except Exception as e:
            logger.error(f"[TaskService] 任务删除失败 - ID: {task_id}, 错误: {str(e)}")
            db.session.rollback()
            raise

