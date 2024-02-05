from flask import Blueprint, make_response, request
from flask_cors import CORS


dataset_api = Blueprint('dataset_api', __name__)
CORS(dataset_api)

@dataset_api.route('/api/dataset', methods=['POST', 'OPTIONS'])
def create_dataset():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    print("data: {}".format(request.data))
    
    # ENDPOINT LOGIC
    

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@dataset_api.route('/api/dataset', methods=['GET'])
def get_datasets():
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@dataset_api.route('/api/dataset/<dataset_id>', methods=['GET'])
def get_dataset(dataset_id):
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@dataset_api.route('/api/dataset/<dataset_id>', methods=['PUT'])
def update_dataset(dataset_id):
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@dataset_api.route('/api/dataset/<dataset_id>', methods=['DELETE'])
def delete_dataset(dataset_id):
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@dataset_api.route('/api/dataset/archive/<dataset_id>', methods=['DELETE'])
def archive_dataset(dataset_id):
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
