from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from models import User
from database import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def home():
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            if user.banned:
                flash('Your account has been banned. Please contact support.', 'danger')
            elif check_password_hash(user.password, password):
                session['user_id'] = user.id
                flash('Login successful!', 'success')
                return redirect(url_for('checker.dashboard'))

            else:
                flash('Invalid credentials. Please try again.', 'danger')
        else:
            flash('User not found.', 'warning')
            
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please log in.', 'danger')
            return redirect(url_for('auth.login'))

        new_user = User(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
