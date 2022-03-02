from urllib import request
from flask_restx import Resource
from appApi.utils import api, app
from appApi.models.transactionModel import transaction
from pprint import pprint
from flask import request 
from appApi.pymongo_connect import get_database
import uuid


"""
    Deletes a transactions for a specific user
    Parameters:
        Json: {
            "userId": "userid1",
            "transactionId": "b64b6ef3-7982-11ec-b66a-7085c243a619"
        }
    Returns:
        userTransactionsList: list of all transactions
"""
class DeleteTransactionApi(Resource):
    # mod = transaction
    # @api.marshal_with(mod, code=200, mask = {})
    @api.doc(description="delete specific transaction")
    def delete(self):
        #deserialize Json
        transactionRequest =  request.json
        userId = transactionRequest["userId"]
        transactionId = transactionRequest["transactionId"]

        #Verify Valid User
        if self.userExists(userId):
            try:
                if(self.deleteUserTransaction(userId, transactionId)):
                    return "Transaction successfully deleted", 200
                else:
                    return "Could not find transaction", 404
            except Exception as e:
                return "Db error", 500
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
    Deletes specific transaction initiated by the user  
    Parameters:
        userId: the unique identification name for the user <str>
        transactionId: unique identification code for the transaction
    Returns:
        userTransactionsList: list containing all transactions under the user
    """
    def deleteUserTransaction(self, userId, transactionId):

        db = get_database()
        TransactionInfoCollection = db["transactions"]
        transaction = TransactionInfoCollection.find_one({"$and":[ {"userId":userId}, {"transactionId":transactionId}]})

        if(transaction != None):
            TransactionInfoCollection.delete_one({"$and":[ {"userId":userId}, {"transactionId":transactionId}]})
            return True 
        else:
            return False 




