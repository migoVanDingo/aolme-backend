from datetime import datetime
from api.organization.AbstractOrganization import AbstractOrganization
from api.organization.utility.OrganizationValidator import OrganizationValidator

class RequestCreateOrganization(AbstractOrganization):
    def __init__(self, params):
        super().__init__()
        self.params = params


    def do_process(self):
       
       # Organization params
        params = {
            "name": self.params['name'],
            "email": self.params['email'],
            "description": self.params['description'] if 'description' in self.params else "",
            "is_active": True,
            "created_at":datetime.now(),
            "created_by": self.params['user_id']
        }

        print("REQUEST_CRETAE_ORGANIZATION_PAYLOAD: {}".format(params))
        #Validate the payload sent from FE
        validator = OrganizationValidator()
        is_valid = validator.validate(params)
        if is_valid[0] is False:
            return is_valid[1]
        
        
        return self.create_organization(params)
    
         

