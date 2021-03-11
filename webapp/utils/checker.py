from flask import session
from functools import wraps


def check_logged_in(func):
    """Декоратор проверяющий авторизацию пользователя перед почещением страницы."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'Yuo are NOT logged in'

    return wrapper
