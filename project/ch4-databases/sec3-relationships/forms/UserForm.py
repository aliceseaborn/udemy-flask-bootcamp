from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class UserForm(FlaskForm):

	username = StringField("Username:")
	submit = SubmitField("Submit")
