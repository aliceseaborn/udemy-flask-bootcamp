# Chapter 3: Forms
# Section 2: Form Fields
#
# This section details the fields
#	available from wtforms as well as
#	the validators to control what
#	input is acceptable from users.
#

from flask import (Flask, render_template, session,
	redirect, url_for)
from forms.ContactForm import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"


@app.route("/", methods=["GET", "POST"])
def index():

	form = ContactForm()

	if form.validate_on_submit():
		# Add data to user's session
		session['firstname'] = form.firstname.data
		session['lastname'] = form.lastname.data
		session['email'] = form.email.data
		session['lead_type'] = form.lead_type.data
		session['message'] = form.message.data

		# Redirect on submit
		return redirect(url_for('thankyou'))

	return render_template("index.html", form=form)


@app.route("/thankyou")
def thankyou():
	return render_template("thankyou.html")


if __name__ == "__main__":
	app.run(debug=True)
