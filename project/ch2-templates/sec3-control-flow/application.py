# Chapter 2: Templates
# Section 3: Template Control Flow
#
# Jinja can pass variables to the 
#	HTML templates.
#
# Jinja can also handle control flow
#	statements such as conditionals
#	and looping statements.
#
# Imagine you passed a list to the
#	template. You can then iterate
#	through the list and format the
#	output as a list, for example.
#

import datetime

from flask import Flask, render_template
app = Flask(__name__)


def fetch_metadata():
	last_login = datetime.date.today() - datetime.timedelta(days=1)
	metadata = dict({
			"date":datetime.date.today(),
			"last-login": last_login,
			"activity": [
				{
					"type": "blog",
					"date": datetime.date.today() - datetime.timedelta(days=1),
					"title": "More pain.",
					"content": """To those human beings who are of any concern to me I wish suffering, desolation, sickness, ill-treatment, indignities—I wish that they should not remain unfamiliar with profound self-contempt, the torture of self-mistrust, the wretchedness of the vanquished: I have no pity for them, because I wish them the only thing that can prove today whether one is worth anything or not—that one endures."""
				},
				{
					"type": "blog",
					"date": datetime.date.today() - datetime.timedelta(days=5),
					"title": "Existence is pain",
					"content": """Life is pain, your highness. Anyone that says differently is selling something."""
				},
				{
					"type": "blog",
					"date": datetime.date.today() - datetime.timedelta(days=9),
					"title": "Darrida",
					"content": """I speak only one language, and it is not my own."""
				}
			]
		})
	return metadata


# localhost:5000/
@app.route('/<username>')
def index(username="Guest"):
	metadata = fetch_metadata()
	return render_template('control-flow.html', username=username.title(), metadata=metadata)


if __name__ == "__main__":
	app.run(debug=True)
