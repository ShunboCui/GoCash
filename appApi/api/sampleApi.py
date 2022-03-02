from flask_restx import Resource
from appApi.utils import api, app
from appApi.models.sampleModel import sampleModel
from pprint import pprint

# Sample api just to get things started

class SampleApi(Resource):
    mod = sampleModel
    @api.marshal_with(mod, code=200, mask = {})
    @api.doc(description="just a dummy api that would be re-used to create actual api")
    def get(self):
        error = ""
        result = ""
        try:
            result = "dummy working"
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