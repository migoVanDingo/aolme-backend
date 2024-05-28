import random
import string
from datetime import datetime

from flask import current_app


class TableDatasetV2:
    def __init__(self): 
        from main import db
        self.db = db

    def generate_id(self):
        N = 22
        return 'DAT' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    
    def insert(self, payload):
        try:
            payload['dataset_id'] = self.generate_id()
            payload['created_at'] = "{}".format(datetime.now())
            payload['created_by'] = payload['owner']
            payload['is_active'] = 1
            query = "INSERT INTO dataset(dataset_id, entity_id, entity_type, name, description, owner, type, path, is_public, is_active, created_by, created_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cur = self.db.connection.cursor()
            cur.execute(query, (payload['dataset_id'], payload['entity_id'], payload['entity_type'], payload['name'], payload['description'], payload['owner'], payload['type'], payload['path'], payload['is_public'], payload['is_active'], payload['created_by'], payload['created_at']))


            self.db.connection.commit()
            cur.close()



            return payload
        
        
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableDatasetV2 -- insert() Error: " + str(e)
        
    def read_list_entity(self, entity_id):
        query = "SELECT * FROM dataset WHERE is_active = 1 AND entity_id = %s"

        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_id,))
            data = cur.fetchall()
            cur.close()
            current_app.logger.info(f"{self.__class__.__name__} :: read_list_entity object :: {data}")
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableDatasetV2 -- read_list() Error: " + str(e)
        
    def read_item(self, dataset_id):
        query = "SELECT * FROM dataset WHERE is_active = 1 AND dataset_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (dataset_id,))
            data = cur.fetchall()
            cur.close()

            if len(data) == 0:
                return "NO_DATA_FOUND"
            return data[0]
        except Exception as e:
            return "TableDatasetV2 -- read_item() Error: " + str(e)
        