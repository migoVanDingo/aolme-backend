from datetime import datetime
import os

from flask import jsonify
from api.files.AbstractFiles import AbstractFiles
from api.dataset.entity.CreateDatasetValidator import CreateDatasetValidator
from dao.TableRepoItem import TableRepoItem

class RequestCreateFileRecord(AbstractFiles):
    def __init__(self, params, files, repo_id=None):
        super().__init__()
        self.params = params
        self.files = files
        self.repo_id = repo_id

    def do_process(self):
        try:

            dao_response = "NULL"

            print("params: {}".format(self.params))
            path = ''
            if "USR" in self.params.get('entity_id'):
                path = os.path.join(os.environ['USER_DIRECTORY'], self.params.get('entity_id'))
            elif "ORG" in self.params.get('entity_id'):
                path = os.path.join(os.environ['ORGANIZATION_DIRECTORY'], self.params.get('entity_id'))

            
            

            
            repo_path = None
            if self.repo_id is not None:
                # repo_path = os.path.join(os.environ['USER_DIRECTORY'], 'repo')
                # repo_path = os.path.join(repo_path, self.repo_id)
                # repo_path = os.path.join(repo_path, 'files')
                repo_path = os.path.join(os.environ['REPO_DIRECTORY'], self.repo_id)
                repo_path = os.path.join(repo_path, self.params.get('type').lower())

            print("repo_path: {}".format(repo_path))

            path = os.path.join(path, self.params.get('type').lower())


            files = self.files

            print("files: {}".format(files))
            now = "{}".format(datetime.now())
            for file in files:
                if file.filename == '':
                    print("Error: File must have name")
                    return "File must have name"
                
        
                path = os.path.join(path, file.filename)
                print("path: {}".format(path))
                # Create entry in db first to get dataset_id
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

                

                # validator = CreateDatasetValidator()
                # is_valid = validator.validate(payload)
                # if is_valid[0] is False:
                #     print("RequestCreateFileRecord::::do_process()::CreateDatasetValidator::Error: {}".format(str(is_valid[1])))
                #     return is_valid[1]
                
                dao_response = self.insert_file(payload)

                print("daoReponse: {}".format(dao_response))

                if self.repo_id is not None:
                    repo_item_payload = {
                        "file_id":dao_response['file_id'],
                        "repo_id": self.repo_id,
                        "is_active": 1,
                        "created_at": dao_response['created_at'],
                        "created_by": dao_response['created_by'],
                        "type": dao_response['type']
                    }
                    print("Saving repo_item -- payload: {}".format(repo_item_payload))
                    table_repo_item = TableRepoItem()
                    response = table_repo_item.insert(repo_item_payload)
                    print("TableRepoItem::::insert()::::response: {}".format(response))
                    
                

                # print("dao_response: {}".format(dao_response))
                # dataset_id = dao_response['dataset_id']
                
                # filename = file.filename
                # f = filename.split('.')
                # last = f.pop()
                # file.filename = dataset_id + '...'.join(f) + '.' + last
                
                file.save(path)
                if repo_path is not None:
                    file.save(os.path.join(repo_path, file.filename))




            return jsonify(dao_response)
            

        except Exception as e:
            print("RequestCreateFileRecord -- do_process() Error: " + str(e))
            return "RequestCreateFileRecord -- do_process() Error: " + str(e), 404