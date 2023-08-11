from flask import Flask
from api.task.TaskAPI import task_api

app = Flask(__name__)

app.register_blueprint(task_api)

@app.route("/")
def hello_world():
    return "Hello World"

if __name__ == "___main___":
    app.run(debug = True)