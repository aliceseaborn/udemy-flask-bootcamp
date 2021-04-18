# Chapter 1: Flask Basics
# Section 1: Hello World
#

from flask import Flask

# Pass module to Flask
app = Flask(__name__)


# localhost:5000/
@app.route('/')
def index():
	return "<h1>Hello, world!</h1>"


# Execute the application at runtime
if __name__ == "__main__":
	app.run()
