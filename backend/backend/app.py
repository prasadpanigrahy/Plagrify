import os
from flask import Flask
from auth import auth_bp
from checker import checker_bp
from admin import admin_bp
from database import db
from flask_jwt_extended import JWTManager
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_secret')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev_jwt_secret')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///plagrification.db')

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(checker_bp)
app.register_blueprint(admin_bp)

@app.before_first_request
def create_tables():
    db.create_all()

@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
