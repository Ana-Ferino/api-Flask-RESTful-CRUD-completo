from models.usuarios import Usuarios
from models.database import db_session
from services.utils import encrypt_password
from dtos.usuario import UsuarioDTO
from dtos.signup import SignUpRequestDTO
from exceptions import UserAlreadyExistsError, UserNotExistsError


class UsuariosServices():  

    def get(self, username: str):
        user = Usuarios.query.filter_by(login=username).first()
        if user:
            return user
    
    def save(self, usuario: SignUpRequestDTO):
        user_already_exists = self.get(usuario.usuario)
        if user_already_exists:
            raise UserAlreadyExistsError
        
        hash = encrypt_password(usuario.senha)
        new_user = Usuarios(login=usuario.usuario, senha=hash)
        db_session.add(new_user)
        db_session.commit()
        db_session.close()

    def modify(self, usuario_atual: str, novo_usuario: UsuarioDTO):
        new_login = novo_usuario.login
        new_password = novo_usuario.senha

        if new_login:
            new_username_already_exists = self.get(new_login)
            if new_username_already_exists:
                raise UserAlreadyExistsError
        
        current_user = self.get(usuario_atual)
        
        if current_user:
            if new_login:
                current_user.login = new_login
            if new_password:
                hash_pw = encrypt_password(new_password)
                current_user.senha = hash_pw
            db_session.commit()
            db_session.close()
        else:
            db_session.close()
            raise UserNotExistsError
    
    def delete(self, usuario: UsuarioDTO):
        user_to_delete = self.get(usuario.login)

        if user_to_delete:
            db_session.delete(user_to_delete)
            db_session.commit()
            db_session.close()
        else:
            db_session.close()
            raise UserNotExistsError