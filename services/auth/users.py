from controller.login_controller import LoginDTO
from models.database import db_session
from models.usuarios import Usuarios


def find_user_by_email(login: LoginDTO):
    usuario = Usuarios.query.filter_by(email=login.usuario).first()

    if usuario:
        return usuario
    
    return None

def get_users_data() -> list[dict]:
    query_results_users = Usuarios.query.all()
    dados_por_usuario = [
        {
            'id': i.id, 
            'login': i.login,
            'senha': i.senha
        } 
        for i in query_results_users
    ]
    db_session.close()
    return dados_por_usuario
