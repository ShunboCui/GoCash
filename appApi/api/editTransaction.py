from urllib import request
from flask_restx import Resource
from appApi.utils import api, app
from appApi.models.transactionModel import transaction
from pprint import pprint
from flask import request 
from appApi.pymongo_connect import get_database
import uuid
import datetime

"""
    Edit a transaction that was initiated by the user
    Parameters:
        transaction = {
            "userId" : userId,
            "transactionId": str,
            "transactionAmount": int,
            "transactionState": "Initialized/Completed"
        }
    Returns:
        transaction: transaction Object
"""
class EditTransactionApi(Resource):
    # mod = transaction
    # @api.marshal_with(mod, code=200, mask = {})
    # @api.doc(description="Transaction")
    def put(self):
        #Parse request parameters 
        transactionRequest =  request.json
        userId = transactionRequest["userId"]
        transactionId = transactionRequest["transactionId"]
        transactionAmount = transactionRequest["transactionAmount"]
        transactionState = transactionRequest["transactionState"]

        # #Verify Valid User
        if self.validTransaction(userId, transactionAmount):
            #Create a new transaction entry and save to db
            newTransaction = {
                "userId" : userId,
                "transactionId": transactionId,
                "transactionAmount": transactionAmount,
                "transactionState": transactionState,
                "date": datetime.datetime.now()
            }

            try:
                self.updateTransaction(userId, transactionId, newTransaction)
                newTransaction["date"]= str(newTransaction["date"])
                return newTransaction
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
    updates transaction in the database 
       
    Parameters:
        transaction: the transaction Object to be inserted into the db
    """
    def updateTransaction(self, userId, transactionId, newTransaction):
        db = get_database()
        TransactionInfoCollection = db["transactions"]
        newTransaction = TransactionInfoCollection.replace_one({"$and":[ {"userId":userId}, {"transactionId":transactionId}]}, newTransaction)


