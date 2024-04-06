from incoming import datatypes, PayloadValidator
class CreateDatasetValidator(PayloadValidator):
    entity_id = datatypes.String(required=True)
    entity_type = datatypes.String(required=True)
    path = datatypes.String(required=True)
    name= datatypes.String(required=True)
    description = datatypes.String(required=False)
    owner = datatypes.String(required=True)
    type = datatypes.String(required=True)
    is_public = datatypes.Integer(required=True)



    
