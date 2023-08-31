from incoming import datatypes, PayloadValidator
class CreateProjectValidator(PayloadValidator):
    name = datatypes.String(required=True)
    description = datatypes.String(required=False)
    owner = datatypes.String(required=True)

    created_by = datatypes.String(required=True)
    # created_at = datatypes.String(required=True) 
    # last_updated = datatypes.String(required=True) 
    last_updated_by = datatypes.String(required=True) 

    # is_active = datatypes.Boolean(required=False) 