# Chapter 1: Flask Basics
# Section 2: Multiple Routes
#

from flask import Flask
app = Flask(__name__)


# localhost:5000/
@app.route('/')
def index():
	source = "<h1>Welcome to the index.</h1>"

	return source


# localhost:5000/info
@app.route('/info')
def info():
	source = """
	<h1>Information.</h1>
	<p>Written by Alice Seaborn.</p>
	"""

	return source 


if __name__ == "__main__":
	app.run()
