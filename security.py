from werkzeug.security import safe_str_cmp
from src.models.user import UserModel


def authenticate(email, password):
    user = UserModel.find_by_email(email)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    return UserModel.find_by_id(payload['identity'])
