import os

from flask import current_app
from api.files.AbstractFiles import AbstractFiles
from dao.TableFiles import TableFiles

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json', 'mp4', 'xlsx'}
class RequestUploadFile(AbstractFiles):
    def __init__(self, data, files):
        self.files = files
        self.data = data

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: payload: {self.data}")
            for file in self.files:

                if file.filename == '':
                    current_app.logger.error("FILE_MUST_HAVE_NAME")
                    return "FILE_MUST_HAVE_NAME", 500
                
                current_directory = os.getcwd()

                uploads_directory = os.path.join(current_directory, 'organization')

                uploads_directory = os.path.join(uploads_directory, self.data['org_id'])

                current_app.logger.info(f"{self.__class__.__name__} :: uploads_directory: {uploads_directory}")

                # match self.data["type"]:
                #     case 'DATASET':
                #         save_path = os.path.join(uploads_directory, 'datasets')
                #         file
                    
                #     case 'MODULE':

                #     case 'CONFIG':

                #     case 'EXPERIMENT':

                #     case 'FILE':

                    
                #     case _:
                #         print("The file didn't match, extention: {}".format(filename[1]))

                if file and allowed_file(file.filename):
                    f = file.filename
                    filename = f.split('.')

                    table_files = TableFiles()



                
            #check if file is allowed
                

            #upload file to proper directory

            #create file entry payload for DB

            #insert file entry into DB

            response = self.insert_file(self.data['file_name'], self.data['file_content'])
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
        

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS