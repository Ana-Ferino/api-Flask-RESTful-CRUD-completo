from flask import Flask, request
from flask_restful import Resource, Api
from models import Atividades, Usuarios, db_session
from flask_httpauth import HTTPBasicAuth
from repository.pessoas import PessoasRepository
from repository.atividades import AtividadesRepository
from repository.usuarios import UsuariosRepository
import bcrypt

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


@auth.verify_password 
def verificacao(login, senha):
    password_encoded = senha.encode('utf-8')
    usuarios = UsuariosRepository.query.all()
    dados_por_usuario = [{'id': i.id, 'login': i.login, 'senha': i.senha} for i in usuarios]
    for i in dados_por_usuario:
        if login in i.values():
            senha_bd = i.get('senha')
    db_session.close()
    if bcrypt.checkpw(password=password_encoded, hashed_password=senha_bd):
        return True
    return False


class Pessoas(Resource): 
    def get(self):
        pessoas = PessoasRepository.get()
        return pessoas
    
    @auth.login_required
    def post(self):
        dados = request.json
        retorno_adicao_de_registro = PessoasRepository.save(nome=dados['nome'], idade=dados['idade'])
        return retorno_adicao_de_registro

    @auth.login_required
    def put(self):
        dados = request.json
        retorno_modificacao = PessoasRepository.modify(id=dados['id'], 
                                                         nome=dados['nome'], 
                                                         idade=dados['idade'])
        return retorno_modificacao

    @auth.login_required
    def delete(self):
        dados = request.json
        retorno_exclusao = PessoasRepository.delete(id=dados['id'])
        return retorno_exclusao


class Atividades(Resource):
    def get(self):
        atividades = AtividadesRepository.get()
        return atividades

    @auth.login_required
    def post(self):
        dados = request.json
        retorno_adicao_de_atividade = AtividadesRepository.save(nome_atividade=dados['nome'],  
                                                                pessoa_id=dados['pessoa_id'])
        return retorno_adicao_de_atividade

    @auth.login_required
    def put(self):
        dados = request.json
        retorno_modificacao = AtividadesRepository.modify(id=dados['id'], 
                                                          nome_atividade=dados['nome'], 
                                                          pessoa_id=dados['pessoa_id'])
        return retorno_modificacao

    @auth.login_required
    def delete(self):
        dados = request.json
        retorno_exclusao = AtividadesRepository.delete(id=dados['id'])
        return retorno_exclusao


class Usuarios(Resource):
    def get(self):
        usuarios = UsuariosRepository.get()
        return usuarios
    
    @auth.login_required
    def post(self):
        dados = request.json
        registrar_usuario = UsuariosRepository.save(usuario=dados['usuario'], senha=dados['senha'])
        return registrar_usuario

    @auth.login_required
    def put(self):
        dados = request.json
        modificar_usuario = UsuariosRepository.modify(id=dados['id'], 
                                                      usuario=dados['usuario'], 
                                                      senha=dados['senha'])
        return modificar_usuario

    @auth.login_required
    def delete(self):
        dados = request.json
        deletar_usuario = UsuariosRepository.delete(id=dados['id'])
        return deletar_usuario


class Login(Resource):
    def get(self):
        dados_login = request.json
        usuario_verificado = verificacao(login=dados_login['usuario'], senha=dados_login['senha'])
        if usuario_verificado:
            return {'status': 'sucesso', 'mensagem': 'Login efetuado.'}
        return {'status': 'erro', 'mensagem': 'Usuário e/ou senha inválido.'}


api.add_resource(Pessoas, '/pessoas/')
api.add_resource(Atividades, '/atividades/')
api.add_resource(Usuarios, '/usuarios/')
api.add_resource(Login, '/login/')


if __name__ == '__main__':
    app.run(debug=True)
