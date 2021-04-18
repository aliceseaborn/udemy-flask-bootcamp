from application import db
from models.User import User
from models.Subject import Subject
from models.Project import Project
from models.Document import Document


Subject.query.delete()
Project.query.delete()


# CREATE DOMAIN OBJECTS
Engineering = Subject("Engineering")
DataScience = Subject("Data Science")

DigitalAudioEqualizer = Project(title="Digital Audio Equalizer", academic=True,
	subject=Engineering)
FuzzyLogicClusteringAlgorithm = Project(title="Fuzzy Logic Clustering Algorithm",
	academic=False, subject=DataScience)


# ADD AND COMMIT
db.session.add_all([Engineering, DataScience, DigitalAudioEqualizer,
	FuzzyLogicClusteringAlgorithm])
db.session.commit()


# PRINT
print(Subject.query.all())


# CREATE RELATIONSHIPS

#	Query project by name
digital_audio_equalizer = Project.query.filter_by(
	name="Digital Audio Equalizer").first

#	Create new subject, owning project
engineering = Subject("Applications", digital_audio_equalizer.id)

#	Create documents, owned by project
project_proposal = Document("Novel MATLAB-driven Application for Audio Equalization",
	"/projects/digital_audio_equalizer/proposal.pdf", DigitalAudioEqualizer)
 = Document("MATLAB-driven Application for Audio Equalization",
	"/projects/digital_audio_equalizer/proposal.pdf", DigitalAudioEqualizer)
