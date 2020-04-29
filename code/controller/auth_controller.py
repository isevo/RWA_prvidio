from flask import request, jsonify,make_response
from flask_restplus import Namespace, Resource, fields
#from service.auth_service import Auth
#from service.auth_service import authenticated
import jwt,datetime,secrets

api = Namespace(name='Auth API', path='/api/auth')

from app import app




app.config['SECRET_KEY']='SecretKey'
tokens=[]
@app.route('/login')
def login():
    auth=request.authorization
    if auth and auth.password=='password7':
        token=jwt.encode({'user':auth.username,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=1)},app.config['SECRET_KEY'], algorithm='HS256')
        tokens.clear()
        lozinka=secrets.token_urlsafe(45)
        print(lozinka)
        print(token)
        tokens.append(lozinka)
        
        #return jsonify({'user':token.decode('UTF-8')})
        return lozinka
    #    return  auth.password
       

    return make_response('Counld not verify',401,{'www-Authenticate':'Basic realm= "Login Required"'})

