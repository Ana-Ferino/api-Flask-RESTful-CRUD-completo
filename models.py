import sqlalchemy.orm
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))

Base = sqlalchemy.orm.declarative_base()
Base.query = db_session.query_property()


class Pessoas(Base): 
    __tablename__ = 'pessoas' 
    id = Column(Integer, primary_key=True) 
    nome = Column(String(40), index=True)
    idade = Column(Integer)


class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas") 


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(150))


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
