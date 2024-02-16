from incoming import datatypes, PayloadValidator
class CreateDatasetValidator(PayloadValidator):
    entity_id = datatypes.String(required=True)
    name= datatypes.String(required=True)
    description = datatypes.String(required=False)
    owner = datatypes.String(required=True)
    type = datatypes.String(required=True)
    is_public = datatypes.Integer(required=True)
    created_by = datatypes.String(required=True)
    created_at = datatypes.String(required=True)
    is_active = datatypes.Integer(required=False)
