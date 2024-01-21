from pydantic import BaseModel, Field

class PersonDTO(BaseModel):
    name: str = Field(default=None, alias='nome')
    age: str = Field(default=None, alias='idade')