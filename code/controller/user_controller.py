from flask import request, jsonify

from flask_wtf import FlaskForm
from wtforms import StringField

from flask_restplus import Namespace, Resource, fields,reqparse
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime


#from model import db
#from model.user import User
#from model.meal import Meal

from model.user import *
from service.auth_service import authenticated
from marshmallow import Schema, fields as ma_fields, post_load
api = Namespace(name='Users API', path='/api/')

# pagination_arguments = reqparse.RequestParser()
# pagination_arguments.add_argument('page', type=int, required=True)
# pagination_arguments.add_argument('per_page', type=int, required=True,
#                                   choices=[5, 10, 20, 30, 40, 50], default=10)

users = []





class TheUser(object):
    def __init__(self, name, surname,phone_number):
        self.name = name
        self.surname = surname 
        self.phone_number=phone_number

    def __repr__(self):
        # addUser(self.name,self.surname,self.phone_number)
        # user_ime.append(self.name)
        # user_prezime.append(self.surname)
        flag=False
        flag_array=[]
        broj_mob=self.phone_number
        for broj in broj_mob:
            if broj in '0123456789':
                flag=True
                flag_array.append(flag)
            else:
                flag=False
                flag_array.append(flag)
        if False not in flag_array:
            addUser(self.name,self.surname,self.phone_number)
            user_ime.append(self.name)
            user_prezime.append(self.surname)
            user_broj.append(self.phone_number)
            return '{} is the name of user. {} is the surname.{} is phone number'.format(self.name, self.surname,self.phone_number)
        else:
            self.name='0'
            self.surname='0'
            self.phone_number='0'
            return '{} {} {}'.format('0','0','0')
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
    #@api.expect(pagination_arguments, validate=True)
    def get(self):
  
        print("kjhbhjbhbhbhjbhjhjjhghhgbhj")
        users.clear()
        schema = UserSchema(many=True)
        if len(new_added_user_name)!=0 and len(new_added_user_surname)!=0:
            for i in range(len(user_ime)):
                users4data_name.append(user_ime[i])
                users4data_surname.append(user_prezime[i])
                users4data_phonenumber.append(user_broj[i ])
        print("mobiteli......",users4data_phonenumber)
        for i in range (len(users4data_name)):
            u1=TheUser(name=users4data_name[i],surname=users4data_surname[i],phone_number=users4data_phonenumber[i])
            users.append(u1)
        print(users4data_name)
        user_ime.clear()
        user_prezime.clear()
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        # for u in users:
        #     print(u.phone_number)


        return schema.dump(users)

    @api.expect(a_user)
    def post(self):
        schema =UserSchema()
        new_user = schema.load(api.payload)
        print('new user:  ',new_user)
        #new_language['id'] = len(languages) + 1
        #users.append(new_user)
        print(type(new_user.name))
        print(new_user.name)
        ime=new_user.name
        print(type(ime))
        if ime=='0':
            return{'result :' :'The input has to be number'}
        else:
            return {'result' : 'User added'}, 201 































