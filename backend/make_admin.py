from server import app
from models import User
from database import db

def make_admin(username):
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if user:
            user.is_admin = True
            db.session.commit()
            print(f"User '{username}' is now an admin.")
        else:
            print(f"User '{username}' not found.")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python make_admin.py <username>")
    else:
        make_admin(sys.argv[1])
