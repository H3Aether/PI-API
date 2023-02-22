from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

HACKBOX_ID = 1

class Hackbox(Resource):
    def get(self):
        # TODO: Get the status of the hackbox
        status = "unknown"
        return {"id": HACKBOX_ID, "status": status}, 200

    def post(self):
        orchestrator_action : str
        orchestrator_action = request.form["action"] # "start" or "stop"
        if orchestrator_action == "start":
            # TODO: Start the hackbox
            status = "started"
        elif orchestrator_action == "stop":
            # TODO: Stop the hackbox
            status = "stopped"
        else:
            return {"error": "Unknown action (valid actions are 'start' and 'stop')"}, 400
        return {"id": HACKBOX_ID, "status": status}, 200

api.add_resource(Hackbox, "/")

if __name__ == '__main__':
    app.run()