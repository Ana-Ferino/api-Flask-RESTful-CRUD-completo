from pydantic import BaseModel
from pydantic import Field


class LoginDTO(BaseModel):
    Usuario: str = Field(default=None, alias='usuario')
    Senha: str = Field(default=None, alias='senha')
    Token: str = Field(default=None, alias='token')

    class Config:
        populate_by_name =  True