from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from models import Base


class Expense(Base):
    __tablename__ = 'expense'

    id = Column("pk_expense", Integer, primary_key=True)
    description = Column(String(140))
    category = Column(String(140))
    value_usd = Column(Float())
    value_brl = Column(Float())
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, 
                 description:str,
                 category:str,
                 value_usd:float,
                 value_brl:float,
                 created_at:DateTime = datetime.now(),
                 updated_at:DateTime = datetime.now()):
        """
        Creates an Expense

        Arguments:
            description: expense description.
            category: expense category.
            value_usd: expense value in USD.
            value_brl: expense value in BRL.
            created_at: date of database insertion.
            updated_at: date of last database update.
        """
        self.description = description
        self.category = category
        self.value_usd = value_usd
        self.value_brl = value_brl
        self.created_at = created_at
        self.updated_at = updated_at


