from datetime import datetime

from feedback_app.extensions import db


class Feedback(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    contact = db.Column(db.String(255))
    ip = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

