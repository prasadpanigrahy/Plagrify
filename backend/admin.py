from flask import Blueprint, render_template, session, redirect, request, url_for, abort
from .models import Upload, User
from .database import db
from datetime import datetime
from .decorators import admin_required  # make sure this is defined as shown earlier

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/admin', methods=['GET'])
@admin_required   # <---- restrict access here
def admin_dashboard():
    query = Upload.query
    users = User.query.all()

    # filters
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    min_score = request.args.get('min_score')
    user_id = request.args.get('user_id')

    if date_from:
        try:
            dt_from = datetime.strptime(date_from, '%Y-%m-%d')
            query = query.filter(Upload.created_at >= dt_from)
        except ValueError:
            pass
    if date_to:
        try:
            dt_to = datetime.strptime(date_to, '%Y-%m-%d')
            query = query.filter(Upload.created_at <= dt_to)
        except ValueError:
            pass

    if min_score:
        try:
            min_score_val = float(min_score) / 100
            query = query.filter(Upload.similarity_score >= min_score_val)
        except ValueError:
            pass

    if user_id:
        try:
            uid = int(user_id)
            query = query.filter(Upload.user_id == uid)
        except ValueError:
            pass

    uploads = query.order_by(Upload.created_at.desc()).all()
    return render_template('admin/dashboard.html', uploads=uploads, users=users, all_users=users)


@admin_bp.route('/admin/ban/<int:user_id>', methods=['POST'])
@admin_required  # <---- restrict access here
def ban_user(user_id):
    user = User.query.get(user_id)
    if user:
        user.banned = True
        db.session.commit()
    return redirect(url_for('admin.admin_dashboard'))


@admin_bp.route('/admin/delete_upload/<int:upload_id>', methods=['POST'])
@admin_required  # <---- restrict access here
def delete_upload(upload_id):
    upload = Upload.query.get(upload_id)
    if upload:
        db.session.delete(upload)
        db.session.commit()
    return redirect(url_for('admin.admin_dashboard'))
