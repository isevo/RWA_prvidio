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
api = Namespace(name='Rezervation API', path='/api/')


reservations=[]

class TheReservation(object):
    def __init__(self,number,id_person,reserved):
        self.id_person=id_person
        self.number=number
        self.reserved=reserved

    def __repr__(self):
        r=RezervateTable(self.number,self.id_person,self.reserved)
        if r=='stol rezerviramo':
            broj_stola.append(self.number)
            id_osobe.append(self.id_person)
            rezervacija.append(self.reserved)
            return '{} is the number of table. {} is the id person who reserved.'.format(self.number,self.id_person)
        else :
            self.number=0
            self.id_person=0
            return '{} {}'.format(0,0)

class ReservationSchema(Schema):
    id_person=ma_fields.Integer()
    number=ma_fields.Integer()
    reserved=ma_fields.String()
    @post_load
    def create_reservation(self,data,**kwargs):
        return TheReservation(**data)

#a_rezervation=api.model('Rezervation',{'number': fields.String('The number of table'),'id_person':fields.String('Person who rezervated desk'),'rezervated':fields.String('YES')})
a_reservation=api.model('Reservation',{'number': fields.Integer(),'id_person':fields.Integer(),'reserved':fields.String()})





@api.route('/reservation')
class Reservation(Resource):
    @api.doc(security='apikey')
    @authenticated
    def get(self):
       
        print('Number of table: ',tabels_number)
        reservations.clear()
        schema=ReservationSchema(many=True)
        print("broj stola: ",broj_stola)
        if len(addNumberofTable)!=0 and len(addIdPerson)!=0:
            for i in range(len(broj_stola)):
                print(broj_stola[i])
                tabels_number.append(broj_stola[i])
                id_person_reservations.append(id_osobe[i])
                y_n_reservation.append(rezervacija[i])
        print(len(tabels_number))
        print(len(rezervacija))
        for i in range(len(tabels_number)):
            rez=TheReservation(number=tabels_number[i],id_person=id_person_reservations[i],reserved=y_n_reservation[i])
            reservations.append(rez)
        


        broj_stola.clear()
        id_osobe.clear()
        rezervacija.clear()

        br=0
        stolovi_stari=[]
        stolovi_novi=[]
        d=len(tabels_number)-len(broj_stola)
        for i in range(len(reservations)):
            if i<=9:
                stolovi_stari.append(reservations[i])
            else:
                stolovi_novi.append(reservations[i])
        for k in stolovi_stari:
            for el in stolovi_novi:
                if k.number==el.number:
                    print(k.reserved)
                    print(el.reserved)
                    k.reserved,el.reserved=el.reserved,k.reserved
                    k.id_person,el.id_person=el.id_person,k.id_person
        print('pravo stanje niza: ')
        for el in stolovi_stari:
            print(el.number,"..........",el.reserved,"........",el.id_person)
                     

        return schema.dump(stolovi_stari)


    @api.expect(a_reservation)
    def put(self):
        flag=True
        schema=ReservationSchema()
        new=schema.load(api.payload)
        #print(ord(new))
        print(new)
        print(new.number )
        if new.number ==0 and new.id_person==0:
            return {'result ':'Desk is already taken or the input is wrong!'}
        else:
            return {'result ':'Desk reserved'},201











