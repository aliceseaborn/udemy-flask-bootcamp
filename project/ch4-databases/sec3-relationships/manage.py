from application import app, db
from manager import Manager
import os

manager = Manager()


@manager.command
def initialize():
	"""Initialize the SQLite3 database."""

	db.create_all()

	os.system("export FLASK_APP=application.py")
	os.system("flask db init")
	

@manager.command
def migration():
	"""Migrate domain object changes to SQLite3 database."""

	os.system(f"flask db migrate")
	os.system("flask db upgrade")
