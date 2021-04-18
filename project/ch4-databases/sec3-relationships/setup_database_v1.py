from application import db
from models.User import User
from models.Subject import Subject
from models.Project import Project


db.create_all()


# SUBJECTS
Engineering = Subject("Engineering")
db.session.add(Engineering)

DataScience = Subject("Data Science")
db.session.add(DataScience)

# PROJECTS
DigitalAudioEqualizer = Project(title="Digital Audio Equalizer", academic=True, subject=Engineering)
db.session.add(DigitalAudioEqualizer)

FuzzyLogicClusteringAlgorithm = Project(title="Fuzzy Logic Clustering Algorithm", academic=False, subject=DataScience)
db.session.add(DigitalAudioEqualizer)


# COMMIT AND PRINT
db.session.commit()

print(Engineering)
print(DataScience)
print(DigitalAudioEqualizer)
print(FuzzyLogicClusteringAlgorithm)

Engineering.report_projects()
DataScience.report_projects()
