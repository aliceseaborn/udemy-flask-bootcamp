from application import db
from models.User import User


# Creates all tables
db.create_all()


# CREATE

Lockheed = User("Lockheed", "Nartin", "recruitment@lmco.com", "Employer")
db.session.add(Lockheed)

Northrop = User("Northrop", "Grumman", "recruitment@ng.com", "Employer")
db.session.add(Northrop)

db.session.commit()
print(f"Created {Lockheed.first_name} {Lockheed.last_name} with ID {Lockheed.id}")
print(f"Created {Northrop.first_name} {Northrop.last_name} with ID {Northrop.id}")


# READ

all_users = User.query.all()
print(f"Users in database: \n{all_users}")


# UPDATE

print("Updating spelling of Lockheed Martin...")
first_user = User.query.get(1)
first_user.last_name = "Martin"
db.session.add(first_user)
db.session.commit()

all_users = User.query.all()
print(f"Users in database: \n{all_users}")


# DESTROY

print("Deleting second user...")
second_user = User.query.get(2)
db.session.delete(second_user)
db.session.commit()

all_users = User.query.all()
print(f"Users in database: \n{all_users}")
