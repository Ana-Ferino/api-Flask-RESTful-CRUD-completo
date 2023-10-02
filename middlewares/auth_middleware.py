from services.auth.sessions import SessaoServices
from werkzeug.wrappers import Request, Response
from jwt.exceptions import ExpiredSignatureError, DecodeError
from exceptions import UserNotExistsError
from dtos.login import LoginDTO


class AuthMiddleware():
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        request = Request(environ)

        if ('sign-up' in request.path 
            or 'login' in request.path):
            return self.app(environ, start_response)

        token = request.headers.get('Authorization')
        user_credentials = request.get_json().get('Auth', None)
        session_services = SessaoServices()

        token_valid = False
        login_valid = False

        try:
            if user_credentials:
                login_valid = session_services.validate_login_input(LoginDTO(**user_credentials))
            
            if token:
                token_valid = session_services.validate_token_in_db(LoginDTO(token=token))
        
        except ExpiredSignatureError:
            res = Response('Please try to log in again.', mimetype='text/plain', status=401)
            return res(environ, start_response)
        except DecodeError:
            res = Response('Invalid token. Verify the authenticity of the token.', mimetype='text/plain', status=401)
            return res(environ, start_response)
        except UserNotExistsError as une:
            res = Response('{}'.format(une), mimetype='text/plain', status=500)
            return res(environ, start_response)
        except Exception as error:
            res = Response('An error occurred: {}. Please check the authentication information sent'.format(error), mimetype='text/plain', status=500)
            return res(environ, start_response)

        if token_valid or login_valid:
            environ['json'] = request.get_json()
            return self.app(environ, start_response)

        res = Response(u'Authorization failed', mimetype='text/plain', status=401)
        return res(environ, start_response)