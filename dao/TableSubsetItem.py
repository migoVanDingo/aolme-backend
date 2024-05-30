import os
import random
import string
from datetime import datetime

from flask import current_app


class TableSubsetItem:
    def __init__(self): 
        from main import db
        self.db = db

    def generate_id(self):
        N = 22
        return 'SBI' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    
    def insert(self, payload):
        try:
            query = "INSERT INTO subset_item (subset_item_id, subset_id, type, name, path, is_active, created_by, created_at) values (%s, %s, %s, %s, %s, %s, %s, %s)"
            payload['sub_item_id'] = self.generate_id()
            payload['created_at'] = "{}".format(datetime.now())
            payload['is_active'] = 1
    
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['sub_item_id'], payload['subset_id'], payload['type'], payload['name'], payload['path'], payload['is_active'], payload['created_by'], payload['created_at']))
            self.db.connection.commit()
            cur.close()

    
            return payload

        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableSubsetItem -- insert() Error: " + str(e)
        
    def read_list(self, subset_id):
        query = "SELECT * FROM subset_item WHERE is_active = 1 AND subset_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (subset_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableSubsetItem -- read_list() Error: " + str(e)
        
    def read_item(self, sub_item_id):
        query = "SELECT * FROM subset_item WHERE is_active = 1 AND sub_item_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (sub_item_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableSubsetItem -- read_item() Error: " + str(e)
        
    def read_item_by_subset_and_filename(self, subset_id, filename):
        query = "SELECT * FROM subset_item WHERE is_active = 1 AND subset_id = %s AND name = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (subset_id, filename))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableSubsetItem -- read_item_by_subset_and_filename() Error: " + str(e)