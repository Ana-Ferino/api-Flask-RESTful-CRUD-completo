from werkzeug.wrappers import Request, Response
from services.auth.verify_login import validate_login_input, validate_token


class AuthMiddleware():
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        request = Request(environ)
        usuario = request.authorization['usuario']
        senha = request.authorization['senha']
        token = request.authorization['token']

        login_validado = validate_login_input(usuario, senha)
        token_validado = validate_token(token)

        if login_validado and token_validado:
            res = Response(u'Successful authorization', mimetype='text/plain', status=200)
            return self.app(environ, start_response)
        
        res = Response(u'Authorization failed', mimetype='text/plain', status=401)
        return res(environ, start_response)