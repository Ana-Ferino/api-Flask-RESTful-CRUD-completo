from flask_restful import Api
from flask import Flask

from routes import setup_routes

app = Flask(__name__)
api = Api(app)

setup_routes(api)


if __name__ == '__main__':
    app.run(debug=True)
