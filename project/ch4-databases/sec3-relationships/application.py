# Chapter 4: Databases
# Section 2: Flask Migrate
#
# Making changes to the model is not
#	simple because adjusting the code
#	will not automatically fix the
#	database table.
#
# However flask migrate can push
#	these model changes to the
#	database for you.
#

from os import path
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from forms.UserForm import UserForm


database_directory = path.join(path.abspath(path.dirname(__file__)), "database")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + path.join(database_directory, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)


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
