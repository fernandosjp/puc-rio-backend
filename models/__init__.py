from os import environ

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# importando os elementos definidos no modelo
from models.base import Base
from models.group import Group
from models.expense import Expense


# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
# db_url = 'sqlite:///database/db.sqlite3'
db_url = environ.get('DB_URL')

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False, pool_size=20, max_overflow=0)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine, checkfirst=True)
