from api.directory_tree.AbstractDirectoryTree import AbstractDirectoryTree
import os

class RequestCreateUserDirectory(AbstractDirectoryTree):
    def __init__(self, user_id):
        self.user_id = user_id
    
    def do_process(self):
        path = os.path.join(os.environ['USER_DIRECTORY'], self.user_id)

        print('userPath', path)
        
        if os.path.isdir(path) is True:
            print("USER_FOLDER_ALREADY_EXISTS")
            data = {"message":"USER_FOLDER_ALREADY_EXISTS", "path":path}
            return data
        
        self.create_directory(path)

        dir_list = ['project', 'dataset', 'module', 'experiment', 'config', 'annotations','model', 'notebook', 'report', 'data', 'logs', 'ground_truth']

        self.create_dir_list(path, dir_list)

        print("USER_FOLDER_CREATED")
        data = {"message":"USER_FOLDER_CREATED", "path":path}

        print(data)
        return data