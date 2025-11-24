from flask_jwt_extended import jwt_required, get_jwt_identity


def admin_required():
    return jwt_required()


def current_admin():
    return get_jwt_identity()

