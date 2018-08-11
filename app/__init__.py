from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from app.controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.controllers.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
