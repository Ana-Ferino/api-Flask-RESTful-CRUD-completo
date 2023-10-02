import bcrypt


def encrypt_password(senha: str) -> bytes:
    salt = bcrypt.gensalt()
    password_encoded = senha.encode('utf-8')
    hash = bcrypt.hashpw(password=password_encoded, salt=salt)
    return hash