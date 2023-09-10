from dtos.login import LoginDTO
from services.auth.redis_data import save_token_in_db
from config import BaseConfig
import jwt
import datetime


class SessaoServices:
    def generate_auth_session_token(self, usuario: LoginDTO):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days= 0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': usuario.id
            }

            token = jwt.encode(
                payload,
                BaseConfig.SecretsToken.secret_key,
                algorithm='HS256'
            )

            save_token_in_db(usuario.id, token)
            return token
        except Exception as e:
            return e
    
    def decode_auth_session_token(auth_token) -> int | str:
        try:
            payload = jwt.decode(auth_token, BaseConfig.SecretsToken.secret_key)
            return payload['sub'], 200
        
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.', 401
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.', 498