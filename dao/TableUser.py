from datetime import datetime

import uuid
class TableUser:
    def __init__(self):
        from main import db
        self.db = db

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
        
    def get_user_by_username(self, username):
        try:
            query = "SELECT * FROM user WHERE username = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (username,))
            
            data = cur.fetchall()

            cur.close()

            (user, ) = data

            return user
        except Exception as e:
            return "TableUser -- get_user_by_username() Error: " + str(e) 