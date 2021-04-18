# Chapter 2: Templates
# Section 2: Template Variables
#
# In order to interact with the HTML
#	templates, we can use Jinja.
#
# Jinja will insert variables into the 
#	HTML templates according to several
#	params.
#

import datetime

from flask import Flask, render_template
app = Flask(__name__)


def fetch_metadata():
	last_login = datetime.date.today() - datetime.timedelta(days=1)
	metadata = dict({
			"date":datetime.date.today(),
			"last-login": last_login
		})
	return metadata


# localhost:5000/
@app.route('/<username>')
def index(username="Guest"):
	metadata = fetch_metadata()
	return render_template('variables.html', username=username.title(), metadata=metadata)


if __name__ == "__main__":
	app.run(debug=True)
