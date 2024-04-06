from api.config.AbstractConfig import AbstractConfig
class RequestGetConfigListByEntity(AbstractConfig):
    def __init__(self, entity_id):
        self.entity_id = entity_id

    def do_process(self):
        return self.read_list_by_entity(self.entity_id)