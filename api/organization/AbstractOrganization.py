from abc import ABC, abstractmethod
import datetime
from dao import TableOrganization

class AbstractOrganization(ABC):
    
    def __init__(self):
        super().__init__()
    

    #Concrete methods
    def create_organization(params):
        return TableOrganization.insert_organization(params)
    
    def get_organization_by_id(self, org_id):
        return TableOrganization.read_organization(org_id)

    def update_organization(self, params):
        return TableOrganization.update_organization(params)

    def archive_organization(self, org_id):
        return TableOrganization.archive_organization(org_id)

    def delete_organization(self, org_id):
        return TableOrganization.delete_organization(org_id)

    #Abstract methods
    @abstractmethod
    def do_process(self):
        pass

