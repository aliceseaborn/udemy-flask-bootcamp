# Chapter 2: Templates
# Section 6: Forms
#
# This section not only creates a form
#	for user input but also implements
#	
#

import datetime

from flask import Flask, render_template, request
app = Flask(__name__)


# localhost:5000/
@app.route('/')
def index():
	return render_template("index.html")


# localhost:5000/contact
@app.route('/contact')
def contact():
	return render_template("contact.html")


# localhost:5000/
@app.route('/thankyou')
def thank_you():
	firstname = request.args.get("firstname")
	lastname = request.args.get("lastname")
	return render_template("thankyou.html", firstname=firstname, lastname=lastname)


# Error: 404
@app.errorhandler(404)
def page_not_found(e):
	return render_template("error/404.html")


if __name__ == "__main__":
	app.run(debug=True)
