from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import socket
import urllib

application = Flask(__name__)
params = urllib.parse.quote_plus(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={socket.gethostname()};DATABASE=bling;Trusted_Connection=yes;')
application.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_ECHO'] = True
application.config["TEMPLATES_AUTO_RELOAD"] = True 
db = SQLAlchemy(application)