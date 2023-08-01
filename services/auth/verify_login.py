from flask_httpauth import HTTPBasicAuth
from services.auth.users import get_users_data
import bcrypt

auth = HTTPBasicAuth()


@auth.verify_password 
def validate_login_input(login, senha):
    password_encoded = senha.encode('utf-8')

    users = get_users_data()
    for i in users:
        if login in i.values():
            password_user = i.get('senha')

    validated = bcrypt.checkpw(password=password_encoded, hashed_password=password_user)
    if validated:
        return True
    else:
        return False
