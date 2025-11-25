import os
import sys
import logging
from flask import Flask
from config import Config
from extensions import init_extensions, db
from routes.feedback_api import bp as feedback_bp
from routes.admin_api import bp as admin_bp
from routes.task_api import bp as task_bp

sys.path.append(os.path.dirname(__file__))

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    logger.info("🚀 正在初始化 Flask 应用...")
    
    init_extensions(app)
    app.register_blueprint(feedback_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(task_bp)
    
    logger.info("✅ 所有蓝图已注册")
    
    # 健康检查端点 (Railway 需要)
    @app.route('/health')
    def health_check():
        logger.debug("健康检查请求")
        return {'status': 'healthy', 'message': 'Service is running'}, 200
    
    # 创建数据库表（如果不存在）
    with app.app_context():
        db.create_all()
        logger.info("✅ 数据库表初始化完成")
    
    logger.info("🎉 Flask 应用初始化完成")
    
    return app

app = create_app()

if __name__ == "__main__":
    # 本地开发环境
    port = int(os.getenv("PORT", 5000))
    logger.info(f"🌐 启动开发服务器 - 地址: 0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)

