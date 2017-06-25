# coding:utf-8
from flask_admin import Admin


from .views import MyModelView, MyAdminIndexView
admin = Admin(name='my_blog', base_template='admin/my_master.html',template_mode='bootstrap3')

