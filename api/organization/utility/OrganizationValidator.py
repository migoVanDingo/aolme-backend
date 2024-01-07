from incoming import datatypes, PayloadValidator
class OrganizationValidator(PayloadValidator):
    name = datatypes.String(required=True)
    user_id = datatypes.String(required=True)
    description = datatypes.String(required=False)
    url = datatypes.String(required=False)

    