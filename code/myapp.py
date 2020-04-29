from flask import Flask
from flask_restplus import Api
from controller import api
#from model import db
#from controller.auth_controller import projects
from model.meal import listAll
from model.user import listAllUsers
from model.reservation import listAllDeskRezervation
from model.reservation import RezervateTable

from app import app

#app = Flask(__name__)

#from . import routes
# load application configuration from config.py
def create_app():
    app.config.from_object('config.DevelopmentConfig')


# initialize database via flask-sqlalchemy
    db.init_app(app)

# initialize rest api via flask-restplus
    api.init_app(app)
    return app
# za jela
listAll()
#za korisnike
listAllUsers()
app.config.from_object('config.DevelopmentConfig')


listAllDeskRezervation()






# initialize database via flask-sqlalchemy
#db.init_app(app)

# initialize rest api via flask-restplus
api.init_app(app)
