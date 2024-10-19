from flask import Flask
from flask_restful import Api, Resource  # Исправлено: 'fleask_restful' на 'flask_restful'

app = Flask(__name__)
api = Api(app)  # Инициализация API с приложением

class Main(Resource):
    def get(self):
        return {"info": "someinfo", "num": 56}

# Исправлено: 'add_resourse' на 'add_resource'
api.add_resource(Main, "/api/main")

if __name__ == "__main__":  # Исправлено: '__name__' на '__main__'
    app.run(debug=True)