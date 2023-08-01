from flask_restful import Resource
from services.auth.verify_login import validate_login_input
from flask import request


class LoginController(Resource):
    def get(self):
        dados_login = request.json
        usuario_verificado = validate_login_input(login=dados_login['usuario'], senha=dados_login['senha'])
        if usuario_verificado:
            return {'status': 'sucesso', 'mensagem': 'Login efetuado.'}
        else:
            return {'status': 'erro', 'mensagem': 'Usuário e/ou senha inválido.'}
