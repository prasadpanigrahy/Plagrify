from flask import Flask
from auth import auth_bp
from checker import checker_bp
from admin import admin_bp
from database import db
from flask_jwt_extended import JWTManager
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plagrification.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB and JWT
db.init_app(app)
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(checker_bp)
app.register_blueprint(admin_bp)

# Create tables before the first request
@app.before_first_request
def create_tables():
    db.create_all()

# Inject current year into all templates
@app.context_processor
def inject_now():
    return {'current_year': datetime.now().year}

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
