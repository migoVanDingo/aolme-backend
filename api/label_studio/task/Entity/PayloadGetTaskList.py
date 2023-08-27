from incoming import datatypes, PayloadValidator
class PayloadGetTaskList(PayloadValidator):
    view = datatypes.Integer(required=False)
    project = datatypes.Integer(required=False)
    resolve_uri = datatypes.Boolean(required=False)

    