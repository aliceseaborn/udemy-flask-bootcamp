# Chapter 2: Templates
# Section 4: Template Inheritance
#
# Most pages on a website are essentially
#	the same page with minor alterations.
#
# Using a base HTML template with the
# 	website features, we can then inherit
#	those features throughout the website.
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
