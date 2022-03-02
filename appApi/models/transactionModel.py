from datetime import date
from flask_restx import fields
from appApi.utils import api

# work in progress

transaction = api.model('Transaction', 
{
    'userId': fields.String(readonly=True, description='The task unique identifier'),
    'transactionId': fields.String(required=True, description='The transaction unique identifier'),
    'transactionAmount': fields.Integer(readonly=True, description='Details of the transaction'),
    'transactionState': fields.String(description='The status of current transaction', enum=["Initialized", "Completed"]),
    'date': fields.String(readonly=True, description='The date of the transaction')
})
