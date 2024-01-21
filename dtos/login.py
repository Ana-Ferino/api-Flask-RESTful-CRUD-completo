from pydantic import BaseModel

class LoginDTO(BaseModel):
    Usuario: str = None
    Senha: str = None
    Token: str = None