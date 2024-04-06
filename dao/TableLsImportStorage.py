from datetime import datetime
import os
import random
import string

from flask import jsonify

class TableLsImportStorage:
    def __init__(self):
        from main import db
        self.db = db

    def generate_entity_user_id(self):
        N = 21
        return 'LSIS' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

    def insert_ls_import_storage(self, payload):
        try:
            payload['import_storage_id'] = self.generate_entity_user_id()
            payload['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            payload['is_active'] = True
            query = "INSERT INTO ls_import_storage(import_storage_id, ls_id, repo_id, entity_id, user_id, path, title, project_id, is_active, created_at, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cur = self.db.connection.cursor()
            cur.execute(query, (payload['import_storage_id'],payload['ls_id'], payload['repo_id'], payload['entity_id'], payload['user_id'], payload['path'], payload['title'], payload['project_id'], payload['is_active'], payload['created_at'], payload['created_by']))

            response = {
                "import_storage_id": payload['import_storage_id'],
                "ls_id": payload['ls_id'],
                "repo_id": payload['repo_id'],
                "entity_id": payload['entity_id'],
                "user_id": payload['user_id'],
                "path": payload['path'],
                "title": payload['title'],
                "project_id": payload['project_id'],
                "is_active": payload['is_active'],
                "created_at":  payload['created_at'],
                "created_by": payload['created_by']
            }

            self.db.connection.commit()
            cur.close()

            print("TableLsImportStorage -- insert_ls_import_storage() -- response: " + str(response))


            return response
        except Exception as e:
            print("TableLsImportStorage -- insert_ls_import_storage() Error: " + str(e))
            return "TableLsImportStorage -- insert_ls_import_storage() Error: " + str(e)
        

    def read_ls_import_storage_by_repo_id(self, repo_id):
        try:
            query = "SELECT * FROM ls_import_storage WHERE repo_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (repo_id,))
            data = cur.fetchall()
            cur.close()

            print("TableLsImportStorage -- read_ls_import_storage_by_repo_id() -- data: " + str(data))

            if(len(data) > 0):
                return data[0]

            return data
        except Exception as e:
            print("TableLsImportStorage -- read_ls_import_storage_by_repo_id() Error: " + str(e))
            return "TableLsImportStorage -- read_ls_import_storage_by_repo_id() Error: " + str(e)