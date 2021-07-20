from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    fname = StringField('First Name',
                        validators=[InputRequired(), Length(min=2, max=20)])
    lname = StringField('Last Name',
                        validators=[InputRequired(), Length(min=2, max=20)])
    username = StringField('Username',
                           validators=[InputRequired(), Length(min=2, max=20)])
    email = StringField('Email Address', validators=[InputRequired(), Email()])
    password = PasswordField('Password',
                             validators=[InputRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', validators=[
        InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up!')

    def make_dict(self):
        """
        Takes response to form and converts to dict,
        ready to pass to User class
        """
        info = {
            "fname": self.fname.data,
            "lname": self.lname.data,
            "username": self.username.data,
            "email": self.email.data,
            "password": self.password.data
        }
        return info
