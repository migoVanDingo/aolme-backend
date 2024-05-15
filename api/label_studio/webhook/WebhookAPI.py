from flask import Blueprint, current_app, jsonify, make_response, request
import json
from api.label_studio.webhook.entity.PayloadCreateWebhook import PayloadCreateWebhook

from api.label_studio.webhook.handler.RequestCreateWebhook import RequestCreateWebhook
from api.label_studio.webhook.handler.RequestDeleteWebhookInfo import RequestDeleteWebhookInfo
from api.label_studio.webhook.handler.RequestGetAllWebhookActions import RequestGetAllWebhookActions
from api.label_studio.webhook.handler.RequestGetWebhookInfo import RequestGetWebhookInfo
from api.label_studio.webhook.handler.RequestListAllWebhooks import RequestListAllWebhooks
from api.label_studio.webhook.handler.RequestSaveWebhookInfo import RequestSaveWebhookInfo
from api.label_studio.webhook.handler.RequestUpdateWebhookInfo import RequestUpdateWebhookInfo


webhook_api = Blueprint('webhook_api', __name__)

@webhook_api.route('/api/webhooks', methods=['POST'])
def create_webhook():

    data = json.loads(request.data)

    current_app.logger.info("WebhookAPI -- create_webhook() -- data: {}".format(data))
    validator = PayloadCreateWebhook()
    is_valid = validator.validate(data)
    if is_valid[0] is False:
        current_app.logger.error("WebhookAPI -- create_webhook() -- Error: {}".format(is_valid[1]))
        return is_valid[1]
    
    
    api_request = RequestCreateWebhook(data)
    response = api_request.do()
    current_app.logger.info("WebhookAPI -- create_webhook() -- response: {}".format(response))

    response = make_response(response)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@webhook_api.route('/api/webhooks/<project_id>', methods=['GET'])
def list_all_webhooks(project_id):

    api_request = RequestListAllWebhooks(project_id)
    response = api_request.do()
    return response

@webhook_api.route('/webhooks/info', methods=['GET'])
def get_webhook_actions():
    #data = json.loads(request.data)
    api_request = RequestGetAllWebhookActions()
    response = api_request.do()
    return response

@webhook_api.route('/webhooks/<webhook_id>', methods=['GET'])
def get_webhook_by_id(webhook_id):
    #data = json.loads(request.data)
    api_request = RequestGetWebhookInfo(webhook_id)
    response = api_request.do()
    return response

@webhook_api.route('/webhooks/<webhook_id>', methods=['PUT'])
def save_webhook_info(webhook_id):
    #data = json.loads(request.data)
    api_request = RequestSaveWebhookInfo(webhook_id)
    response = api_request.do()
    return response

@webhook_api.route('/webhooks/<webhook_id>', methods=['PATCH'])
def update_webhook(webhook_id):
    #data = json.loads(request.data)
    api_request = RequestUpdateWebhookInfo(webhook_id)
    response = api_request.do()
    return response

@webhook_api.route('/webhooks/<webhook_id>', methods=['DELETE'])
def delete_webhook_info(webhook_id):
    #data = json.loads(request.data)
    api_request = RequestDeleteWebhookInfo(webhook_id)
    response = api_request.do()
    return response