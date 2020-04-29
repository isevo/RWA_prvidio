from flask_restplus import Api

from .auth_controller import api as auth_ns
from .user_controller import api as user_ns
from .meal_controller import api as meal_ns
from .desk_rezervation import api as rez_ns
#from .order_controller import api as ord_ns

authorizations = {
    'apikey' : {
        'type' : 'apiKey',
        'in' : 
        'header',
        'name' : 'X-API-KEY'
    }
}

api = Api(
    title='Todo API',
    version='1.0.0',
    description='Sveučilište u Zadru - Studij informacijske tehnologije - Razvoj web aplikacija',
    contact='sbuljat@unizd.hr',
    authorizations=authorizations,
    serve_challenge_on_401=False
)

api.add_namespace(auth_ns)
api.add_namespace(user_ns)
api.add_namespace(meal_ns)
api.add_namespace(rez_ns)
#api.add_namespace(ord_ns)