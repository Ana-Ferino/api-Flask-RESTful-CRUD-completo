from models.database import db_session
from models.usuarios import Usuarios


def get_users_data() -> list[dict]:
    query_results_users = Usuarios.query.all()
    dados_por_usuario = [{'id': i.id, 'login': i.login, 'senha': i.senha} for i in query_results_users]
    db_session.close()
    return dados_por_usuario
