"""
路由包
"""
from .feedback_api import bp as feedback_bp
from .admin_api import bp as admin_bp
from .task_api import bp as task_bp

__all__ = ['feedback_bp', 'admin_bp', 'task_bp']

