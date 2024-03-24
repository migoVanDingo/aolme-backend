import bcrypt
from abc import ABC, abstractmethod
from dao.TableUser import TableUser


class AbstractUser(ABC):
        
        def __init__(self):
            super().__init__()
            self.table_user = TableUser()

        def hash_password(self, password):
            bytes = password.encode('utf-8') 
            salt = bcrypt.gensalt() 

            return bcrypt.hashpw(bytes, salt) 
        
        def check_password(self, password, hash):
            userBytes = password.encode('utf-8') 
            hash = hash.encode('utf-8')
  
            # checking password 
            return bcrypt.checkpw(userBytes, hash)
            
        
        #Concrete methods
        def insert_user(self, params):
            return self.table_user.insert_user(params)
        
        def read_user(self, user_id):
            return self.table_user.read_user(user_id)
    
        def update_user(self, params):
            return self.table_user.update_user(params)
        
        def update_user_email(self, params, user_id):
            return self.table_user.update_user_email(params, user_id)
        
        def update_username(self, params, user_id):
            return self.table_user.update_username(params, user_id)
    
        def archive_user(self, user_id):
            return self.table_user.archive_user(user_id)
    
        def delete_user(self, user_id):
            return self.table_user.delete_user(user_id)
    
        #Abstract methods
        @abstractmethod
        def do_process(self):
            pass