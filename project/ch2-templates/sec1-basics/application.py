# Chapter 2: Templates
# Section 1: Template Basics
#
# Realistically, hardcoding HTML strings in
#	a Flask application is not good practice.
#
# Using a folder named /templates, HTML can
#	be stored and linked to routes within the
#	Flask application.
#

from flask import Flask, render_template
app = Flask(__name__)


# localhost:5000/
@app.route('/')
def index():
	return render_template('basic.html')


if __name__ == "__main__":
	app.run(debug=True)
