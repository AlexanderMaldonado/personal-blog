# app.py
import os
from flask import Flask
from dotenv import load_dotenv
from models import db
from auth import auth_bp
from routes_public import public_bp
from routes_admin import admin_bp

load_dotenv()  # lee el .env antes de todo

def create_app():
    app = Flask(__name__)

    app.secret_key = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
