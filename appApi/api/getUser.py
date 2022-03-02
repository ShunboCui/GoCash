from urllib import request
from flask_restx import Resource
from itsdangerous import exc
from appApi.utils import api, app
from appApi.models.userModel import user
from pprint import pprint
from flask import request 
from appApi.pymongo_connect import get_database
import uuid


"""
    Returns user information
    Parameters:
        userId: unique user identifier
    Returns:
        user: user object
"""
class GetUserApi(Resource):
    # mod = transaction
    # @api.marshal_with(mod, code=200, mask = {})
    @api.doc(description="get user information")
    def get(self, userId):

        #Verify Valid User
        try:
            user = self.getUser(userId)
        except: 
            return "Failed to access db", 500
        if user != None:
            user.pop("_id")
            return user 
        else:
            return "Invalid user", 404
                            


    """
    Checks whether a user already exists in the database 
    Parameters:
        userId: the unique identification name for the user <str>
    Returns:
        True/False <boolean>
    """
    def getUser(self, userId):
        db = get_database()
        UserInfoCollection = db["user_account"]
        user = UserInfoCollection.find_one({"userId": userId})
        return user 





