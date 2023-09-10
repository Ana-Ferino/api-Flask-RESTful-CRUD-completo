from pydantic import BaseModel


class LoginDTO(BaseModel):
    id: int
    usuario: str
    senha: str