from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Orchestrator(Resource):
    def post(self):
        hackbox_id : int
        hackbox_success : bool
        hackbox_id = request.form["id"]
        hackbox_success = request.form["success"]
        hackbox_data = request.form["data"]
        # TODO: Display the results of the hackbox in the software
        return {}, 200

api.add_resource(Orchestrator, "/")

if __name__ == '__main__':
    app.run()