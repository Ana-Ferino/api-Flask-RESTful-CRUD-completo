from pydantic import BaseModel, Field

class SignUpRequestDTO(BaseModel):
    usuario: str = Field(description='email do usuário', min_length=10, max_length=20)
    senha: str = Field(description='senha do usuário', min_length=10, max_length=16)