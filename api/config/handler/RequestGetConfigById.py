from flask import jsonify
from api.config.AbstractConfig import AbstractConfig


class RequestGetConfigById(AbstractConfig):
    def __init__(self, config_id):
        super().__init__()
        self.config_id = config_id

    def do_process(self):
        try:
            print("RequestGetConfigById -- do_process() -- config_id: " +
                str(self.config_id))
            response = self.read_item(self.config_id)
            print("RequestGetConfigById -- do_process() -- response: " +
                str(response))
            return jsonify(response)

        except Exception as e:
            print("RequestGetConfigById -- do_process() Error: " + str(e))
            return "RequestGetConfigById -- do_process() Error: " + str(e)
