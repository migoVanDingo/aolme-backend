import random
import string

from flask import current_app


class TableFilesV2:
    def __init__(self):
        from main import db
        self.db = db

    def generate_id(self, type):
        N = 22
        match type:
            case "DATASET":
                return 'FDS' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            case "CONFIG":
                return 'FCF' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            case "MODULE":
                return 'FMD' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            case "ANNOTATION":
                return 'FAN' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            case "GROUND_TRUTH":
                return 'FGT' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        

            case _:
                return 'FYL' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

        
    
    def insert_files(self, payload):
        query = "INSERT INTO files(file_id, entity_id, name, description, owner, type, path, is_public, is_active, created_by, created_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        

        try:
            payload['file_id'] = self.generate_id(payload['type'])

            current_app.logger.debug(f"{self.__class__.__name__} :: insert_files :: payload: {payload}")
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['file_id'], payload['entity_id'], payload['name'], payload['description'], payload['owner'], payload['type'], payload['path'], payload['is_public'], payload['is_active'], payload['created_by'], payload['created_at']))
            
            self.db.connection.commit()
            cur.close()
            
            current_app.logger.debug(f"{self.__class__.__name__} :: insert_files :: inserted-object: {payload}")
            return payload
            
        
        except Exception as e:  
            current_app.logger.error(f"{self.__class__.__name__} :: insert_files :: Error: {str(e)}")
            return "TableFilesV2 -- insert_files() Error: " + str(e)
        

    def read_list(self):
        query = "SELECT * FROM files WHERE is_active = 1 AND is_public = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: read_list :: Error: {str(e)}")
            return "TableFilesV2 -- read_list() Error: " + str(e)
        

    def read_item(self, files_id):
        query = "SELECT * FROM files WHERE file_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (files_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: read_item :: Error: {str(e)}")
            return "TableFilesV2 -- read_item() Error: " + str(e)

    def read_list_by_entity(self, entity_id):
        query = "SELECT * FROM files WHERE entity_id = %s AND is_active = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: read_list_by_entity :: Error: {str(e)}")
            return "TableFilesV2 -- read_list_by_entity() Error: " + str(e)

    def read_list_by_user(self, user_id):
        query = "SELECT * FROM files WHERE owner = %s AND is_active = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (user_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: read_list_by_user :: Error: {str(e)}")
            return "TableFilesV2 -- read_list_by_user() Error: " + str(e)
        

    def update(self, payload):
        query = "UPDATE files SET name = %s, description = %s, type = %s, path = %s, is_public = %s, is_active = %s, modified_by = %s, modified_at = %s WHERE file_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['name'], payload['description'], payload['type'], payload['path'], payload['is_public'], payload['is_active'], payload['modified_by'], payload['modified_at'], payload['file_id']))
            self.db.connection.commit()
            cur.close()
            return payload
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: update :: Error: {str(e)}")
            return "TableFilesV2 -- update() Error: " + str(e)

    def delete(self, files_id):
        query = "DELETE FROM files WHERE file_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (files_id,))
            self.db.connection.commit()
            cur.close()
            return files_id
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: delete :: Error: {str(e)}")
            return "TableFilesV2 -- delete() Error: " + str(e)

    def archive(self, files_id):
        query = "UPDATE files SET is_active = 0 WHERE file_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (files_id,))
            self.db.connection.commit()
            cur.close()
            return files_id
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: archive :: Error: {str(e)}")
            return "TableFilesV2 -- archive() Error: " + str(e)
        
    def archive_by_name(self, name, entity_id):
        query = "UPDATE files SET is_active = 0 WHERE name = %s AND entity_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (name, entity_id))
            self.db.connection.commit()
            cur.close()
            return name
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: archive_by_name :: Error: {str(e)}")
            return "TableFilesV2 -- archive_by_name() Error: " + str(e)
        

