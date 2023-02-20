from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class UserRegisterForm(FlaskForm):
    username = StringField(label = 'username', validators=[DataRequired()])
    email = StringField(label = 'email', validators=[DataRequired()])
    name = StringField(label = 'name', validators=[DataRequired()])
    password1 = PasswordField(label = 'password', validators=[DataRequired()])
    password2 = PasswordField(label = 'confirm password', validators=[DataRequired(), EqualTo('password1')])