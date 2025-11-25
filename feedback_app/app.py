import os
import sys
from flask import Flask
from config import Config
from extensions import init_extensions, db
from routes.feedback_api import bp as feedback_bp
from routes.admin_api import bp as admin_bp
from routes.task_api import bp as task_bp

sys.path.append(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_extensions(app)
    app.register_blueprint(feedback_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(task_bp)
    
    # 健康检查端点 (Railway 需要)
    @app.route('/health')
    def health_check():
        return {'status': 'healthy', 'message': 'Service is running'}, 200
    
    # 创建数据库表（如果不存在）
    with app.app_context():
        db.create_all()
        print("✅ 数据库表初始化完成")
    
    return app

app = create_app()

if __name__ == "__main__":
    # 本地开发环境
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

