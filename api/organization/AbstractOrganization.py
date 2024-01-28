from abc import ABC, abstractmethod
import datetime
from dao.TableEntityUser import TableEntityUser
from dao.TableOrganization import TableOrganization

class AbstractOrganization(ABC):
    
    def __init__(self):
        super().__init__()
        self.table_organization = TableOrganization()
        self.entity_user = TableEntityUser()
    

    #Concrete methods
    def create_organization(self, params):
        return self.table_organization.insert_organization(params)
    
    def get_organization_by_id(self, org_id):
        return self.table_organization.read_organization(org_id)
    
    def get_organization_list_by_user_id(self, user_id):
        return self.entity_user.read_entity_list_by_user_id(user_id)

    def update_organization(self, params):
        return self.table_organization.update_organization(params)

    def archive_organization(self, org_id):
        return self.table_organization.archive_organization(org_id)

    def delete_organization(self, org_id):
        return self.table_organization.delete_organization(org_id)

    #Abstract methods
    @abstractmethod
    def do_process(self):
        pass

