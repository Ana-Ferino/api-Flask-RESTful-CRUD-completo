from services.atividade_services import AtividadesServices
from services.auth.verify_login import auth
from flask_restful import Resource
from flask import request


class AtividadeController(Resource):
    def get(self):
        atividades = AtividadesServices.get()
        return atividades

    @auth.login_required
    def post(self):
        dados = request.json
        retorno_adicao_de_atividade = AtividadesServices.save(nome_atividade=dados['nome'],  
                                                              pessoa_id=dados['pessoa_id'])
        return retorno_adicao_de_atividade

    @auth.login_required
    def put(self):
        dados = request.json
        retorno_modificacao = AtividadesServices.modify(id=dados['id'], 
                                                        nome_atividade=dados['nome'], 
                                                        pessoa_id=dados['pessoa_id'])
        return retorno_modificacao

    @auth.login_required
    def delete(self):
        dados = request.json
        retorno_exclusao = AtividadesServices.delete(id=dados['id'])
        return retorno_exclusao
