from flask import Blueprint
from flask_cors import CORS


entity_group_api = Blueprint('entity_group_api', __name__)
CORS(entity_group_api)

@entity_group_api.route('/entity_group', methods=['POST', 'OPTIONS'])
def create_entity_group():
    pass
