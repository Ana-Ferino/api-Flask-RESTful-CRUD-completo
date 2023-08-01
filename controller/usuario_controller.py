from services.usuario_services import UsuariosServices
from flask_restful import Resource
from services.auth.verify_login import auth
from flask import request


class UsuariosController(Resource):
    def get(self):
        dados_por_usuario = UsuariosServices.get()
        return dados_por_usuario, 200
    
    @auth.login_required
    def post(self):
        dados = request.json
        registrar_usuario = UsuariosServices.save(usuario=dados['login'], senha=dados['senha'])
        return registrar_usuario
    
    @auth.login_required
    def put(self):
        dados = request.json
        modificar_usuario = UsuariosServices.modify(id=dados['id'], 
                                                    usuario=dados['login'], 
                                                    senha=dados['senha'])
        return modificar_usuario
    
    @auth.login_required
    def delete(self):
        dados = request.json
        deletar_usuario = UsuariosServices.delete(id=dados['id'])
        return deletar_usuario
