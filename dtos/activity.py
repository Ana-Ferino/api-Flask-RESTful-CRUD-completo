from pydantic import BaseModel, Field

class ActivityDTO(BaseModel):
    name: str = Field(default=None, alias='nome')
    person_id: str = Field(default=None, alias='pessoa_id')
    person_name: str = Field(default=None, alias='pessoa_nome')