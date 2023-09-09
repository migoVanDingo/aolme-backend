import os
from flask import Flask, flash, make_response, request, redirect, url_for
from werkzeug.utils import secure_filename

from dao.TableFiles import TableFiles


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json', 'mp4'}
UPLOAD_FOLDER = '/uploads'
class RequestUploadFiles:
    def __init__(self, project_id, files):
        self.files = files
        self.project_id = project_id
        self.count = 0
        self.final_path = ''

    def do(self):
        

        """ if 'file' not in request.files:
                response = make_response('No file found', 500)
                return response """
        files = self.files
        #print(len(files))


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

                #working code 
                # print(os.path.join(uploads_directory, file.filename))
                # final_path = os.path.join(uploads_directory, file.filename)
                
                #test code
                payload = {
                    'filename': file.filename
                }
                table_files = TableFiles()
                if self.count == 0:
                    self.final_path = table_files.make_directory(self.project_id)
                
                save_path = os.path.join(self.final_path, file.filename)
                
                file.save(save_path)

                f = file.filename
                filename = f.split('.')
                #print("filename: {}".format(filename[0]))
                #print("ext: {}".format(filename[1]))

                payload = {
                    'project_id': self.project_id,
                    'path': save_path,
                    'name': filename[0],
                    'extension':filename[1],
                    'file_type': 'UPLOAD'
                }

                insert_file = table_files.create_file_info(payload)

                #print(insert_file)
                
                if insert_file == 'success':
                    response = payload

                #print(jsonify(url_for('download_file', name=file.filename)))
            
            self.count = self.count + 1
        
        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

