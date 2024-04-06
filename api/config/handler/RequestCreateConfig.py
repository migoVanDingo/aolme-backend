from datetime import datetime
import os
from api.config.AbstractConfig import AbstractConfig
from api.config.entity.CreateConfigValidator import CreateConfigValidator
from dao.TableRepoItem import TableRepoItem

class RequestCreateConfig(AbstractConfig):
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
                
            path = os.path.join(path, 'config')
            
            
            files = self.files
            now = "{}".format(datetime.now())
            for file in files:
                if file.filename == '':
                    return "File must have name"
                

                path = os.path.join(path, file.filename)
                print("path: {}".format(path))
                # Create entry in db first to get config_id
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

                print("payload: {}".format(payload))

                validator = CreateConfigValidator()
                is_valid = validator.validate(payload)
                if is_valid[0] is False:
                    return is_valid[1]
                
                dao_response = self.create(payload)

                if self.repo_id is not None:
                    repo_item_payload = {
                        "repo_item_id":dao_response['config_id'],
                        "repo_id": self.repo_id,
                        "is_active": 1,
                        "created_at": dao_response['created_at'],
                        "created_by": dao_response['created_by'],
                        "type": "CONFIG"
                    }
                    print("Saving repo_item -- payload: {}".format(repo_item_payload))
                    table_repo_item = TableRepoItem()
                    response = table_repo_item.insert(repo_item_payload)
                    print("TableRepoItem::::insert()::::response: {}".format(response))

                # print("dao_response: {}".format(dao_response))
                # config_id = dao_response['config_id']
                
                # filename = file.filename
                # f = filename.split('.')
                # last = f.pop()
                # file.filename = config_id + '...'.join(f) + '.' + last
                
                file.save(path)




            return dao_response
            

        except Exception as e:
            print("RequestCreateConfig -- do_process() Error: " + str(e))
            return "RequestCreateConfig -- do_process() Error: " + str(e)