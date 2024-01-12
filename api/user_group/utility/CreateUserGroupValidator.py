from incoming import datatypes, PayloadValidator
class CreateUserGroupValidator(PayloadValidator):
    name = datatypes.String(required=True)
    description = datatypes.String(required=False)
    created_by = datatypes.String(required=True)
    created_at = datatypes.String(required=True)