import os
from credentials import user, password, database_name

if os.environ.get('DATABASE_URL') is None:
	SQLALCHEMY_DATABASE_URI = "postgresql://" + user + ":" + password + "@localhost/" + database_name
else:
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
