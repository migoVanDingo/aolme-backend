import datetime
from api.organization.AbstractOrganization import AbstractOrganization
from api.organization.utility.OrganizationValidator import OrganizationValidator

class RequestCreateOrganization(AbstractOrganization):
    def __init__(self, params):
        self.params = params

    def do_process(self):
       
        #Validate the payload sent from FE
        validator = OrganizationValidator()
        is_valid = validator.validate(self.params)
        if is_valid[0] is False:
            return is_valid[1]
        
        # Organization params
        params = {
            "name": self.params['name'],
            "url":self.params['url'],
            "description": self.params['description'],
            "is_active": True,
            "created_at":datetime.now(),
            "created_by": self.params['user_id']
        }

        
        return self.create_organization(params)
    
         

