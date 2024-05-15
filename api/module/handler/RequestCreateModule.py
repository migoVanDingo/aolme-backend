from datetime import datetime
import os

from flask import current_app
from api.module.AbstractModule import AbstractModule
from api.module.entity.ModuleValidator import CreateModuleValidator
from dao.TableRepoItem import TableRepoItem

class RequestCreateModule(AbstractModule):
    def __init__(self, params, files, repo_id=None):
        super().__init__()
        self.params = params
        self.files = files
        if repo_id is None:
            self.repo_id = None
        else:
            self.repo_id = repo_id

    def do_process(self):
        try:

            dao_response = "NULL"
            if "USR" in self.params.get('entity_id'):
                path = os.path.join(os.environ['USER_DIRECTORY'], self.params.get('entity_id'))
            elif "ORG" in self.params.get('entity_id'):
                path = os.path.join(os.environ['ORGANIZATION_DIRECTORY'], self.params.get('entity_id'))
            path = os.path.join(path, 'module')
            
            
            files = self.files
            now = "{}".format(datetime.now())
            for file in files:
                if file.filename == '':
                    return "File must have name"
                

                path = os.path.join(path, file.filename)
                current_app.logger.debug(f"{self.__class__.__name__} :: path: {path}")
                # Create entry in db first to get module_id
                payload = {
                    "entity_id": self.params.get('entity_id'),
                    "name": file.filename,
                    "description": self.params.get('description'),
                    "owner": self.params.get('owner'),
                    "type": self.params.get('type'),
                    "created_by": self.params.get('owner'),
                    "created_at": now,
                    "path": path,
                    "is_active": 1,
                }

                payload['is_public'] = 1 if self.params.get('is_public') == '1' else 0

                current_app.logger.debug(f"{self.__class__.__name__} :: create-module-payload: {payload}")

                validator = CreateModuleValidator()
                is_valid = validator.validate(payload)
                if is_valid[0] is False:
                    current_app.logger.error(f"{self.__class__.__name__} :: ERROR: Invalid Payload: {is_valid[1]}")
                    return is_valid[1]
                
                dao_response = self.create(payload)
                if self.repo_id is not None:
                    repo_item_payload = {
                        "repo_item_id":dao_response['module_id'],
                        "repo_id": self.repo_id,
                        "is_active": 1,
                        "created_at": dao_response['created_at'],
                        "created_by": dao_response['created_by'],
                        "type": "MODULE"
                    }
                    current_app.logger.debug(f"{self.__class__.__name__} :: repo_item_payload: {repo_item_payload}")
                    table_repo_item = TableRepoItem()
                    response = table_repo_item.insert(repo_item_payload)
                    current_app.logger.debug(f"{self.__class__.__name__} :: insert-repo-item-response: {response}")

                file.save(path)




            return dao_response
            

        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestCreateModule -- do_process() Error: " + str(e)
        
    

        