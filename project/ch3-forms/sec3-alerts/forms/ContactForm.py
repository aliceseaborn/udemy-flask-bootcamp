from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,
	DateTimeField, RadioField, SelectField,
	TextField, TextAreaField, SubmitField)
from wtforms.fields.html5 import EmailField
from wtforms.validators import (DataRequired,
	Email)


class ContactForm(FlaskForm):

	firstname = StringField("First Name", validators=[DataRequired()])
	lastname = StringField("Last Name", validators=[DataRequired()])
	email = EmailField("Email", [DataRequired(), Email()])
	lead_type = RadioField("What best describes your relationship to me?",
		choices=[("lead_employer", "Employer"), ("lead_collaborator", "Collaborator"),
		("lead_other", "Other")], validators=[DataRequired()])
	message = TextAreaField()
	submit = SubmitField("Submit")
