from application import db


class Subject(db.Model):

	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.Text)

	# One to many relationship Subject --> Project
	projects = db.relationship('Project', backref="subject", lazy="dynamic")


	def __init__(self, title):
		self.title = title


	def __repr__(self):
		return f"Subject is {self.title}."


	def report_projects(self):

		print(f"{self.title} has the following projects:")
		for project in self.projects:
			print("\t" + project.title)

