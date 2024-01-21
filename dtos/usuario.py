from pydantic import BaseModel, Field

class UsuarioDTO(BaseModel):
    login: str = Field(default=None, alias='user')
    senha: str = Field(default=None, alias='senha')