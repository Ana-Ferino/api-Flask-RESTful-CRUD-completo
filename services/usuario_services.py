from models.usuarios import Usuarios
from models.database import db_session
from services.utils import criptografar_senha


class UsuariosServices():
    def get():
        usuarios = Usuarios.query.all()
        dados_por_usuario = [{'id': i.id, 'login': i.login} for i in usuarios]
        db_session.close()
        return dados_por_usuario
    
    def save(usuario, senha):
        hash = criptografar_senha(senha)
        novo_usuario = Usuarios(login=usuario, senha=hash)
        db_session.add(novo_usuario)
        db_session.commit()
        db_session.close()
        return {'status': 'sucesso', 'mensagem': 'Usuário registrado com sucesso.'}

    def modify(id, usuario, senha):
        hash = criptografar_senha(senha)
        user = Usuarios.query.filter_by(id=id).first()
        if user:
            user.login = usuario
            user.senha = hash
            db_session.commit()
            db_session.close()
            return {'status': 'sucesso', 'mensagem': 'Usuário editado com sucesso.'}
        db_session.close()
    
    def delete(id):
        usuario_a_deletar = Usuarios.query.filter_by(id=id).first()
        db_session.delete(usuario_a_deletar)
        db_session.commit()
        db_session.close()
        return {'status': 'sucesso', 'mensagem': 'Usuário excluído com sucesso.'}
