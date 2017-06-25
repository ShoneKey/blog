# coding:utf-8

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
login_manager=LoginManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from admin import admin
    from .admin.views import MyModelView,MyAdminIndexView
    from .models import Role, User, Post, Category, Tag
    admin.init_app(app, index_view=MyAdminIndexView())
    admin.add_view(MyModelView(Role, db.session))
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(Post, db.session))
    admin.add_view(MyModelView(Category, db.session))
    admin.add_view(MyModelView(Tag, db.session))

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app