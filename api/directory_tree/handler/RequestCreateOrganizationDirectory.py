from api.directory_tree.AbstractDirectoryTree import AbstractDirectoryTree
import os
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

        #Create org project folder
        path_project = os.path.join(path, 'project')
        self.create_directory(path_project)

        #Create Dataset directory
        path_dataset = os.path.join(path, 'dataset')
        self.create_directory(path_dataset)
        
        #Create Module Directory
        path_module = os.path.join(path, 'module')
        self.create_directory(path_module)

        #Create Experiments directory
        path_experiment = os.path.join(path, 'experiment')
        self.create_directory(path_experiment)

        #Create config directory
        path_config = os.path.join(path, 'config')
        self.create_directory(path_config)
        
        print("ORG_FOLDER_CREATED")
        data = {"message":"ORG_FOLDER_CREATED", "path":path}

        print(data)
        return data