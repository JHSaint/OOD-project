from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , FloatField
from wtforms.validators import InputRequired , NumberRange
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

    
class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    Username = StringField('Username', validators = [DataRequired()])
    Password = StringField('Password',validators = [DataRequired()])
    account_type = SelectField('Account Type', choices = [('Guild','guild'),('Student','student'),('Sponsor','sponsor')])
    pic = FileField('Profile Picture', validators = [FileRequired(), FileAllowed(['jpg','jpeg','png'], 'Only images please.')])
    submit = SubmitField("Register Account")


class EventForm(FlaskForm):
	name = StringField('Event Name', validators = [DataRequired()])
	date = DateField('Planned Date', validators = [DataRequired()], format='%d/%m/%Y')
	price = StringField('Admissions Price', validators = [DataRequired()])
	sponsors = StringField('List of Sponsors', validators = [DataRequired()])
	event_type = StringField('Type of Event', validators = [DataRequired()])
	location = StringField('Venue', validators = [DataRequired()])
	pic = FileField('Profile Picture', validators = [FileRequired(), FileAllowed(['jpg','jpeg','png'], 'Only images please.')])
	submit = SubmitField("Register Event")

class SupportForm(FlaskForm):
    donation = FloatField('Support',validators = [NumberRange(1,1000000000)])
