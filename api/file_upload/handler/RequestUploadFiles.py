import os
from time import sleep
from flask import Flask, current_app, flash, make_response, request, redirect, url_for
from werkzeug.utils import secure_filename
from api.file_upload.FileUtility import FileUtility
from api.subprocess.handler.HandleUploadGroundTruthLabelStudio import HandleUploadGroundTruthLabelStudio

from dao.TableFiles import TableFiles
from dao.TableLsImportStorage import TableLsImportStorage


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json', 'mp4', 'xlsx'}
UPLOAD_FOLDER = '/uploads'
class RequestUploadFiles:
    def __init__(self, project_id, files, repo_id, file_set_id):
        self.files = files
        self.project_id = project_id
        self.count = 0
        self.final_path = ''
        self.gt_path = ''
        self.repo_id = repo_id
        self.file_set_id = file_set_id

    def do(self):
        
        current_app.logger.info(f"{self.__class__.__name__} :: project_id: {self.project_id} :: repo_id: {self.repo_id} :: file_set_id: {self.file_set_id}")
        """ if 'file' not in request.files:
                response = make_response('No file found', 500)
                return response """
        files = self.files
        #print(len(files))


        # If the user does not select a file, the browser submits an
        # empty file without a filename.

        

        repo_path = os.path.join(os.environ['REPO_DIRECTORY'], self.repo_id)
        xlsx_switch = False



        for file in files:

            if file.filename == '':
                current_app.logger.error(f"{self.__class__.__name__} :: Error ::File must have name")
                response = make_response('File must have name', 500)
                return response
    

            current_app.logger.info(f"{self.__class__.__name__} :: file: {file.filename}")
            # Create the uploads directory
            # current_directory = os.getcwd()
            
            # uploads_directory = os.path.join(current_directory, 'project')
          
            if file and allowed_file(file.filename):
                #filename = secure_filename(file.filename)

                #working code 
                # print(os.path.join(uploads_directory, file.filename))
                # final_path = os.path.join(uploads_directory, file.filename)
                
                f = file.filename
                filename = f.split('.')


                #test code
                payload = {
                    'filename': file.filename
                }
                table_files = TableFiles()
                if self.count == 0:
                    self.final_path = table_files.make_directory_videos(self.project_id, repo_path)
                    self.gt_path = table_files.make_directory_raw_gt(self.project_id, repo_path)
                    
                file_type = ''
                match filename[1]:
                    case 'mp4':
                        save_path = os.path.join(self.final_path, file.filename)
                        current_app.logger.info(f"{self.__class__.__name__} :: Save video files: {save_path}")
                        file.save(save_path)
                        file_type = "VIDEO"
                    
                    case 'xlsx':
                        xlsx_switch = True
                        print('Save xlsx files')
                        save_path = os.path.join(self.gt_path, file.filename)
                        table_files.make_directory_reformat_gt(self.project_id, repo_path)
                        current_app.logger.info(f"{self.__class__.__name__} :: Save xlsx files: {save_path}")
                        file.save(save_path)
                        sleep(1)
                        FileUtility.signal_reformat_xlsx(self.repo_id, self.file_set_id)
                        file_type = "GROUND_TRUTH_RAW_XLSX_VJ"
                        

                    case _:
                        print("The file didn't match, extention: {}".format(filename[1]))
                        current_app.logger.error(f"{self.__class__.__name__} :: The file didn't match, extention: {filename[1]}")
                
                
                

                
                #print("filename: {}".format(filename[0]))
                #print("ext: {}".format(filename[1]))

                payload = {
                    'project_id': self.project_id,
                    'path': save_path,
                    'name': filename[0],
                    'extension':filename[1],
                    'file_type': file_type
                }


                current_app.logger.info(f"{self.__class__.__name__} :: create-file-info-payload: {payload}")
                insert_file = table_files.create_file_info(payload)

                #print(insert_file)
                
                if insert_file == 'success':
                    response = payload

                #print(jsonify(url_for('download_file', name=file.filename)))
            
            self.count = self.count + 1

        
        local_storage_directory = FileUtility.signal_create_local_storage(self.project_id, self.repo_id)
        current_app.logger.info(f"{self.__class__.__name__} :: local_storage_directory: {local_storage_directory}")
        move_files_response = FileUtility.move_files_to_local_storage(self.project_id, self.repo_id)

        current_app.logger.info(f"{self.__class__.__name__} :: Response: {move_files_response}")
        return move_files_response
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

