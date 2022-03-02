from flask_restx import Resource
from pprint import pprint
from appApi.utils import api, app
from appApi.models.mongoEntryModel import mongoEntryModel
from appApi.pymongo_connect import get_database


# Sample api just to get things started

class MongoEntriesApi(Resource):
    mod = mongoEntryModel
    @api.marshal_with(mod, code=200, mask = {})
    @api.doc(description="api that prints one of the entry in the db")
    def get(self):
        error = ""
        result = ""
        try:
            db = get_database()
            print("trying to find the collection")
            colec = db["comments"]
            singleEntry = colec.find_one()
            pprint(singleEntry)
            returnJson = {
                "data" : singleEntry,
                "error": error
            }
            return returnJson
        except Exception as e:
            returnJson  = {
                "data": {},
                "error": str(type(e).__name__)+": " + str(e)
            }
            return returnJson