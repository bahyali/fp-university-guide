from functools import wraps
from flask import redirect
from flask_login import current_user


def redirect_if_authenticated(func):
    @wraps(func)
    def _inner(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect('/')
        return func(*args, **kwargs)

    return _inner
