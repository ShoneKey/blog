# coding:utf-8
import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from blog import create_app, db, login_manager
from blog.models import User, Post, Category, Tag, Role

app= create_app(os.getenv('BLOG_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def make_shell_context():
    return dict(app=app, db=db, Role=Role,User=User, Post=Post, Category=Category, Tag=Tag)

manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()