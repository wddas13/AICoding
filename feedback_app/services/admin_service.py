import logging
from flask import current_app
from flask_jwt_extended import create_access_token

logger = logging.getLogger(__name__)


class AdminService:
    @staticmethod
    def authenticate(username, password):
        try:
            logger.debug(f"[AdminService] 开始验证管理员凭据 - 用户名: {username}")
            
            cfg_user = current_app.config.get("ADMIN_USERNAME")
            cfg_pass = current_app.config.get("ADMIN_PASSWORD")
            
            if username == cfg_user and password == cfg_pass:
                logger.info(f"[AdminService] 管理员凭据验证成功 - 用户名: {username}")
                token = create_access_token(identity=username)
                logger.debug(f"[AdminService] JWT Token 生成成功 - 用户名: {username}")
                return token
            
            logger.warning(f"[AdminService] 管理员凭据验证失败 - 用户名: {username}")
            return None
        except Exception as e:
            logger.error(f"[AdminService] 管理员认证异常 - 用户名: {username}, 错误: {str(e)}")
            raise
