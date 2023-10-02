from flask_restful import Resource
from flask import request, current_app
from werkzeug.wrappers import Response
from dtos.login import LoginDTO
from services.auth.sessions import SessaoServices
from pydantic import ValidationError


class LoginController(Resource):

    def post(self) -> Response:
        sessao_services = SessaoServices()
        try:
            payload = request.get_json()
            user = payload.get('Auth', None)
            login_valid = sessao_services.validate_login_input(LoginDTO(**user))

            if login_valid:
                sessao_services.generate_auth_session_token(LoginDTO(**user))
                return 'Bem-vindo(a), {}!'.format(user['usuario']), 200

            current_app.logger.error('Unsuccessful login attempt | User >> {}'.format(user['usuario']))
            return 'ERROR: Please check the authentication information sent', 401

        except ValidationError as error:
            return {'errors': error.errors()}, 420
        except Exception as error:
            return 'ERROR: {}. Please check the authentication information sent'.format(error), 500  