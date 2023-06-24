from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()


def create_app():
    from personalwebsite.config import Config

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
#   login_manager.init_app(app)
    mail.init_app(app)

    from personalwebsite.main.routes import main
    from personalwebsite.logger.routes import logger
    app.register_blueprint(main)
    app.register_blueprint(logger)

    return app

