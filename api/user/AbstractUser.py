import bcrypt
from abc import ABC, abstractmethod
from dao.TableUser import TableUser


class AbstractUser(ABC):
        
        def __init__(self):
            pass

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
            request = TableUser()
            return request.insert_user(params)
        
        def read_user(self, user_id):
            return TableUser.read_user(user_id)
    
        def update_user(self, params):
            return TableUser.update_user(params)
    
        def archive_user(self, user_id):
            return TableUser.archive_user(user_id)
    
        def delete_user(self, user_id):
            return TableUser.delete_user(user_id)
    
        #Abstract methods
        @abstractmethod
        def do_process(self):
            pass