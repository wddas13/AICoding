"""修复数据库表结构"""
from app import app
from extensions import db
from models.task import Task
from models.feedback import Feedback

def fix_database():
    """重建数据库表"""
    with app.app_context():
        print("开始修复数据库...")
        
        # 删除task表并重建
        print("删除旧的task表...")
        db.session.execute(db.text("DROP TABLE IF EXISTS task"))
        db.session.commit()
        
        print("重新创建所有表...")
        db.create_all()
        
        print("数据库修复完成!")
        print("Task表列:", [c.name for c in Task.__table__.columns])

if __name__ == "__main__":
    fix_database()

