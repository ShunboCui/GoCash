from urllib import request
from flask_restx import Resource
from appApi.utils import api, app
from appApi.models.transactionModel import transaction
from pprint import pprint
from flask import request 
from appApi.pymongo_connect import get_database
import datetime
from bson.json_util import dumps
from bson.json_util import loads
from bson import json_util
import json
import uuid


"""
    Creates a transaction that was initiated by the user
    Parameters:
        Json: {
            "userId": "userid1",
            "transactionAmount": 123
        }
    Returns:
        transaction: transaction Object
"""
class CreateTransactionApi(Resource):
    # mod = transaction
    # @api.marshal_with(mod, code=200, mask = {})
    # @api.doc(description="Transaction")
    def post(self):
        #Parse request parameters 
        transactionRequest =  request.json
        userId = transactionRequest["userId"]
        transactionAmount = transactionRequest["transactionAmount"]
        # #Verify Valid User

        if self.validTransaction(userId, transactionAmount):
            #Create transaction entry and save to db
            transaction = {
                "userId" : userId,
                "transactionId": str(uuid.uuid1()),
                "transactionAmount": transactionAmount,
                "transactionState": "Initialized",
                "date": datetime.datetime.now()
            }

            try:
                self.insertTransaction(transaction)
                transaction.pop("_id")
                transaction["date"]= str(transaction["date"])
                return transaction
            except Exception as e:
                return "Failed to save into DB, transaction discarded", 500
        else:
            return "Invalid Transaction Request", 404


    """
    Checks whether a transaction is valid
    Parameters:
        userId: the unique identification name for the user <str>
        transactionAmount: amount of money needs to take out <int>

    Returns:
        True/False <boolean>
    """
    def validTransaction(self, userId, transactionAmount):
        db = get_database()
        UserInfoCollection = db["user_account"]
        user = UserInfoCollection.find_one({"userId": userId})
        if user == None or user["balanceAmount"] < transactionAmount or transactionAmount < 0:
            return False
        else:
            return True


    """
    inserts transaction in the database 
       
    Parameters:
        transaction: the transaction Object to be inserted into the db
    """
    def insertTransaction(self, transaction):
        db = get_database()
        TransactionInfoCollection = db["transactions"]
        TransactionInfoCollection.insert_one(transaction)