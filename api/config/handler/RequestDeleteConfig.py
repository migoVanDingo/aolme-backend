from flask import current_app
from api.config.AbstractConfig import AbstractConfig

class RequestDeleteConfig(AbstractConfig):
    def __init__(self, config_id):
        self.config_id = config_id

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: config_id: {self.config_id}")
            response = self.delete(self.config_id)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
