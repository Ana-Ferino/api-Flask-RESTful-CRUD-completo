from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from dtos.login import LoginDTO
from services.auth.users import find_user_by_email
from services.auth.redis_data import get_token_by_user_id
import bcrypt

auth = HTTPBasicAuth()

@auth.verify_password 
def validate_login_input(usuario, senha) -> bool:
    password_encoded = senha.encode('utf-8')
    user = find_user_by_email(LoginDTO(usuario, senha))

    if user:
        validated = bcrypt.checkpw(password=password_encoded, hashed_password=user.senha)
        return validated
    
    return False


auth_with_token = HTTPTokenAuth()

@auth_with_token.verify_token
def validate_token(token, id_usuario) -> bool:
    token_bd = get_token_by_user_id(id_usuario)
    return token == token_bd