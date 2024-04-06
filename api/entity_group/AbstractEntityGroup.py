from abc import ABC, abstractmethod

class AbstractEntityGroup(ABC):
    def __init__(self, name, entities):
        self.name = name
        self.entities = entities


    def insert_entity(self, payload):
        pass

    def get_entity_group_by_id(self, group_id):
        pass

    def get_entity_group_by_entity_id(self, entity_id):
        pass

    def get_entity_list_by_type(self, entity_type):
        pass

    def archive_entity_group(self, group_id):
        pass

    def delete_entity_group(self, group_id):
        pass



    def insert_group_member(self, payload):
        pass

    def list_group_members(self, group_id):
        pass

    def remove_group_member(self, payload):
        pass


    @abstractmethod
    def do_process(self):
        pass
    

