from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
swagger = Swagger(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.resources.task import TaskResource 
from app.resources.healthcheck import HealthcheckResource

api.add_resource(HealthcheckResource, "/healthcheck")
api.add_resource(TaskResource, "/task/<int:task_id>", endpoint='get')
api.add_resource(TaskResource, "/task", endpoint='post')
if __name__ == "__main__":
    app.run(debug=True)

@app.shell_context_processor
def make_shell_context():
    from app.models.task import Task
    return {'db': db, 'Task': Task}