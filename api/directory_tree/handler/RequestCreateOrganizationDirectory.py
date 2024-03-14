
from api.directory_tree.AbstractDirectoryTree import AbstractDirectoryTree
import os

from utility.Constant import Constant
class RequestCreateOrganizationDirectory(AbstractDirectoryTree):
    def __init__(self, org_id) -> None:
        self.org_id = org_id

    def do_process(self):
            
        path = os.path.join(os.environ['ORGANIZATION_DIRECTORY'], self.org_id)

        if os.path.isdir(path) is True:
            print("FOLDER_ALREADY_EXISTS")
            data = {"message":"FOLDER_ALREADY_EXISTS", "path":path}
            return data
        
        self.create_directory(path)

        dir_list = Constant.directory_list

        self.create_dir_list(path, dir_list)
        
        print("ORG_FOLDER_CREATED")
        data = {"message":"ORG_FOLDER_CREATED", "path":path}

        print(data)
        return data