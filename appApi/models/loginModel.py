from flask_restx import fields
from appApi.utils import api

# create a template for json that is populated by api
loginModel = api.model('login',
{
    'data': fields.String(),
    "error": fields.String(),
}

)