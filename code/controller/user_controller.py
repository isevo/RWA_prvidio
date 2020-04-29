from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

#from model import db
#from model.user import User
#from model.meal import Meal

from model.user import *
from service.auth_service import authenticated
from marshmallow import Schema, fields as ma_fields, post_load
api = Namespace(name='Users API', path='/api/users')



users = []
class TheUser(object):
    def __init__(self, name, surname,phone_number):
        self.name = name
        self.surname = surname 
        self.phone_number=phone_number

    def __repr__(self):
        addUser(self.name,self.surname,self.phone_number)
        user_ime.append(self.name)
        user_prezime.append(self.surname)
        user_broj.append(self.phone_number)
        return '{} is the name of user. {} is the surname.{} is phone number'.format(self.name, self.surname,self.phone_number)

class UserSchema(Schema):
    name = ma_fields.String()
    surname = ma_fields.String()
    phone_number=ma_fields.String()
    @post_load
    def create_User(self, data,**kwargs):
        return TheUser(**data)
 

 
a_user = api.model('User', {'name' : fields.String('The name.'), 'surname' : fields.String('The surname'),'phone_number': fields.String('000-000-000')})



#python = {'language' : 'Python', 'id' : 1}
#Mate = TheUser(name='Mate', surname='Matic')
#users.append(Mate)



@api.route('/User')
class User(Resource):

    #@api.marshal_with(a_language, envelope='the_data')
    @api.doc(security='apikey')
    @authenticated
    def get(self):
        print("kjhbhjbhbhbhjbhjhjjhghhgbhj")
        users.clear()
        schema = UserSchema(many=True)
        if len(new_added_user_name)!=0 and len(new_added_user_surname)!=0:
            for i in range(len(user_ime)):
                users4data_name.append(user_ime[i])
                users4data_surname.append(user_prezime[i])
                users4data_phonenumber.append(users4data_phonenumber[i])
        for i in range (len(users4data_name)):
            u1=TheUser(name=users4data_name[i],surname=users4data_surname[i],phone_number=users4data_phonenumber[i])
            users.append(u1)
        print(users4data_name)
        user_ime.clear()
        user_prezime.clear()
        



        return schema.dump(users)

    @api.expect(a_user)
    def post(self):
        schema =UserSchema()
        new_user = schema.load(api.payload)
        print('new user:  ',new_user)
        #new_language['id'] = len(languages) + 1
        #users.append(new_user)
        return {'result' : 'User added'}, 201 































