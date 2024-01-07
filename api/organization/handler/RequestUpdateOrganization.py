import datetime
from api.organization.AbstractOrganization import AbstractOrganization


class RequestUpdateOrganization(AbstractOrganization):
    def __init__(self, org_id, params):
        self.org_id = org_id
        self.params = params

    def do_process(self):

        params = {
            "org_id": self.org_id,
            "name": self.params["name"],
            "url": self.params["url"],
            "description": self.params["description"],
            "updated_at": datetime.now(),
            "updated_by": self.params["updated_by"]

        }
        return self.update_organization(params)
    
    