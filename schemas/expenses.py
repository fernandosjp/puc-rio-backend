from pydantic import BaseModel
from typing import Optional, List, Dict, Union
from models.expense import Expense


class ExpenseSchema(BaseModel):
    """ Define how new expense will be represented
    """
    description: str = "Expense 1"
    category: str = "Category 1"
    value_usd: float = 1.0
    created_at: str = "2021-01-01"

class ExpenseEditSchema(BaseModel):
    """ Define how expense will be edit
    """
    id: int = 1
    description: str = "Expense 1"
    category: str = "Category 1"
    value_usd: float = 1.0
    created_at: str = "2021-01-01"

class ExpenseSearchSchema(BaseModel):
    id: Optional[int] = 1

class ExpenseViewSchema(BaseModel):
    """ Define how expense will be returned
    """
    id: int = 1
    description: str = "Expense 1"
    category: str = "Category 1"
    value_usd: float = 1.0
    value_brl: float = 1.0
    created_at: str = "2021-01-01"
    updated_at: str = "2021-01-01"

def view_expense(expense: Expense):
    """ Retuns representation of expense defined in ExpenseViewSchema.
    """
    return {
        "id": expense.id,
        "description": expense.description,
        "category": expense.category,
        "value_usd": expense.value_usd,
        "value_brl": expense.value_brl,
        "created_at": expense.created_at.strftime("%Y-%m-%d"),
        "updated_at": expense.updated_at.strftime("%Y-%m-%d")
    }

class ExpenseListViewSchema(BaseModel):
    groups: List[ExpenseViewSchema]

def view_expense_list(expenses):
    result = []
    for expense in expenses:
        result.append(view_expense(expense))
    return {"expenses": result}

class ExpenseDeleteSchema(BaseModel):
    message: str
    id: int
