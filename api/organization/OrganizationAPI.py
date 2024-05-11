import json
from flask import Blueprint, jsonify, make_response, request
from flask_cors import CORS
from api.organization.handler.RequestArchiveOrganization import RequestArchiveOrganization

from api.organization.handler.RequestCreateOrganization import RequestCreateOrganization
from api.organization.handler.RequestDeleteOrganization import RequestDeleteOrganization
from api.organization.handler.RequestGetOrganizationById import RequestGetOrganizationById
from api.organization.handler.RequestGetOrganizationListByUserId import RequestGetOrganizationListByUserId
from api.organization.handler.RequestUpdateOrganization import RequestUpdateOrganization

organization_api = Blueprint('organization_api', __name__)
CORS(organization_api)

@organization_api.route('/api/organization', methods=['POST', 'OPTIONS'])
def create_organization():
    
    # ENDPOINT LOGIC
    api_request = RequestCreateOrganization(json.loads(request.data))
    response = api_request.do_process()

    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
    

@organization_api.route('/api/organization/<org_id>', methods=['GET'])
def get_organization_by_id(org_id):
    
    print("\norg_id: {}\n\n".format(org_id))
    # ENDPOINT LOGIC
    api_request = RequestGetOrganizationById(org_id)
    response = api_request.do_process()

    print("\nget_organization_by_id:::Response: {}\n\n".format(response))

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
    

@organization_api.route('/api/organization', methods=['GET'])
def get_organization_list():
        
        user_id = request.args.get('user_id')
        # ENDPOINT LOGIC
        api_request = RequestGetOrganizationListByUserId(user_id)
        response = api_request.do_process()
    
        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    
@organization_api.route('/api/organization/<org_id>', methods=['PATCH', 'OPTIONS'])
def update_organization_by_id(org_id):
    
    data = json.loads(request.data)

    # ENDPOINT LOGIC
    api_request = RequestUpdateOrganization(org_id, data)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
    

@organization_api.route('/api/organization/<org_id>', methods=['PATCH', 'OPTIONS'])
def archive_organization(org_id):

    
    # ENDPOINT LOGIC
    api_request = RequestArchiveOrganization(org_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
    

@organization_api.route('/api/organization/<org_id>', methods=['DELETE', 'OPTIONS'])
def delete_organization(org_id):
    # ENDPOINT LOGIC
    api_request = RequestDeleteOrganization(org_id)
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
    
