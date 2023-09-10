from flask_restful import Api
from flask import Flask
from middleware import AuthMiddleware
from routes import setup_routes

app = Flask(__name__)
api = Api(app)

app.wsgi_app = AuthMiddleware(app.wsgi_app)

setup_routes(api)


if __name__ == '__main__':
    app.run(debug=True)
