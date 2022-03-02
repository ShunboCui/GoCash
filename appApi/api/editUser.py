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
        {
        'userId': fields.String(readonly=True, description='The task unique identifier'),
        'userName': fields.String(readonly=True, description='The username'),
        'firstName': fields.String(readonly=True, description='The firstName'),
        'lastName': fields.String(readonly=True, description='The lastName'),
        'balanceAmount': fields.Integer(readonly=True, description='Details of the user account balance'),
        'email': fields.String(readonly=True, description='email'),
        'userPass': fields.String(readonly=True, description='password'),
        }
    Returns:
        user: user object
"""
class EditUserApi(Resource):
    # mod = transaction
    # @api.marshal_with(mod, code=200, mask = {})
    @api.doc(description="get user information")
    def put(self):

        userRequest =  request.json
        userId = userRequest["userId"]
        userName = userRequest["userName"]
        firstName = userRequest["firstName"]
        lastName = userRequest["lastName"]
        balanceAmount = userRequest["balanceAmount"]
        email = userRequest["email"]
        userPass = userRequest["userPass"]


        newUser = {
            "userId" : userId,
            "userName": userName,
            "firstName": firstName,
            "lastName": lastName,
            "balanceAmount": balanceAmount,
            "email": email,
            "userPass": userPass
        }

        #Verify Valid User
        try:
            self.editUser(userId, newUser)
        except: 
            return "Failed to access db", 500

        if newUser != None:
            return newUser 
        else:
            return "Invalid user", 404
                            

    def editUser(self, userId, newUser):
        db = get_database()
        UserInfoCollection = db["user_account"]
        newUser = UserInfoCollection.replace_one({"userId": userId}, newUser)


        





