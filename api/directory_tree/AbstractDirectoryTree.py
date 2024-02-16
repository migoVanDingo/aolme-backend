from abc import ABC, abstractmethod
import os

class AbstractDirectoryTree(ABC):
    def __init__(self) -> None:
        super().__init__()


    # ACTION
    def create_directory(self, path):
        os.mkdir(path)

    def create_dir_list(self, path, dir_list):
        for dir in dir_list:
            os.mkdir(os.path.join(path, dir))

    def get_root_folder(self, project_id):
        pass

    def get_folder_items(self, folder_path):

        items = []
        with os.scandir(folder_path) as it:
            for entry in it:
                if not entry.name.startswith('.'):
                    if entry.is_file():
                        file_name = entry.name
                        base_name, extension = os.path.splitext(file_name)
                        items.append({ "name": base_name + extension, "type": "file"})

                    if entry.is_dir():
                        items.append({"name": entry.name, "type": "folder"})
                    
          
            
            # Split the file name into base and extension
            

        print("dir_list: {}".format(items))
        return items


    # DAO INTERACTION
    def insert_directory(self, project_id, folder_path):
        pass

    def get_directory_list_by_project_id(self, project_id):
        pass

    def get_directory_list_by_entity_id(self, project_id):
        pass

    def update_directory(self, project_id, folder_path):
        pass

    def delete_directory(self, project_id):
        pass

    def archive_directory(self, project_id):
        pass

    

    