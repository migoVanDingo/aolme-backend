from flask import Blueprint, request
import json

from api.webhook.handler.RequestCreateWebhook import RequestCreateWebhook
from api.webhook.handler.RequestDeleteWebhookInfo import RequestDeleteWebhookInfo
from api.webhook.handler.RequestGetAllWebhookActions import RequestGetAllWebhookActions
from api.webhook.handler.RequestGetWebhookInfo import RequestGetWebhookInfo
from api.webhook.handler.RequestListAllWebhooks import RequestListAllWebhooks
from api.webhook.handler.RequestSaveWebhookInfo import RequestSaveWebhookInfo
from api.webhook.handler.RequestUpdateWebhookInfo import RequestUpdateWebhookInfo

webhook_api = Blueprint('webhook_api', __name__)

@webhook_api.route('/webhooks', methods=['POST'])
def create_webhook():
    #data = json.loads(request.data)
    api_request = RequestCreateWebhook()
    response = api_request.do()
    return response

@webhook_api.route('/webhooks', methods=['GET'])
def list_all_webhooks():
    #data = json.loads(request.data)
    api_request = RequestListAllWebhooks()
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