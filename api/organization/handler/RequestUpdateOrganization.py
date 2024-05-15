import datetime

from flask import current_app
from api.organization.AbstractOrganization import AbstractOrganization


class RequestUpdateOrganization(AbstractOrganization):
    def __init__(self, org_id, params):
        self.org_id = org_id
        self.params = params

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: org_id: {self.org_id} :: payload: {self.params}")
            params = {
                "org_id": self.org_id,
                "name": self.params["name"],
                "url": self.params["url"],
                "description": self.params["description"],
                "updated_at": datetime.now(),
                "updated_by": self.params["updated_by"]

            }
            current_app.logger.debug(f"{self.__class__.__name__} :: update-organization-payload: {params}")
            response = self.update_organization(params)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"
        
    
    