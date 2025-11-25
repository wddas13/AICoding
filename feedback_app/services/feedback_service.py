import logging
from feedback_app.extensions import db
from feedback_app.models import Feedback

logger = logging.getLogger(__name__)


class FeedbackService:
    @staticmethod
    def add_feedback(content, contact, ip):
        try:
            logger.info(f"[FeedbackService] 开始添加反馈 - IP: {ip}, 内容长度: {len(content)}")
            
            fb = Feedback(content=content, contact=contact, ip=ip)
            db.session.add(fb)
            db.session.commit()
            
            logger.info(f"[FeedbackService] 反馈添加成功 - ID: {fb.id}, IP: {ip}")
            return fb
        except Exception as e:
            logger.error(f"[FeedbackService] 反馈添加失败 - IP: {ip}, 错误: {str(e)}")
            db.session.rollback()
            raise

    @staticmethod
    def list_feedback(page, size, keyword=None):
        try:
            logger.debug(f"[FeedbackService] 开始查询反馈列表 - page: {page}, size: {size}, keyword: {keyword}")
            
            query = Feedback.query
            if keyword:
                query = query.filter(Feedback.content.contains(keyword))
                logger.debug(f"[FeedbackService] 应用关键词过滤 - keyword: {keyword}")
            
            query = query.order_by(Feedback.create_time.desc())
            total = query.count()
            items = query.offset((page - 1) * size).limit(size).all()
            pages = (total + size - 1) // size
            
            logger.info(f"[FeedbackService] 反馈列表查询成功 - 总数: {total}, 当前页: {page}, 返回: {len(items)} 条")
            
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
        except Exception as e:
            logger.error(f"[FeedbackService] 反馈列表查询失败 - 错误: {str(e)}")
            raise

