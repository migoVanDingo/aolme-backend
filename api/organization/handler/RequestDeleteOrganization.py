from api.organization.AbstractOrganization import AbstractOrganization


class RequestDeleteOrganization(AbstractOrganization):
    def __init__(self, org_id):
        self.org_id = org_id

    def do_process(self):
        return self.delete_organization(self.org_id)