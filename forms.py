from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, Optional


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(granular_message=True), Length(min=5, max=128)])
    # gnarly regex which basically just checks for one lower case, one upper case, a digit, a special character, and 8 characters minimum in the string
    password = PasswordField('Password', validators=[DataRequired(), Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    reminder = StringField('Reminder', validators=[Optional()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Recover my password')

