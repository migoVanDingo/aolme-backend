from incoming import datatypes, PayloadValidator

class InsertEntityUserValidator(PayloadValidator):
    entity_id = datatypes.String(required=True)
    user_id = datatypes.String(required=True)
    entity_type = datatypes.String(required=True)
    entity_status = datatypes.String(required=True)


    created_by = datatypes.String(required=True)

    roles = datatypes.Function('validate_roles', required=True)
    @classmethod
    def validate_roles(self,val,**kwargs):
        if len(val) == 0:
            return False
        return True
    