from flask_restx import fields
from appApi.utils import api

# create a template for json that is populated by api

singleEntryNod = api.model('singleEntry',
{
    'email': fields.String(),
    'name' : fields.String(),
    'text' : fields.String(),

}

)

mongoEntryModel = api.model('mongoEntry',
{
    'data': fields.Nested(singleEntryNod),
    "error": fields.String(),
}

)