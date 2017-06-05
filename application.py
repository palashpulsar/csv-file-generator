from flask import Flask, request, jsonify, json, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
import csv

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Model here
class Data_Table(db.Model):
	__tablename__ = 'data_table'
	id = db.Column(db.Integer, primary_key=True)
	data = db.Column(JSON)
	def __init__(self, data):
		self.data=data
	def __repr__(self):
		return '<json data: %r>' % self.data

# Views here
@app.route('/')
def home():
	"""The following function retrieves data in GET and stores it in a PostgreSQL database
	"""
	all_args = json.dumps(request.args.to_dict())
	new_data = Data_Table(all_args)
	db.session.add(new_data)
	db.session.commit()	
	return jsonify(request.args.to_dict())

@app.route('/download')
def csv_file():
	"""The following function generates a csv file
	"""
	filename = 'folder/csv_file.csv'
	data = Data_Table.query.all()
	[data_keys, data_json] = determining_KeysNData(data)
	with open(filename, 'wb') as output_file:
		dict_writer = csv.DictWriter(output_file, data_keys)
		dict_writer.writeheader()
		dict_writer.writerows(data_json)
	return send_file(filename, as_attachment=True)

@app.route('/delete')
def deleting_content_in_database():
	"""This function deletes all elements in database.
	"""
	data = Data_Table.query.all()
	for item in data:
		db.session.delete(item)
		db.session.commit()
	return "Successful deletion of data in database"

def determining_KeysNData(data):
	"""This function determines the keys present in the database
	"""
	data_keys = []
	data_json = []
	for item in data:
		data_json.append(json.loads(item.data))
		for element in json.loads(item.data):
			if element not in data_keys:
				data_keys.append(element)
	return [data_keys, data_json]
