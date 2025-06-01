from flask import Blueprint, render_template, request, redirect, session
from models import User
from database import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
    return redirect('/login')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = User.query.filter_by(username=request.form['username']).first()
        if u and check_password_hash(u.password, request.form['password']) and not u.banned:
            session['user_id'] = u.id
            return redirect('/dashboard')
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        u = User(username=request.form['username'],
                 password=generate_password_hash(request.form['password']))
        db.session.add(u)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')
