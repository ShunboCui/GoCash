from flask_restx import Namespace
from appApi.api.sampleApi import SampleApi
from appApi.api.mongoEntries import MongoEntriesApi
from appApi.api.login import LoginApi
from appApi.api.createTransaction import CreateTransactionApi
from appApi.api.editTransaction import EditTransactionApi
from appApi.api.getAllTransactions import GetAllTransactionsApi
from appApi.api.getActiveTransactions import GetActiveTransactionsApi
from appApi.api.editTransaction import EditTransactionApi
from appApi.api.deleteTransaction import DeleteTransactionApi
from appApi.api.getUser import GetUserApi
from appApi.api.editUser import EditUserApi

from appApi.utils import api

ApiNamespace = Namespace('api', decription="endpoints for the GoCash app")

# add api resource to api namespace and specify the url for each endpoint
ApiNamespace.add_resource(SampleApi, "/dummy")
ApiNamespace.add_resource(MongoEntriesApi, "/mongo")
ApiNamespace.add_resource(LoginApi, "/login/<string:username>/<string:pwd>")
ApiNamespace.add_resource(CreateTransactionApi, "/createTransaction")
ApiNamespace.add_resource(GetAllTransactionsApi, "/getAllTransactions/<string:userId>")
ApiNamespace.add_resource(GetActiveTransactionsApi, "/getActiveTransactions/<string:userId>")
ApiNamespace.add_resource(EditTransactionApi, "/editTransaction")
ApiNamespace.add_resource(DeleteTransactionApi, "/deleteTransaction")

ApiNamespace.add_resource(GetUserApi, "/getUser/<string:userId>")
ApiNamespace.add_resource(EditUserApi, "/editUser")

# Add namespace to our api app
api.add_namespace(ApiNamespace)