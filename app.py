from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from datetime import datetime
import pandas as pd

from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func

from models import Session, Group, Expense
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Personal Finance Manager", version="0.0.1")
app = OpenAPI(__name__, info=info)
CORS(app)

# Define documentation tags
home_tag = Tag(name="Documentation",
               description="Documentation framework: Swagger, Redoc or RapiDoc")
expense_tag = Tag(
    name="Expenses", description="Add, visualize and remove expenses")
group_tag = Tag(name="Groups", description="Add, visualize and remove groups")

# ==============================|| Home Endpoint ||============================== #


@app.get('/', tags=[home_tag])
def home():
    """Redirect to /openapi, screen that lets you choose type of documentation.
    """
    return redirect('/openapi')

# ==============================|| Expense Endpoints ||============================== #


@app.post('/expenses', tags=[expense_tag],
          responses={"200": ExpenseViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_expense(form: ExpenseSchema):
    """Add a new Expense to the database

    Return representation of expense added.
    """
    expense = Expense(
        description=form.description,
        category=form.category,
        value=float(form.value),
        created_at=datetime.strptime(form.created_at, "%Y-%m-%d"),
    )
    logger.debug(
        f"Add expense named: '{expense.description}' at {expense.created_at}")
    try:
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
            f"Error adding expense named: '{expense.description}', Exception:{e}")
        return {"mesage": error_msg}, 400


@app.get('/expenses', tags=[expense_tag],
         responses={"200": ExpenseViewSchema, "404": ErrorSchema})
def get_expense(query: ExpenseSearchSchema):
    """Searches an expense from expense id

    Returns representation of expense found.
    """
    expense_id = query.id
    logger.debug(f"Colect data from expense #{expense_id}")
    session = Session()
    expense = session.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        error_msg = "Expense not found in the database :/"
        logger.warning(f"Error finding expense '{expense_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Expense found: '{expense.description}'")
        return view_expense(expense), 200


@app.get('/expense_all', tags=[expense_tag],
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
        logger.debug(f"Retorning expense list")
        return view_expense_list(expenses), 200


@app.delete('/expenses', tags=[expense_tag],
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


@app.get('/expense_stats', tags=[expense_tag],
         responses={"200": ExpenseStatsViewSchema, "404": ErrorSchema})
def get_expense_stats():
    """Get expense stats such as total transactions and total value.

    Retorns stats.
    """
    logger.debug(f"Getting expense stats")
    session = Session()
    total_transactions = session.query(Expense).count()
    total_value = session.query(func.sum(Expense.value)).all()[0][0]
    if not total_transactions or not total_value:
        error_msg = "Error calculating stats :/"
        logger.warning(f"{error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(
            f"Getting expense stats {total_transactions} and {total_value}")
        return {
            "total_transactions": str(total_transactions),
            "total_transactions_perc": str(15.5),
            "total_value": str(total_value),
            "total_value_perc": str(-10.5)}, 200


@app.get('/expense_stats_timeseries', tags=[expense_tag],
         responses={"200": ExpenseStatsTimeseriesViewSchema, "404": ErrorSchema})
def get_expense_stats_timeseries():
    """Get expense monthly stats.

    Retorns stats.
    """
    logger.debug(f"Getting expense timeseries stats")

    number_of_months = 11
    try:
        session = Session()
        transactions_month = session.query(func.strftime(
            "%Y-%m-01", Expense.created_at), func.count(Expense.id)).group_by(func.strftime(
                "%Y-%m-01", Expense.created_at)).order_by(Expense.created_at.asc()).limit(number_of_months).all()
        logger.debug(f"transactions_month: {transactions_month}")
        transaction_data, transaction_categories = create_api_response(
            transactions_month, number_of_months)

        value_spent_month = session.query(func.strftime(
            "%Y-%m-01", Expense.created_at), func.sum(Expense.value)).group_by(func.strftime(
                "%Y-%m-01", Expense.created_at)).order_by(Expense.created_at.asc()).limit(number_of_months).all()
        logger.debug(f"value_spent_month: {value_spent_month}")
        value_spent_data, value_spent_categories = create_api_response(
            value_spent_month, number_of_months)

        return {
            "transactions": {
                "data": transaction_data,
                "categories": transaction_categories,
            },
            "value": {
                "data": value_spent_data,
                "categories": value_spent_categories,
            },
        }, 200
    except Exception as e:
        error_msg = "Error calculating stats"
        logger.warning(f"{error_msg}:{e}")
        return {"mesage": error_msg}, 400


def create_api_response(query_response, number_of_months):
    """Create a response object with the query response

    Args:
        query_response (list): list of tuples with the query response

    Returns:
        dict: dictionary with the response
    """
    data = []
    categories = []

    # Fill in with missing months
    column_names=["month","data"]
    df = pd.DataFrame(query_response, columns=column_names)
    df['month']= pd.to_datetime(df['month'])
    most_recent_month = df['month'].max()
    first_month = pd.to_datetime(most_recent_month, format="%Y-%m-%d") - pd.DateOffset(months=number_of_months-1)
    
    new_date_range = pd.date_range(start=first_month, end=most_recent_month, freq="MS")
    df = df.set_index("month")
    df = df.reindex(new_date_range, fill_value=0)

    data = df['data'].values.tolist()
    categories = df.index.strftime("%b-%y").tolist()

    return data, categories


# ==============================|| Groups Endpoints ||============================== #


@ app.post('/groups', tags=[group_tag],
           responses={"200": GroupViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_group(form: GroupSchema):
    """Add a new Group to the database

    Return representation of products and comments
    """
    group = Group(name=form.name)
    logger.debug(f"Add group named: '{group.name}'")
    try:
        session = Session()
        session.add(group)
        session.commit()
        logger.debug(f"Add group named: '{group.name}'")
        return view_group(group), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Group of same name already saved :/"
        logger.warning(
            f"Error adding group named: '{group.name}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Not possible to save item :/"
        logger.warning(
            f"Error adding group named: '{group.name}', {error_msg}")
        return {"mesage": error_msg}, 400


@ app.get('/groups', tags=[group_tag],
          responses={"200": GroupViewSchema, "404": ErrorSchema})
def get_group(query: GroupSearchSchema):
    """Faz a busca por um Produto a partir do id do produto

    Retorna uma representação dos produtos e comentários associados.
    """
    group_id = query.id
    logger.debug(f"Colect data from group #{group_id}")
    session = Session()
    group = session.query(Group).filter(Group.id == group_id).first()
    if not group:
        error_msg = "Group not found in the database :/"
        logger.warning(f"Error finding group '{group_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Group found: '{group.name}'")
        return view_group(group), 200


@ app.get('/group_all', tags=[group_tag],
          responses={"200": GroupListViewSchema, "404": ErrorSchema})
def get_produtos():
    """List all groups

    Retorns a list of groups.
    """
    logger.debug(f"Fetching group list")
    session = Session()
    groups = session.query(Group).all()
    if not groups:
        error_msg = "Groups not found in the database :/"
        logger.warning(f"Error fetching groups {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Retorning group list")
        return view_group_list(groups), 200


@ app.delete('/groups', tags=[group_tag],
             responses={"200": GroupDeleteSchema, "404": ErrorSchema})
def del_produto(query: GroupSearchSchema):
    """Deletes a group with id.

    Returns a confirmation message.
    """
    group_id = query.id

    logger.debug(f"Deleting group #{group_id}")
    session = Session()

    if group_id:
        count = session.query(Group).filter(Group.id == group_id).delete()

    session.commit()
    if count:
        logger.debug(f"Deleting group #{group_id}")
        return {"message": "Group removed!", "id": group_id}
    else:
        error_msg = "Groups not found in the database :/"
        logger.warning(f"Error deleting group #'{group_id}', {error_msg}")
        return {"message": error_msg}, 400
