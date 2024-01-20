from datetime import datetime
import random
import string

import uuid
class TableUser:
    def __init__(self):
        from main import db
        self.db = db


    def generate_user_id(self):
        N = 22
        return 'USR' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    
    #V2
    def insert_user(self, payload):
        try:
            
            insert_query = "INSERT INTO user (user_id, username, email, hash, firstname, lastname, is_active, created_at, created_by) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"


            cur = self.db.connection.cursor()
            cur.execute(insert_query, (self.generate_user_id(), payload['username'], payload['email'], payload['hash'], payload['firstname'], payload['lastname'], payload['is_active'], payload['created_at'], payload['created_by']))

            self.db.connection.commit()
            cur.close()

            return payload
        
        except Exception as e:
            return "TableUser -- insert_user() Error: " + str(e)
        

    def read_user(self, user_id):
        try:
            query = "SELECT * FROM user WHERE is_active = 1 AND WHERE user_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (user_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return "TableUser -- read_user() Error: " + str(e)
        

    def update_user(self, payload):
        try:
            update_query = "UPDATE user SET username = %s, email = %s, hash = %s, firstname = %s, lastname = %s, is_active = %s, updated_at = %s, updated_by = %s WHERE is_active = 1 AND user_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(update_query, (payload['username'], payload['email'], payload['password'], payload['firstname'], payload['lastname'], payload['is_active'], payload['updated_at'], payload['updated_by'], payload['user_id']))

            self.db.connection.commit()
            cur.close()

            

            return payload
        except Exception as e:
            return "TableUser -- update_user() Error: " + str(e)
        

    def archive_user(self, user_id):
        try:
            update_query = "UPDATE user SET is_active = %s WHERE user_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(update_query, (False, user_id))

            self.db.connection.commit()
            cur.close()


            return user_id
        except Exception as e:
            return "TableUser -- archive_user() Error: " + str(e)
        

    def delete_user(self, user_id):
        try:
            delete_query = "DELETE FROM user WHERE user_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(delete_query, (user_id,))

            self.db.connection.commit()
            cur.close()

            response = {
                "username":payload['username'],
                "email":payload['email'],
                "is_active": True,
                "created_at": now,
                "user_id": user_id
            }

            return response
        except Exception as e:
            return "TableUser -- delete_user() Error: " + str(e)
        


    #V1
    def create_new_user(self, payload):
        try:
            insert_query = "INSERT INTO user (username, email, hash, is_active, created_at, user_id) VALUES(%s, %s, %s, %s, %s, %s)"

            now = datetime.now()
            user_id = uuid.uuid4()

            cur = self.db.connection.cursor()
            cur.execute(insert_query, (payload['username'], payload['email'], payload['password'], True, now, user_id))

            self.db.connection.commit()
            cur.close()

            response = {
                "username":payload['username'],
                "email":payload['email'],
                "is_active": True,
                "created_at": now,
                "user_id": user_id
            }

            return response
        except Exception as e:
            return "TableUser -- create_new_user() Error: " + str(e)

    def get_user_by_id(self, user_id):
        try:
            query = "SELECT * FROM user WHERE user_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (user_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return "TableUser -- get_user() Error: " + str(e) 
        
    def get_user_by_email(self, email):
        try:
            query = "SELECT * FROM user WHERE is_active = 1 AND email = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (email,))
            
            data = cur.fetchall()

            cur.close()

            (user, ) = data

            return user
        except Exception as e:
            return "TableUser -- get_user_by_email() Error: " + str(e) 