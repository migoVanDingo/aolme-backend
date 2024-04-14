from flask import jsonify
from api.organization.AbstractOrganization import AbstractOrganization


class RequestGetOrganizationById(AbstractOrganization):
    def __init__(self, org_id):
        super().__init__()
        self.org_id = org_id

    def do_process(self):
        try:

            response = self.get_organization_by_id(self.org_id)
            print("Response: {}".format(response))
            return jsonify(response)
        except Exception as e:
            print("RequestGetOrganizationById -- do_process() Error: " + str(e))
            return "RequestGetOrganizationById -- do_process() Error: " + str(e)