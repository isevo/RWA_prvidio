from flask import Flask
from flask_restplus import Api
from controller import api
#from model import db
#from controller.auth_controller import projects
from model.meal import listAll
from model.user import listAllUsers
from model.reservation import listAllDeskReservation
from model.reservation import ReservateTable

from app import app


app.config['SWAGGER_UI_JSONEDITOR']=True
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


listAllDeskReservation()






# initialize database via flask-sqlalchemy
#db.init_app(app)

# initialize rest api via flask-restplus
api.init_app(app)


if __name__ == '__main__':
    app.run()
