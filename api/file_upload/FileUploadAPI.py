import os
from flask import Blueprint, jsonify, make_response, request, flash, url_for
import json
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename


file_upload_api = Blueprint('file_upload_api', __name__)
CORS(file_upload_api)

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json', 'csv'}

@file_upload_api.route("/upload", methods=['POST', 'OPTIONS'])
def upload_files():
    
    
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'

        return response

    """ if 'file' not in request.files:
        response = make_response('No file found', 500)
        return response """
    
    files = request.files.getlist('file')
    print(len(files))


        # If the user does not select a file, the browser submits an
        # empty file without a filename.

    for file in files:

        if file.filename == '':
            response = make_response('File must have name', 500)
            return response
    
        # Create the uploads directory
        current_directory = os.getcwd()
        uploads_directory = os.path.join(current_directory, 'uploads')
    
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            print(os.path.join(uploads_directory, file.filename))
            file.save(os.path.join(uploads_directory, file.filename))
            #print(jsonify(url_for('download_file', name=file.filename)))
            
        print(file.filename)

    data = request.form
    project_name = data["project_name"]
    project_description = data['project_description']
    project_owner = data['project_owner']

    print(project_name)
    print(project_description)
    print(project_owner)

    


    

    #print(uploads_directory)
    # Save the file to the uploads directory



    
    response = make_response('success', 200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

