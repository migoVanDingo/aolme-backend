import os
from flask import Flask, flash, make_response, request, redirect, url_for
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json', 'mp4'}
UPLOAD_FOLDER = '/uploads'
class RequestUploadFiles:
    def __init__(self, files):
        self.files = files

    def do(self):
        

        """ if 'file' not in request.files:
                response = make_response('No file found', 500)
                return response """
        files = self.files
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
            
           
        
        response = make_response(file.filename, 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

