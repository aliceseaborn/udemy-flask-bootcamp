# Chapter 3: Forms
# Section 3: Flash Alerts
#
# Flask has a built-in ability to
#	alerts users given some stimulus.
#	Here we demonstrate how to alert
#	a user upon form submission.
#
#

from flask import (Flask, render_template, session,
	redirect, url_for, flash)
from forms.ContactForm import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"


@app.route("/", methods=["GET", "POST"])
def index():

	form = ContactForm()

	if form.validate_on_submit():
		session['firstname'] = form.firstname.data
		session['lastname'] = form.lastname.data
		session['email'] = form.email.data
		session['lead_type'] = form.lead_type.data
		session['message'] = form.message.data

		# Alert user of form submission
		flash("Contact request received.")

		return redirect(url_for('index'))

	return render_template("index.html", form=form)


if __name__ == "__main__":
	app.run(debug=True)
