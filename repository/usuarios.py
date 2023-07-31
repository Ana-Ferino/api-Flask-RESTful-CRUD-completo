from models import Usuarios, db_session
import bcrypt


class UsuariosRepository(Usuarios):
    def __init__(self, usuario, senha):
        self.login = usuario
        self.senha = senha

    def get():
        usuarios = UsuariosRepository.query.all()
        dados_por_usuario = [{'id': i.id, 'login': i.login} for i in usuarios]
        db_session.close()
        return dados_por_usuario, 200

    def modify(id, usuario, senha):
        salt = bcrypt.gensalt()
        try:
            password_encoded = senha.encode('utf-8')
            hash = bcrypt.hashpw(password=password_encoded, salt=salt)
            user = UsuariosRepository.query.filter_by(id=id).first()
            if user:
                user.login = usuario
                user.senha = hash
                db_session.commit()
                db_session.close()
                return {'status': 'sucesso', 'mensagem': 'Usuário editado com sucesso.'}, 200
            db_session.close()
        except Exception:
            return {'status': 'erro', 'mensagem': 'ocorreu um erro, verifique os dados enviados.'}
    
    def save(usuario, senha):
        salt = bcrypt.gensalt()
        try:
            password_encoded = senha.encode('utf-8')
            hash = bcrypt.hashpw(password=password_encoded, salt=salt)
            novo_usuario = UsuariosRepository(usuario=usuario, senha=hash)
            db_session.add(novo_usuario)
            db_session.commit()
            db_session.close()
            return {'status': 'sucesso', 'mensagem': 'Usuário criado com sucesso.'}, 200
        except TypeError:
            return {'status': 'erro', 'mensagem': 'A senha deve ser enviada como string.'}, 400
        except Exception:
            return {'status': 'erro', 'mensagem': 'ocorreu um erro, verifique os dados enviados.'}

    def delete(id):
        try:
            usuario_a_deletar = UsuariosRepository.query.filter_by(id=id).first()
            db_session.delete(usuario_a_deletar)
            db_session.commit()
            db_session.close()
            return {'status': 'sucesso', 'mensagem': 'Usuário excluído com sucesso.'}, 200
        except Exception:
            return {'status': 'erro', 'mensagem': 'ocorreu um erro, verifique os dados enviados.'}
