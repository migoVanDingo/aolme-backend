from flask import current_app
from api.config.AbstractConfig import AbstractConfig

class RequestUpdateConfig(AbstractConfig):
    def __init__(self, config_id, params):
        self.config_id = config_id
        self.params = params

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: config_id: {self.config_id}")
            response = self.update(self.config_id, self.params)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestUpdateConfig -- do_process() Error: " + str(e)