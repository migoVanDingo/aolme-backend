from abc import ABC, abstractmethod

from dao.TableUser import TableUser

class AbstractUser(ABC):
        
        def __init__(self):
            pass

        def hash_password(self, password):
            return TableUser.hash_password(password)
        
        #Concrete methods
        def insert_user(params):
            return TableUser.insert_user(params)
        
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