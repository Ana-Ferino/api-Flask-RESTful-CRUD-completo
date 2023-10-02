from pydantic import BaseModel
from pydantic import Field

class UsuarioDTO(BaseModel):
    login: str = Field(default=None, alias='user')
    senha: str = Field(default=None, alias='senha')