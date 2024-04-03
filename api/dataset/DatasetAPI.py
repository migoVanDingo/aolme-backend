import json
from flask import Blueprint, make_response, request
from flask_cors import CORS
from api.dataset.handler.RequestArchiveDataset import RequestArchiveDataset

from api.dataset.handler.RequestCreateDataset import RequestCreateDataset
from api.dataset.handler.RequestCreateSubset import RequestCreateSubset
from api.dataset.handler.RequestDeleteDataset import RequestDeleteDataset
from api.dataset.handler.RequestGetDatasetById import RequestGetDatasetById
from api.dataset.handler.RequestGetDatasetList import RequestGetDatasetList
from api.dataset.handler.RequestGetDatasetListByEntity import RequestGetDatasetListByEntity
from api.dataset.handler.RequestGetDatasetListByUser import RequestGetDatasetListByUser
from api.dataset.handler.RequestGetSubset import RequestGetSubset
from api.dataset.handler.RequestGetSubsetItems import RequestGetSubsetItems
from api.dataset.handler.RequestGetSubsetList import RequestGetSubsetList
from api.dataset.handler.RequestUpdateDataset import RequestUpdateDataset


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

    
    # repo_id = request.args.get('repo_id')

    # print("repoId: " + repo_id)

    
    # files = request.files.getlist('file')
    data = json.loads(request.data)
    
    # ENDPOINT LOGIC
    api_request = RequestCreateDataset(data)
    response = api_request.do_process()
    

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@dataset_api.route('/api/dataset', methods=['GET'])
def get_dataset_list():

    api_request = RequestGetDatasetList()
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@dataset_api.route('/api/dataset/<dataset_id>', methods=['GET'])
def get_dataset(dataset_id):

    api_request = RequestGetDatasetById(dataset_id)
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@dataset_api.route('/api/dataset/entity/<entity_id>', methods=['GET'])
def get_dataset_list_by_entity(entity_id):

    api_request = RequestGetDatasetListByEntity(entity_id)
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@dataset_api.route('/api/dataset/user/<user_id>', methods=['GET'])
def get_dataset_list_by_user(user_id):

    api_request = RequestGetDatasetListByUser(user_id)
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

# @dataset_api.route('/api/dataset/repo/<repo_id>', methods=['GET'])
# def get_dataset_list_by_repo(repo_id):

#     api_request = RequestGetDatasetListByRepo(repo_id)
#     response = api_request.do_process()
    
#     response = make_response(response, 200)
#     response.headers['Access-Control-Allow-Headers'] = '*'
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Content-Type'] = '*'
#     return response


@dataset_api.route('/api/dataset/<dataset_id>', methods=['PATCH'])
def update_dataset(dataset_id):

    api_request = RequestUpdateDataset(dataset_id, json.loads(request.data))
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@dataset_api.route('/api/dataset/<dataset_id>', methods=['DELETE'])
def delete_dataset(dataset_id):

    api_request = RequestDeleteDataset(dataset_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@dataset_api.route('/api/dataset/archive/<dataset_id>', methods=['DELETE'])
def archive_dataset(dataset_id):

    api_request = RequestArchiveDataset(dataset_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@dataset_api.route('/api/dataset/subset', methods=['POST', 'OPTIONS'])
def create_subset():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    files = request.files.getlist('file')
    data = request.form

    print("RequestCreateSubset::data: {}".format(data))
    
    # ENDPOINT LOGIC
    api_request = RequestCreateSubset(data, files)
    response = api_request.do_process()
    

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@dataset_api.route('/api/dataset/subset/<subset_id>', methods=['GET'])
def get_subset(subset_id):

    api_request = RequestGetSubset(subset_id)
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@dataset_api.route('/api/dataset/<dataset_id>/subset', methods=['GET'])
def get_subset_list(dataset_id):

    api_request = RequestGetSubsetList(dataset_id)
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@dataset_api.route('/api/dataset/subset/<subset_id>/item', methods=['GET'])
def get_subset_items(subset_id):

    api_request = RequestGetSubsetItems(subset_id)
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
