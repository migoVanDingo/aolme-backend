import json
from flask import Blueprint, jsonify, make_response, request

from api.webhook_handler.handler.HandleProjectUpdate import HandleProjectUpdate

webhook_handler_api = Blueprint('webhook_handler_api', __name__)

@webhook_handler_api.route('/api/webhook-handler/project-created', methods=['POST'])
def handle_project_created():

    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    print('here webhook handler')
    # data = json.loads(request.data)
    # data = json.dumps(data)
    #print("json data: {}".format(data))
    handler = HandleProjectUpdate(request.data)
    response = handler.do_process()





    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response