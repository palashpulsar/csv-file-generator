import os
from credentials import user, password

if os.environ.get('DATABASE_URL') is None:
	SQLALCHEMY_DATABASE_URI = "postgresql://" + user + ":" + password + "@localhost/csv_flask"
else:
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
