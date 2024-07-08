from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from datetime import datetime
from logger import logger

from sqlalchemy.exc import IntegrityError

from schemas import ExpenseSchema, ExpenseEditSchema, ExpenseViewSchema, ErrorSchema, ExpenseSearchSchema, ExpenseListViewSchema, ExpenseDeleteSchema
from schemas import view_expense_list, view_expense
from models import Session, Expense

from forex import Forex

expense_tag = Tag(
    name="Expenses", description="Add, visualize and remove expenses")
expenses_api = APIBlueprint('/expenses', __name__, url_prefix='', abp_tags=[expense_tag])
forex = Forex()

# ==============================|| Expense Endpoints ||============================== #

@expenses_api.post('/expenses', tags=[expense_tag],
          responses={"200": ExpenseViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_expense(form: ExpenseSchema):
    """Add a new Expense to the database

    Return representation of expense added.
    """
    try:
        usd_to_brl = forex.get_forex_usd_brl(form.created_at)

        expense = Expense(
            description=form.description,
            category=form.category,
            value_usd=float(form.value_usd),
            value_brl=float(form.value_usd)*float(usd_to_brl),
            created_at=datetime.strptime(form.created_at, "%Y-%m-%d"),
        )
        logger.debug(
            f"Add expense named: '{expense.description}' at {expense.created_at}")
    
        session = Session()
        session.add(expense)
        session.commit()
        logger.debug(f"Added expense named: '{expense.description}'")
        return view_expense(expense), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Expense of same name already saved :/"
        logger.warning(
            f"Error adding expense named: '{expense.description}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Not possible to save item :/"
        logger.warning(
            f"Error adding expense.', Exception:{e}")
        return {"mesage": error_msg}, 400

@expenses_api.put('/expenses', tags=[expense_tag],
          responses={"200": ExpenseViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def edit_expense(form: ExpenseEditSchema):
    """Edit existing Expense to the database

    Return representation of edited expense.
    """
    try:
        session = Session()
        expense = session.query(Expense).filter(Expense.id == form.id).first()
        logger.debug(
            f"Editing expense named: '{expense.description}' at {expense.created_at}")

        usd_to_brl = forex.get_forex_usd_brl(form.created_at)
        expense.description = form.description
        expense.category = form.category
        expense.value_usd = float(form.value_usd)
        expense.value_brl = float(form.value_usd)*float(usd_to_brl)
        expense.created_at = datetime.strptime(form.created_at, "%Y-%m-%d")
        expense.updated_at = datetime.now()

        session.add(expense)
        session.commit()
        logger.debug(f"Edited expense named: '{expense.description}'")
        return view_expense(expense), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Expense of same name already saved :/"
        logger.warning(
            f"Error adding expense named: '{expense.description}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Not possible to edit item :/"
        logger.warning(
            f"Error editing expense', Exception:{e}")
        return {"mesage": error_msg}, 400


@expenses_api.get('/expenses', tags=[expense_tag],
         responses={"200": ExpenseViewSchema, "404": ErrorSchema})
def get_expense(query: ExpenseSearchSchema):
    """Searches an expense from expense id

    Returns representation of expense found.
    """
    expense_id = query.id
    logger.debug(f"Collect data from expense #{expense_id}")
    session = Session()
    expense = session.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        error_msg = "Expense not found in the database :/"
        logger.warning(f"Error finding expense '{expense_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Expense found: '{expense.description}'")
        return view_expense(expense), 200


@expenses_api.get('/expense_all', tags=[expense_tag],
         responses={"200": ExpenseListViewSchema, "404": ErrorSchema})
def get_expenses():
    """List all expenses

    Retorns a list of expenses.
    """
    logger.debug(f"Fetching expense list")
    session = Session()
    expenses = session.query(Expense).order_by(Expense.created_at.desc()).all()
    if not expenses:
        error_msg = "Expenses not found in the database :/"
        logger.warning(f"Error fetching Expenses {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Returning expense list")
        return view_expense_list(expenses), 200


@expenses_api.delete('/expenses', tags=[expense_tag],
            responses={"200": ExpenseDeleteSchema, "404": ErrorSchema})
def del_expense(query: ExpenseSearchSchema):
    """Deletes a expense with id.

    Returns a confirmation message.
    """
    expense_id = query.id

    logger.debug(f"Deleting expense #{expense_id}")
    session = Session()

    if expense_id:
        count = session.query(Expense).filter(
            Expense.id == expense_id).delete()

    session.commit()
    if count:
        logger.debug(f"Deleting expense #{expense_id}")
        return {"message": "Expense removed!", "id": expense_id}
    else:
        error_msg = "Expenses not found in the database :/"
        logger.warning(f"Error deleting expense #'{expense_id}', {error_msg}")
        return {"message": error_msg}, 400

