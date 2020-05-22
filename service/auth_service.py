from flask import request,make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

#from model import db
#from model.user import User
#from model.meal import Meal
from config import secret_key
from controller.auth_controller import*


def authenticated(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token= request.args.get('token')
    	
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message' : 'Token is missing.'}, 401


        if token != tokens[0]:
            print("Ovo je token:{} ".format(token))
            print("Ovo je tok:{} ".format(tokens[0]))
           
            return {'message' : 'Your token is wrong, wrong, wrong!!!'}, 401

        
        print('TOKEN: {}'.format(token))
        return f(*args, **kwargs)

    return decorated