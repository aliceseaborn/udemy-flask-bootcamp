from application import db


class User(db.Model):

	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	email = db.Column(db.Text)
	lead_type = db.Column(db.Text)


	def __init__(self, first_name, last_name, email,
		lead_type):

		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.lead_type = lead_type


	def __repr__(self):
		return f"User {self.first_name} {self.last_name} is a {self.lead_type} with email {self.email}"
