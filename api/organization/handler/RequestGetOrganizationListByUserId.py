from api.organization.AbstractOrganization import AbstractOrganization

class RequestGetOrganizationListByUserId(AbstractOrganization):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id


    def do_process(self):
        return self.get_organization_list_by_user_id(self.user_id)