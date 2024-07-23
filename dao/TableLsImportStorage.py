from datetime import datetime
import os
import random
import string

from flask import current_app, jsonify

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
            payload['is_active'] = 1
            query = "INSERT INTO ls_import_storage(import_storage_id, ls_import_id, subset_id, entity_id, user_id, path, title, ls_project_id, is_active, created_at, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            current_app.logger.debug(f"{self.__class__.__name__} :: insert_ls_import_storage :: payload: {payload}")

            cur = self.db.connection.cursor()
            cur.execute(query, (payload['import_storage_id'],payload['ls_import_id'], payload['subset_id'], payload['entity_id'], payload['user_id'], payload['path'], payload['title'], payload['ls_project_id'], payload['is_active'], payload['created_at'], payload['created_by']))

            response = {
                "import_storage_id": payload['import_storage_id'],
                "ls_import_id": payload['ls_import_id'],
                "subset_id": payload['subset_id'],
                "entity_id": payload['entity_id'],
                "user_id": payload['user_id'],
                "path": payload['path'],
                "title": payload['title'],
                "ls_project_id": payload['ls_project_id'],
                "is_active": payload['is_active'],
                "created_at":  payload['created_at'],
                "created_by": payload['created_by']
            }

            self.db.connection.commit()
            cur.close()

            current_app.logger.debug(f"{self.__class__.__name__} :: inserted-object: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: insert_ls_import_storage :: Error: {str(e)}")
            return "TableLsImportStorage -- insert_ls_import_storage() Error: " + str(e)
        
    def read_ls_import_storage_by_subset_id(self, subset_id):
        try:
            query = "SELECT * FROM ls_import_storage WHERE subset_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (subset_id,))
            data = cur.fetchall()
            cur.close()

            current_app.logger.debug(f"{self.__class__.__name__} :: read_ls_import_storage_by_subset_id() -- data: {data}")

            if(len(data) > 0):
                return data[0]

            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: read_ls_import_storage_by_subset_id() Error: {str(e)}")
            return "TableLsImportStorage -- read_ls_import_storage_by_subset_id() Error: " + str(e)
        

    def read_ls_import_storage_by_repo_id(self, repo_id):
        try:
            query = "SELECT * FROM ls_import_storage WHERE repo_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (repo_id,))
            data = cur.fetchall()
            cur.close()

            current_app.logger.debug(f"{self.__class__.__name__} :: read_ls_import_storage_by_repo_id() -- data: {data}")

            if(len(data) > 0):
                return data[0]

            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: read_ls_import_storage_by_repo_id() Error: {str(e)}")
            return "TableLsImportStorage -- read_ls_import_storage_by_repo_id() Error: " + str(e)