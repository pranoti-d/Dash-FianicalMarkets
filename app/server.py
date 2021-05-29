import atexit

import sqlalchemy
from config import Config
from flask import Flask, render_template
#from flask_mysqldb import MySQL
#from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
#from flask_sqlalchemy import SQLAlchemy



AppServer = Flask(__name__)
CORS(AppServer, support_credentials=True)

AppServer.config.from_object(Config)

#db = SQLAlchemy(AppServer)



from app import routes
