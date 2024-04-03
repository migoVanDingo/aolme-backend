import os
import random
import string
from datetime import datetime


class TableSubset:
    def __init__(self): 
        from main import db
        self.db = db

    def generate_id(self):
        N = 22
        return 'SBS' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    
    def insert(self, payload):
        try:
            payload['subset_id'] = self.generate_id()
            payload['created_at'] = "{}".format(datetime.now())
            payload['is_active'] = 1
            payload['path'] = os.path.join(payload['path'], payload['subset_id'])
            query = "INSERT INTO subset(subset_id, dataset_id, name, description, owner, path, is_public, is_active, created_by, created_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cur = self.db.connection.cursor()
            cur.execute(query, (payload['subset_id'], payload['dataset_id'], payload['name'], payload['description'], payload['owner'], payload['path'], payload['is_public'], payload['is_active'], payload['created_by'], payload['created_at']))
                        
            self.db.connection.commit()

            cur.close()

            return payload
        except Exception as e:
            print("TableSubset -- insert() Error: " + str(e))
            return "TableSubset -- insert() Error: " + str(e)
        

    def read_list_by_dataset_id(self, dataset_id):
        query = "SELECT * FROM subset WHERE is_active = 1 AND dataset_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query,(dataset_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            print("TableSubset -- read_list() Error: " + str(e))
            return "TableSubset -- read_list() Error: " + str(e)
        
    def read_item(self, subset_id):
        query = "SELECT * FROM subset WHERE is_active = 1 AND subset_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (subset_id,))
            data = cur.fetchall()
            cur.close()
            return data[0]
        except Exception as e:
            print("TableSubset -- read_item() Error: " + str(e))
            return "TableSubset -- read_item() Error: " + str(e)