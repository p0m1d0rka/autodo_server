from flask_restful import Resource, reqparse
from app.models.task import Task
from app import db

class TaskResource(Resource):
    def get(self, task_id):
        """
        Get one task
        ---
        parameters:
            - in: path
              name: task_id
              type: int
              required: true
              description: task id
        responses:
            200:
                description: A single task item
                id: Task
                properties:
                    title: string
                    description: Title of the task
            404:
                description: Task not found
        """
        task = Task.query.get(task_id)
        if task:
            return task.to_dict(), 200
        else:
            return {"error": f"Not found task with id={task_id}"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text')
        parser.add_argument('title')
        args = parser.parse_args()
        task = Task(title=args.title, text=args.text)
        db.session.add(task)
        db.session.commit()
        return {"status": "ok", "task": task.to_dict()}, 200

    def put(self):
        return {}, 200
    
    def delete(self, task_id):
        return {}, 200
    
