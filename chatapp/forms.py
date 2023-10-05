from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(min=6, max=24)])
    password = PasswordField(validators=[DataRequired(), Length(min=6, max=16)])
    password2 = PasswordField(validators=[DataRequired(), Length(min=6, max=16)], label='Confirm password')
    first_name = StringField(validators=[DataRequired()])
    last_name = StringField(validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(min=6, max=24)])
    password = PasswordField(validators=[DataRequired(), Length(min=6, max=16)])


