from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
#from model import db
#from model.meal import Meal
from model.reservation import *

from service.auth_service import authenticated
from marshmallow import Schema, fields as ma_fields, post_load
api = Namespace(name='Rezervation API', path='/api/rezervationDesk')


rezervations=[]

class TheRezervation(object):
    def __init__(self,number,id_person,rezervated):
        self.id_person=id_person
        self.number=number
        self.rezervated=rezervated

    def __repr__(self):
        r=RezervateTable(self.number,self.id_person,self.rezervated)
        if r=='stol rezerviramo':
            broj_stola.append(self.number)
            id_osobe.append(self.id_person)
            rezervacija.append(self.rezervated)
            return '{} is the number of table. {} is the id person who rezervated.'.format(self.number,self.id_person)
        else :
            self.number=0
            self.id_person=0
            return '{} {}'.format(0,0)

class RezervationSchema(Schema):
    id_person=ma_fields.Integer()
    number=ma_fields.Integer()
    rezervated=ma_fields.String()
    @post_load
    def create_rezervation(self,data,**kwargs):
        return TheRezervation(**data)

#a_rezervation=api.model('Rezervation',{'number': fields.String('The number of table'),'id_person':fields.String('Person who rezervated desk'),'rezervated':fields.String('YES')})
a_rezervation=api.model('Rezervation',{'number': fields.Integer(),'id_person':fields.Integer(),'rezervated':fields.String()})





@api.route('/rezervation')
class Rezervation(Resource):
    #@api.doc(security='apikey')
   # @authenticated
    def get(self):
       
        print('Number of table: ',tabels_number)
        rezervations.clear()
        schema=RezervationSchema(many=True)
        print("broj stola: ",broj_stola)
        if len(addNumberofTable)!=0 and len(addIdPerson)!=0:
            for i in range(len(broj_stola)):
                print(broj_stola[i])
                tabels_number.append(broj_stola[i])
                id_person_rezervations.append(id_osobe[i])
                y_n_rezervation.append(rezervacija[i])
        print(len(tabels_number))
        print(len(rezervacija))
        for i in range(len(tabels_number)):
            rez=TheRezervation(number=tabels_number[i],id_person=id_person_rezervations[i],rezervated=y_n_rezervation[i])
            rezervations.append(rez)
        


        broj_stola.clear()
        id_osobe.clear()
        rezervacija.clear()

        br=0
        stolovi_stari=[]
        stolovi_novi=[]
        d=len(tabels_number)-len(broj_stola)
        for i in range(len(rezervations)):
            if i<=9:
                stolovi_stari.append(rezervations[i])
            else:
                stolovi_novi.append(rezervations[i])
        for k in stolovi_stari:
            for el in stolovi_novi:
                if k.number==el.number:
                    print(k.rezervated)
                    print(el.rezervated)
                    k.rezervated,el.rezervated=el.rezervated,k.rezervated
                    k.id_person,el.id_person=el.id_person,k.id_person
        print('pravo stanje niza: ')
        for el in stolovi_stari:
            print(el.number,"..........",el.rezervated,"........",el.id_person)
                     

        return schema.dump(stolovi_stari)


    @api.expect(a_rezervation)
    def put(self):
        flag=True
        schema=RezervationSchema()
        new=schema.load(api.payload)
        #print(ord(new))
        print(new)
        print(new.number )
        if new.number ==0 and new.id_person==0:
            return {'result ':'Desk is already taken or the input is wrong!'}
        else:
            return {'result ':'Desk reserved'},201











