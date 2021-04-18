# Chapter 3: Forms
# Section 1: Form Basics
#
# Flask has many tools to make form
#	development easier. Here flask-wtf
#	is used to develop advanced forms.
#

from flask import Flask, render_template
from forms.UserForm import UserForm

app = Flask(__name__)


# Configure key
# !!! Later on this process will be
#	replaced by something more secure. 
app.config['SECRET_KEY'] = "secretkey"


# Setup form view
@app.route("/", methods=["GET", "POST"])
def index():

	username = False
	form = UserForm()

	if form.validate_on_submit():
		username = form.username.data
		form.username.data = ""

	return render_template("index.html", form=form, username=username)


if __name__ == "__main__":
	app.run(debug=True)
