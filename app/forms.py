from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,   BooleanField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User

class Loginform(FlaskForm):
    username    = StringField("Username", validators=[DataRequired()])
    password    = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit      = SubmitField("Sign In")

class RegisterationForm(FlaskForm):
    username    = StringField("Username", validators=[DataRequired()])
    first_name  = StringField("First Name", validators=[DataRequired()])
    last_name   = StringField("Last Name", validators=[DataRequired()])
    email       = StringField("Email", validators=[DataRequired(), Email()])
    password    = PasswordField("Password", validators=[DataRequired()])
    password2   = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit      = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError("Please use a different user name")

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email id")

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')            