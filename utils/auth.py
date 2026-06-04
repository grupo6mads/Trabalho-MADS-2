from functools import wraps
from flask import session, redirect, url_for

def login_required(role):

    def decorator(f):

        @wraps(f)
        def decorated_function(*args, **kwargs):

            user_role = session.get("role")

            if user_role != role and user_role != "admin":
                return redirect(url_for("index"))

            return f(*args, **kwargs)

        return decorated_function

    return decorator
