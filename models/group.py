from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  models import Base


class Group(Base):
    __tablename__ = 'group'

    id = Column("pk_group", Integer, primary_key=True)
    name = Column(String(140), unique=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o produto e o comentário.
    # Essa relação é implicita, não está salva na tabela 'produto',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    # comentarios = relationship("Comentario")

    def __init__(self, name:str,
                 created_at:Union[DateTime, None] = None,
                 updated_at:Union[DateTime, None] = None):
        """
        Creates a Group

        Arguments:
            name: group name.
            created_at: data de quando o produto foi inserido à base,
            updated_at: 
        """
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

        # se não for informada, será o data exata da inserção no banco
        if created_at:
            self.created_at = created_at

    # def adiciona_comentario(self, comentario:Comentario):
    #     """ Adiciona um novo comentário ao Produto
    #     """
    #     self.comentarios.append(comentario)

