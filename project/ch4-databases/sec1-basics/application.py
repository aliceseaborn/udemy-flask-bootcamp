# Chapter 4: Databases
# Section 1: Basics
#
# ...
#

from os import path

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms.UserForm import UserForm


database_directory = path.join(path.abspath(path.dirname(__file__)), "database")
print(database_directory)

app = Flask(__name__)

# Setup the database location
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + path.join(database_directory, 'data.sqlite')

# Do not track all database updates
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Pass the application to the SQLAlchemy instance
db = SQLAlchemy(app)


# localhost:5000/
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
