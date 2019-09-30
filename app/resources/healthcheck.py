from flask_restful import Resource

class HealthcheckResource(Resource):
    def get(self):
        """
        This is a helthcheck endpoint
        ---
        responses:
            200:
                description: healthcolor

        """
        return {"status": "green"}, 200
