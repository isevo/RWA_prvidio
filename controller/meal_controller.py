from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
#from model import db
#from model.meal import Meal
from model.meal import *

from service.auth_service import authenticated
from marshmallow import Schema, fields as ma_fields, post_load
api = Namespace(name='Meals API', path='/api/')


meals=[]

class TheMeal(object):
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __repr__(self):
        jelo_ime.append(self.name)
        jelo_cijena.append(self.price)
        addArgument(self.name,self.price)
        return '{} is the number of table. {} is the id person who rezervated.'.format(self.name,self.price)

class MealSchema(Schema):
    price=ma_fields.Integer()
    name=ma_fields.String()
    @post_load
    def create_rezervation(self,data,**kwargs):
        return TheMeal(**data)

#a_rezervation=api.model('Rezervation',{'number': fields.String('The number of table'),'id_person':fields.String('Person who rezervated desk'),'rezervated':fields.String('YES')})
a_reservation=api.model('Meal',{'name': fields.String(),'price':fields.Integer()})





@api.route('/meal')
class Mealn(Resource):
    @api.doc(security='apikey')
    @authenticated
    def get(self):
       
        meals.clear()
        schema=MealSchema(many=True)
     
        if len(new_added_meal_name)!=0 and len(new_added_meal_price)!=0:
            for i in range(len(jelo_ime)):
                print(i)
                meals4data_name.append(jelo_ime[i])
                meals4data_price.append(jelo_cijena[i])
               
        
        for i in range(len(meals4data_name)):
            rez=TheMeal(name=meals4data_name[i],price=meals4data_price[i])
            meals.append(rez)
        

        jelo_cijena.clear()
        jelo_ime.clear()

        for el in meals:
            print(el.name,"....",el.price)



        return schema.dump(meals)


    @api.expect(a_reservation)
    def post(self):
      
        schema=MealSchema()
        new=schema.load(api.payload)
        print(new)
        return {'result ':'meal added'},201















