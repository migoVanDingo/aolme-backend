from flask import current_app, jsonify
from api.organization.AbstractOrganization import AbstractOrganization


class RequestGetOrganizationById(AbstractOrganization):
    def __init__(self, org_id):
        super().__init__()
        self.org_id = org_id

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: org_id: {self.org_id}")
            response = self.get_organization_by_id(self.org_id)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return jsonify(response)
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestGetOrganizationById -- do_process() Error: " + str(e)