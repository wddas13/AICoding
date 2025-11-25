from feedback_app.extensions import db
from feedback_app.models import Feedback


class FeedbackService:
    @staticmethod
    def add_feedback(content, contact, ip):
        fb = Feedback(content=content, contact=contact, ip=ip)
        db.session.add(fb)
        db.session.commit()
        return fb

    @staticmethod
    def list_feedback(page, size, keyword=None):
        query = Feedback.query
        if keyword:
            query = query.filter(Feedback.content.contains(keyword))
        query = query.order_by(Feedback.create_time.desc())
        total = query.count()
        items = query.offset((page - 1) * size).limit(size).all()
        pages = (total + size - 1) // size
        return {
            "items": [
                {
                    "id": i.id,
                    "content": i.content,
                    "contact": i.contact,
                    "ip": i.ip,
                    "create_time": i.create_time.isoformat(),
                }
                for i in items
            ],
            "total": total,
            "pages": pages,
            "page": page,
            "size": size,
        }

