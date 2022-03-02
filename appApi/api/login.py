from flask_restx import Resource
from appApi.utils import api, app
from appApi.models.loginModel import loginModel
from appApi.pymongo_connect import get_database
import bcrypt
from pprint import pprint

"""
    Resource Login takes input on a GET protocol and and logs user in
    Parameters:
        username: unique input username correspoding to our user
        pwd: inout password by our user
    Returns:
        returnJson: contains result string and error msg if any
"""
class LoginApi(Resource):
    mod = loginModel
    @api.marshal_with(mod, code=200, mask = {})
    @api.doc(description="api to handle user login to the GoCash app")
    def get(self, username, pwd):
        error = ""
        result = ""
        try:
            # check to make sure user exists
            if not self.userExists(username):
                error = "User: '" + username + "' does not exist, please register!"
            
            # User exists, check that the password is valid
            else:
                ################ USE HASHED PASSWORD. UNCOMMENT NEXT LINE ##################
                # hashedPwd = bcrypt.hashpw(pwd.encode('utf8'), bcrypt.gensalt())

                # check that this hashed password is same as the one stored in the db
                if not self.verifypw(username, pwd):
                    error = "Input password for User: '" + username + "' is in-correct, please re-enter the correct password"
                else:
                    result = "Login successful for User: '" + username + "'"
            
            returnJson = {
                "data" : result,
                "error": error
            }
            return returnJson
        except Exception as e:
            returnJson  = {
                "data": result,
                "error": str(type(e).__name__)+": " + str(e)
            }
            return returnJson
    
    """
    Checks whether a user already exists in the database 
       
    Parameters:
        username: the unique identification name for the user <str>
    Returns:
        True/False <boolean>
    """
    def userExists(self, username):
        db = get_database()
        print("Dies it orint?")
        UserInfoCollection = db["user_info"]
        singleEntry = UserInfoCollection.find_one()
        pprint(singleEntry)
        print("?????????????")
        if UserInfoCollection.find({"username": username}):
            return True
        else:
            return False

    
    """
    Verifies password provided by the user against the one already present in the database
       
    Parameters:
        username: the unique identification name for the user <str>
        password : password given at the time of calling the API <str>
    Returns:
        True/False <boolean>
    """
    def verifypw(self, username, inputHashedPwd):
        db = get_database()
        UserInfoCollection = db["user_info"]
        correctHashedPwd = UserInfoCollection.find({
            "username" : username
        })[0]["password"]

        if inputHashedPwd == correctHashedPwd:
            return True
        else:
            return False
            