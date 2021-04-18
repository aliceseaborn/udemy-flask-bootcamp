# Chapter 1: Flask Basics
# Section 4: Debug Mode
#
# Without debug mode, errors will be handled
#	internally without passing error details
#	to the website user.
#
# As a developer, you need these details. By
#	changing debug=True in app.run(), you can
#	access errors in the browser.
#
# Additionally, if you click the console button
#	on an error in the browser, you can access
#	a Python terminall running in the current
#	session. Provide the debugger pin to the
#	prompt to authenticate the terminal.
#

from flask import Flask
app = Flask(__name__)


# localhost:5000/
@app.route('/')
def index():
	source = "<h1>Welcome to the index.</h1>"

	return source


# localhost:5000/user/<username>
@app.route('/user/<username>')
def user(username):
	source = f"""
	<h1>{username.title()[100]}'s Page.</h1>
	<p>Welcome {username.title()[100]}.</p>
	"""

	return source 


if __name__ == "__main__":
	app.run(debug=True)
