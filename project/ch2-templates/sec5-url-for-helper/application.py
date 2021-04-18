# Chapter 2: Templates
# Section 5: URL for Helper
#
# Hardcoding links in HTML means that
#	if a route changes name you will
#	have to change the name in multiple
#	places.
#
# Using the URL_for() helper, you can
#	pass the names of routes into the
#	HTML, thereby linking Flask routes
#	together.
#

import datetime

from flask import Flask, render_template
app = Flask(__name__)


# localhost:5000/
@app.route('/')
def index():
	return render_template('home.html')


# localhost:5000/
@app.route('/user/<username>')
def user(username):
	return render_template('user.html', username=username)


if __name__ == "__main__":
	app.run(debug=True)
