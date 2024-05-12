from flask import current_app, jsonify
from api.config.AbstractConfig import AbstractConfig


class RequestGetConfigById(AbstractConfig):
    def __init__(self, config_id):
        super().__init__()
        self.config_id = config_id

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: config_id: {self.config_id}")

            response = self.read_item(self.config_id)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return jsonify(response)

        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestGetConfigById -- do_process() Error: " + str(e)
