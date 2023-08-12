from flask import Flask
from api.task.TaskAPI import task_api
from api.project.ProjectAPI import project_api
from api.export.ExportAPI import export_api
from api.file_import.ImportAPI import import_api
from api.storage.local.LocalStorageAPI import local_storage_api

app = Flask(__name__)

app.register_blueprint(task_api)
app.register_blueprint(project_api)
app.register_blueprint(export_api)
app.register_blueprint(import_api)
app.register_blueprint(local_storage_api)

@app.route("/")
def hello_world():
    return "Hello World"

if __name__ == "___main___":
    app.run(debug = True)