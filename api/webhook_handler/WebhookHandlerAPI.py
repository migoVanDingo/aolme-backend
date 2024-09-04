import json
from flask import Blueprint, current_app, jsonify, make_response, request
from flask_cors import CORS

from api.webhook_handler.handler.HandleProjectUpdate import HandleProjectUpdate

webhook_handler_api = Blueprint('webhook_handler_api', __name__)

CORS(webhook_handler_api)

@webhook_handler_api.route('/api/webhook-handler/project-created', methods=['POST'])
def handle_project_created():

    
    handler = HandleProjectUpdate(request.data)
    response = handler.do_process()


    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@webhook_handler_api.route('/api/webhook-handler/project-testing', methods=['POST'])
def handle_project_testing():

    current_app.logger.debug(f"WEBHOOK::::{request.data}")

    response = make_response("SUCCESS", 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response