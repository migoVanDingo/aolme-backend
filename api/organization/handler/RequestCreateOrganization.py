from datetime import datetime
import json

from flask import current_app
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
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.params}")
        
        # Organization params
            params = {
                "name": self.params['name'],
                "email": self.params['email'],
                "description": self.params['description'] if 'description' in self.params else "",
                "is_active": True,
                "created_at":datetime.now(),
                "created_by": self.params['user_id']
            }
            current_app.logger.debug(f"{self.__class__.__name__} :: create-organization-payload: {params}")


            #Validate the payload sent from FE
            validator = OrganizationValidator()
            is_valid = validator.validate(params)
            if is_valid[0] is False:
                current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {is_valid[1]}")
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
                "roles": "OWNER",
                "user_status": self.params['user_status']
            
            }
            current_app.logger.debug(f"{self.__class__.__name__} :: entity-user-payload: {entity_user_payload}")



            api_request = RequestInsertEntityUser(entity_user_payload)
            response = api_request.do_process()
            current_app.logger.debug(f"{self.__class__.__name__} :: entity-user-response: {response}")



            api_request = RequestCreateOrganizationDirectory(org['org_id'])
            response = api_request.do_process()
            current_app.logger.debug(f"{self.__class__.__name__} :: create-organization-directory-response: {response}")

            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {org}")

            return org
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"
    
         

