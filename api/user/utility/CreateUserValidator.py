from incoming import datatypes, PayloadValidator
class CreateUserValidator(PayloadValidator):
    username = datatypes.String(required=True)
    email = datatypes.String(required=True)
    hash = datatypes.String(required=True)  
    created_by = datatypes.String(required=True)
    firstname = datatypes.String(required=False)
    lastname    = datatypes.String(required=False)
    