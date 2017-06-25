# coding:utf-8
from werkzeug.security import check_password_hash
from wtforms import form, fields, validators
from wtforms.validators import DataRequired


# Define login and registration forms (for flask-login)
from blog.models import User


class LoginForm(form.Form):
    username = fields.StringField(validators=[DataRequired()])
    password = fields.PasswordField(validators=[DataRequired()])

    def validate_login(self, field):
        user = self.get_user()
        if user is None:
            raise validators.ValidationError('Invalid user')
        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
            # to compare plain text passwords use
            # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return User.query.filter_by(username=self.username.data).first()


class RegistrationForm(form.Form):
    username = fields.StringField(validators=[DataRequired()])
    email = fields.StringField(validators=[DataRequired()])
    password = fields.PasswordField(validators=[DataRequired()])

    def validate_login(self, field):
        if User.query.filter_by(login=self.email.data).count() > 0:
            raise validators.ValidationError('Duplicate username')

