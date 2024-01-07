from incoming import datatypes, PayloadValidator
class CreateProjectValidator(PayloadValidator):
    project_id = datatypes.String(required=True)
    name = datatypes.String(required=True)
    description = datatypes.String(required=False)
    owner = datatypes.String(required=True)
    ls_project_id = datatypes.String(required=True)
    is_public = datatypes.Boolean(required=True)
    created_by = datatypes.String(required=True)
    created_at = datatypes.String(required=True) 
    is_active = datatypes.Boolean(required=False)
    organization = datatypes.String(required=True)
    
 
    

    # is_active = datatypes.Boolean(required=False) 