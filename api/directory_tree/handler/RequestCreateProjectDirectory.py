from api.directory_tree.AbstractDirectoryTree import AbstractDirectoryTree

import os
class RequestCreateProjectDirectory(AbstractDirectoryTree):
    
    def __init__(self, org_id, project_id) -> None:
        self.org_id = org_id
        self.project_id = project_id

    def do_process(self):
            
        path = os.path.join(os.environ['ORGANIZATION_DIRECTORY'], self.org_id)
        path = os.path.join(path, 'project')
        path = os.path.join(path, self.project_id)

        if os.path.isdir(path) is True:
            print("PROJECT_FOLDER_ALREADY_EXISTS")
            data = {"message":"PROJECT_FOLDER_ALREADY_EXISTS", "path":path}
            return data
        
        self.create_directory(path)
        
        print("PROJECT_FOLDER_CREATED")
        data = {"message":"PROJECT_FOLDER_CREATED", "path":path}

        print(data)
        return data