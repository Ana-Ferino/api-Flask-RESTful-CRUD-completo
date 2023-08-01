from services.pessoa_services import PessoasServices
from services.auth.verify_login import auth
from flask_restful import Resource
from flask import request


class PessoasController(Resource):
    def get(self):
        pessoas = PessoasServices.get()
        return pessoas
    
    @auth.login_required
    def post(self):
        dados = request.json
        retorno_adicao_de_registro = PessoasServices.save(nome=dados['nome'], idade=dados['idade'])
        return retorno_adicao_de_registro

    @auth.login_required
    def put(self):
        dados = request.json
        retorno_modificacao = PessoasServices.modify(id=dados['id'], 
                                                     nome=dados['nome'], 
                                                     idade=dados['idade'])
        return retorno_modificacao

    @auth.login_required
    def delete(self):
        dados = request.json
        retorno_exclusao = PessoasServices.delete(id=dados['id'])
        return retorno_exclusao
