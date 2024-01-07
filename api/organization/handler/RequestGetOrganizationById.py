from api.organization.AbstractOrganization import AbstractOrganization


class RequestGetOrganizationById(AbstractOrganization):
    def __init__(self, org_id):
        self.org_id = org_id

    def do_process(self):
        return self.get_organization_by_id(self.org_id)