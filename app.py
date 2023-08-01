from controller.atividade_controller import AtividadeController
from controller.usuario_controller import UsuariosController
from controller.pessoa_controller import PessoasController
from controller.login_controller import LoginController
from flask_restful import Api
from flask import Flask

app = Flask(__name__)
api = Api(app)


api.add_resource(PessoasController, '/pessoas/')
api.add_resource(AtividadeController, '/atividades/')
api.add_resource(UsuariosController, '/usuarios/')
api.add_resource(LoginController, '/login/')


if __name__ == '__main__':
    app.run(debug=True)
