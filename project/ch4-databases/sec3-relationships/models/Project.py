from application import db


class Project(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text)
	academic = db.Column(db.Boolean)
	subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'),
        nullable=False)

	# One to many relationship Project --> Document
	documents = db.relationship('Document', backref="project", lazy="dynamic")


	def __init__(self, title, subject, academic):

		self.title = title
		self.academic = academic
		self.subject = subject


	def __repr__(self):

		if self.academic:
			return f"{self.title} is in the {self.subject.title} subject and is an academic project ."
		else:
			return f"{self.title} is in the {self.subject.title} subject and is not an academic project ."


	def report_documents(self):

		print(f"{self.title} has the following documents:")
		for document in self.documents:
			print("\t" + document.title)
