# Chapter 1: Flask Basics
# Section 3: Dynamic Routing
#
# Consider a website with multiple users. You don't want
#	users to collide with other users. Ergo, you can
#	dynamically route users to their page, e.g.
#	
#	site.com/user/unique_user_name
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
	<h1>{username.title()}'s Page.</h1>
	<p>Welcome {username.title()}.</p>
	"""

	return source 


if __name__ == "__main__":
	app.run()
