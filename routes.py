from flask_restful import Api
from controller.atividade_controller import AtividadeController
from controller.login_controller import LoginController
from controller.pessoa_controller import PessoasController
from controller.usuario_controller import UsuariosController


def setup_routes(api: Api):
    api.add_resource(PessoasController, '/pessoas/')
    api.add_resource(AtividadeController, '/atividades/')
    api.add_resource(UsuariosController, '/usuarios/')
    api.add_resource(LoginController, '/login/')