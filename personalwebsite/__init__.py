import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail


db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

def create_app_from_config():
    from personalwebsite.config import Config

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from personalwebsite.main.routes import main

    app.register_blueprint(main)

    return app

