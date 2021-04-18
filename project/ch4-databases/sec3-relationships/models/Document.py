from application import db


class Document(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	path = db.Column(db.Text)
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'),
		nullable=False)


	def __init__(self, name, last_name, email,
		company, lead_type):

		self.name = name
		self.path = path
		self.project = project


	def __repr__(self):
		return f"Document {self.name} with path {self.path} is owned by project {self.project}"
