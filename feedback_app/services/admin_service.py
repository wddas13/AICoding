from flask import current_app
from flask_jwt_extended import create_access_token


class AdminService:
    @staticmethod
    def authenticate(username, password):
        cfg_user = current_app.config.get("ADMIN_USERNAME")
        cfg_pass = current_app.config.get("ADMIN_PASSWORD")
        if username == cfg_user and password == cfg_pass:
            token = create_access_token(identity=username)
            return token
        return None
