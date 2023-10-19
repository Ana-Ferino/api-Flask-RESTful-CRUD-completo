from services.auth.repository import AuthSessionRepository
from services.usuario_services import UsuariosServices
from dtos.login import LoginDTO
from dtos.usuario import UsuarioDTO
from config import AppConfig
from exceptions import UnauthorizedModification, UserNotExistsError
import datetime
import bcrypt
import jwt


class SessaoServices:

    def validate_login_input(self, usuario: LoginDTO) -> bool:
        password_encoded = usuario.Senha.encode('utf-8')
        user = UsuariosServices().get(usuario.Usuario)

        if user:
            validated = bcrypt.checkpw(password=password_encoded, hashed_password=user.senha)
            return validated
        
        raise UserNotExistsError
    

    def validate_token_in_db(self, token: LoginDTO) -> bool:
        user_input = self.decode_auth_session_token(auth_token=token.Token)
        user_in_db = AuthSessionRepository().get(token=token.Token)

        if user_in_db:
            return user_in_db == user_input
        
        return False
    

    def validate_user_on_request(self, token_logged_user: LoginDTO, user_to_modify: UsuarioDTO):
        user_that_made_request = user_to_modify.login
        user_in_db = AuthSessionRepository().get(token=token_logged_user.Token)

        if user_in_db == user_that_made_request:
            return True
        else:
            raise UnauthorizedModification


    def generate_auth_session_token(self, usuario: LoginDTO) -> str:
        now = datetime.datetime.utcnow()
        two_hours_from_now =  now + datetime.timedelta(hours=2)
        
        payload = {
            'exp': two_hours_from_now,
            'iat': now,
            'sub': usuario.Usuario
        }

        token = jwt.encode(
            payload,
            AppConfig.SecretsToken.SECRET_KEY,
            algorithm='HS256'
        )

        AuthSessionRepository().save(token=token, usuario=usuario.Usuario)
        return token
    

    def decode_auth_session_token(self, auth_token: str) -> str:
        '''
        Returns the user if auth_token is valid according to the secret
        '''
        payload = jwt.decode(jwt=auth_token, key=AppConfig.SecretsToken.SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
