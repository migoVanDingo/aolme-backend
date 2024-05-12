from flask import current_app
from api.organization.AbstractOrganization import AbstractOrganization

class RequestGetOrganizationListByUserId(AbstractOrganization):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id


    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: user_id: {self.user_id}")

            response = self.get_organization_list_by_user_id(self.user_id)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"