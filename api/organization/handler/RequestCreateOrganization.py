from datetime import datetime
import json

import requests
from api.directory_tree.handler.RequestCreateOrganizationDirectory import RequestCreateOrganizationDirectory
from api.entity_user.handler.RequestInsertEntityUser import RequestInsertEntityUser
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
        
        org = self.create_organization(params)

        headers = {
            "Content-Type": "application/json"
        }

        #url = "http://localhost:5000/api/entity-user"
        entity_user_payload = {
            "entity_id": org['org_id'],
            "user_id": self.params['user_id'],
            "entity_type": "ORGANIZATION",
            "entity_status": "ACTIVE",
            "created_by": self.params['user_id'],
            "roles": "OWNER"
        
        }

        #entity_user_payload["roles"] = json.dumps(entity_user_payload["roles"])
        print("ENTITY_USER_PAYLOAD: {}".format(entity_user_payload))

        api_request = RequestInsertEntityUser(entity_user_payload)
        response = api_request.do_process()
        print("RESPONSE1: {}".format(response))
        print("orgID_ID: {}".format(org['org_id']))
        api_request = RequestCreateOrganizationDirectory(org['org_id'])
        response = api_request.do_process()
        print("RESPONSE2: {}".format(response))


        return org
    
         

