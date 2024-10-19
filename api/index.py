from flask import Flask
from fleask_restful import Api, Resource

app = Flask(__name__)
api = Api()

class Main(Resource):
    def get(self):
        return {"info": "someinfo", "num": 56}



api.add_resourse(Main, "/api/main")
api.init_app(app)

if __name__ == "__name__":
    app.run(debug=True)