from sqlalchemy import Column, Integer, String
from models.database import Base


class Pessoas(Base): 
    __tablename__ = 'pessoas' 
    id = Column(Integer, primary_key=True) 
    nome = Column(String(40), index=True)
    idade = Column(Integer)