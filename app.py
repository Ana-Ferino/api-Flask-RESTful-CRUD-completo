from flask_restful import Api
from flask import Flask, request
from middlewares.auth_middleware import AuthMiddleware
from routes import setup_routes
from config import AppConfig
from monitoring.log_config import custom_log

app = Flask(__name__)
api = Api(app)

app.wsgi_app = AuthMiddleware(app.wsgi_app)

setup_routes(api)

@app.errorhandler(Exception)
def handler_exception(error):
    app.logger.error(f"AN ERROR OCCURRED: {error}")


@app.after_request
def log_after_request(response):
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)

    app.logger.info(
        "path: %s | method: %s | status: %s | IP: %s",
        request.path,
        request.method,
        response.status,
        ip_addr
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)