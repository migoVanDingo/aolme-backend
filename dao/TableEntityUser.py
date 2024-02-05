from datetime import datetime
import json
import logging
import random
import string

import MySQLdb
from flask import jsonify

class TableEntityUser:
    def __init__(self):
        from main import db
        self.db = db


    def generate_entity_user_id(self):
        N = 22
        return 'ENU' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))


    def insert_entity_user(self, payload):
        try:
            payload['entity_user_id'] = self.generate_entity_user_id()

            insert_query = "INSERT INTO entity_user (entity_user_id, entity_id, user_id, entity_type, entity_status, roles, is_active, created_at, created_by) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cur = self.db.connection.cursor()
            cur.execute(insert_query, (payload['entity_user_id'], payload['entity_id'], payload['user_id'], payload['entity_type'], payload['entity_status'], payload['roles'], payload['is_active'], payload['created_at'], payload['created_by']))

            self.db.connection.commit()

            return payload
        except MySQLdb.IntegrityError as e:
            logging.warn("failed to insert values %d, %s", id, "TABLE_ENTITY_USER::INSERT_ENTITY_USER::" + str(e))
        except Exception as e:
            return "TableEntityUser -- insert_entity_user() Error: " + str(e)
        finally:
            cur.close()
        

    def read_entity_user(self, entity_user_id):
        try:
            query = "SELECT * FROM entity_user WHERE is_active = 1 AND entity_user_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_user_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return "TableEntityUser -- read_entity_user() Error: " + str(e)
        

    def read_user_list_by_entity_id(self, entity_id):
        try:
            query = "SELECT * FROM entity_user JOIN user ON entity_user.user_id = user.user_id WHERE entity_user.is_active = 1 AND entity_user.entity_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_id,))
            
            data = cur.fetchall()

            cur.close()
            
            


            print("data: {}".format(data))
            return jsonify(data)
        except Exception as e:
            return "TableEntityUser -- read_user_list_by_entity_id() Error: " + str(e)
        
    def read_entity_list_by_user_id(self, user_id):
        try:

            query = "SELECT * FROM entity_user JOIN organization ON entity_user.entity_id = organization.organization_id WHERE entity_user.is_active = 1 AND organization.is_active = 1 AND entity_user.user_id = %s"
            #query = "SELECT * FROM entity_user WHERE is_active = 1 AND user_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (user_id,))
            
            data = cur.fetchall()

            cur.close()
            data = list(data)
            print("data: {}".format(data))

            return data
        except Exception as e:
            return "TableEntityUser -- read_entity_list_by_user_id() Error: " + str(e)
        

    def update_entity_user(self, payload):
        try:
            update_query = "UPDATE entity_user SET entity_id = %s, user_id = %s, is_active = %s, updated_at = %s, updated_by = %s WHERE is_active = 1 AND entity_user_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(update_query, (payload['entity_id'], payload['user_id'], payload['is_active'] , payload['updated_at'], payload['updated_by'], payload['entity_user_id']))

            self.db.connection.commit()
            cur.close()
            

            return payload
        except Exception as e:
            return "TableEntityUser -- update_entity_user() Error: " + str(e)
        


    def archive_entity_user(self, entity_user_id):
        try:
            update_query = "UPDATE entity_user SET is_active = %s WHERE entity_user_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(update_query, (False, entity_user_id))

            self.db.connection.commit()
            cur.close()


            return entity_user_id
        except Exception as e:
            return "TableEntityUser -- archive_entity_user() Error: " + str(e)
        


    def delete_entity_user(self, entity_user_id):
        try:
            query = "DELETE FROM entity_user WHERE entity_user_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_user_id,))
            self.db.connection.commit()
            cur.close()

            return entity_user_id
        except Exception as e:
            return "TableEntityUser -- delete_entity_user() Error: " + str(e)
