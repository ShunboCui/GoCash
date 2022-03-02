from datetime import date
from flask_restx import fields
from appApi.utils import api

# work in progress

user = api.model('User', 
{
    'userId': fields.String(readonly=True, description='The task unique identifier'),
    'userName': fields.String(readonly=True, description='The username'),
    'firstName': fields.String(readonly=True, description='The firstName'),
    'lastName': fields.String(readonly=True, description='The lastName'),
    'balanceAmount': fields.Integer(readonly=True, description='Details of the user account balance'),
    'email': fields.String(readonly=True, description='email'),
    'userPass': fields.String(readonly=True, description='password'),
})
