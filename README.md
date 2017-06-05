## CSV file generator

This flask application is developed for generating a csv file from the data sent as https' GET method in the url form
```
url/?var1=value1&var2=value2&......
```

The application is deployed on heroku.

## Built With

* Python version 2.7 is used for programming.
* [Flask](http://flask.pocoo.org) as the application framework.
* [PostgreSQL](https://www.postgresql.org) as the database.
* [Heroku](https://www.heroku.com) as the application deployment platform.

## Quick start

Create a local repository with
```
mkdir csv-file-generator
cd csv-file-generator
git init
```

Create a virtual environment:
```
pip install virtualenv
virtualenv venv
```

Activate virtualenv with
```
source venv/bin/activate
```

Download the project from GitHub with:
```
git clone https://github.com/palashpulsar/csv-file-generator.git
```

Install dependencies with
```
pip install -r requirements.txt
```

Go to [credentials.py](/credentials.py) and include your credential information for your local PostgreSQL database.

Run this app locally as follow:
```
export FLASK_APP=application.py
flask run
```

Then open a browser and enter: 
```
http://127.0.0.1:5000/?var1=value1&var2=value2&......
```

For downloading CSV file from the data, type in a browser:
```
http://127.0.0.1:5000/download
```

For deleting data stored locally in database, type in the browser:
```
http://127.0.0.1:5000/delete
```

## Description

This application is developed as part of a larger data-analytical project. Its purpose is to collect data from GET requests and generate a CSV file out of the saved. This CSV file can then be further used for data-analysis with popular analytical tools such as MATLAB.

A particular example of this application is to receive a vehicle's [On-board Diagnostic Data](https://en.wikipedia.org/wiki/On-board_diagnostics) from a [Torque Pro android app](https://play.google.com/store/apps/details?id=org.prowl.torque&hl=en). The Torque Pro app is configured to send data to a server URL that contains this application. In this case, Heroku platform is used for deploying this app.

The app comprises of three primary functions:

```
from application import home
```
This function corresponds to reading the GET parameters and storing it in database.

```
from application import csv_file
```
This function corresponds to generating and auto-downloading csv file.

```
from application import deleting_content_in_database
```
This function corresponds to deleting data in database.

These primary functions correspond to '/', '/download' and '/delete' urls respectively.

## Heroku Deployment

The application is deployed in heroku.

