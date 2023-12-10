from pydantic import BaseModel
from typing import Optional, List
from models.expense import Expense


class ExpenseSchema(BaseModel):
    """ Define how new expense will be represented
    """
    description: str = "Expense 1"
    category: str = "Category 1"
    value: float = 1.0
    created_at: str = "2021-01-01 00:00:00"

class ExpenseSearchSchema(BaseModel):
    id: Optional[int] = 1

class ExpenseViewSchema(BaseModel):
    """ Define how expense will be returned
    """
    id: int = 1
    description: str = "Expense 1"
    category: str = "Category 1"
    value: float = 1.0
    created_at: str = "2021-01-01 00:00:00"
    updated_at: str = "2021-01-01 00:00:00"

def view_expense(expense: Expense):
    """ Retuns representation of expense defined in ExpenseViewSchema.
    """
    return {
        "id": expense.id,
        "description": expense.description,
        "category": expense.category,
        "value": expense.value,
        "created_at": expense.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": expense.updated_at.strftime("%Y-%m-%d %H:%M:%S")
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

class ExpenseStatsSchema(BaseModel):
    """ Define how new expense stats will be represented
    """
    total_transactions: int = 0
    total_value: float = 0.0