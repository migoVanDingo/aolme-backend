from incoming import datatypes, PayloadValidator
class OrganizationValidator(PayloadValidator):
    name = datatypes.String(required=True)
    email = datatypes.String(required=True)
    created_by = datatypes.String(required=True)
    description = datatypes.String(required=False)
    

    