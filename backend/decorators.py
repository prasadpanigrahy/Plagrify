from functools import wraps
from flask import session, redirect, url_for, abort
from models import User

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('auth.login'))  # redirect to login if not logged in

        user = User.query.get(user_id)
        if not user or not user.is_admin:
            # Optionally abort with 403 Forbidden or redirect somewhere safe
            return abort(403)  # forbidden access

        return f(*args, **kwargs)
    return decorated_function
