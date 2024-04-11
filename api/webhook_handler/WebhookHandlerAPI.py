import json
from flask import Blueprint, jsonify, make_response, request
from flask_cors import CORS

from api.webhook_handler.handler.HandleProjectUpdate import HandleProjectUpdate

webhook_handler_api = Blueprint('webhook_handler_api', __name__)

CORS(webhook_handler_api)

@webhook_handler_api.route('/api/webhook-handler/project-created', methods=['POST'])
def handle_project_created():

    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    #print('webhook_handler_api::handle_project_created::webhook_payload: {}'.format(request.data))
    # data = json.loads(request.data)
    # data = json.dumps(data)
    handler = HandleProjectUpdate(request.data)
    response = handler.do_process()





    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response