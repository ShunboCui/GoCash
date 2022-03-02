from urllib import request
from flask_restx import Resource
from appApi.utils import api, app
from appApi.models.transactionModel import transaction
from pprint import pprint
from flask import request 
from appApi.pymongo_connect import get_database
import uuid


"""
    Returns all transactions done by the user
    Parameters:
        userId: unique user identifier
    Returns:
        userTransactionsList: list of all transactions
"""
class GetAllTransactionsApi(Resource):
    # mod = transaction
    # @api.marshal_with(mod, code=200, mask = {})
    @api.doc(description="get all transactions from specific user")
    def get(self, userId):

        #Verify Valid User
        if self.userExists(userId):
            try:
                userTransactionsList = self.getUserTransactions(userId)
                return userTransactionsList
            except Exception as e:
                return "Failed to find transactions", 500
        else:
            return "Invalid user", 404


    """
    Checks whether a user already exists in the database 
    Parameters:
        userId: the unique identification name for the user <str>
    Returns:
        True/False <boolean>
    """
    def userExists(self, userId):
        db = get_database()
        UserInfoCollection = db["user_account"]
        if UserInfoCollection.find_one({"userId": userId}):
            return True
        else:
            return False


    """
    Obtains all documents from the db of the specified user 
    Parameters:
        userId: the unique identification name for the user <str>
    Returns:
        userTransactionsList: list containing all transactions under the user
    """
    def getUserTransactions(self, userId):
        userTransactionsList = []

        db = get_database()
        TransactionInfoCollection = db["transactions"]
        transactionsCursor = TransactionInfoCollection.find({"userId": userId})  #mongodb returns a cursor object, which we must iterate through, or else is not serializable 
        for i in transactionsCursor:
            i.pop("_id")    #need to manually pop _id, as it is not serializable, and too lazy to find other methods, plus we dont need this
            i["date"]= str(i["date"])
            userTransactionsList.append(i)
        return userTransactionsList




