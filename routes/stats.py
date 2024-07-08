from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint

from datetime import datetime
from logger import logger
import pandas as pd

from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError

from schemas import ExpenseStatsViewSchema, ExpenseStatsTimeseriesViewSchema, ErrorSchema
from models import Session, Expense

stats_tag = Tag(
    name="Stats", description="Retrieve statistics from expenses.")
stats_api = APIBlueprint('/stats', __name__, url_prefix='', abp_tags=[stats_tag])

# ==============================|| Expense Endpoints ||============================== #

@stats_api.get('/expense_stats', tags=[stats_tag],
         responses={"200": ExpenseStatsViewSchema, "404": ErrorSchema})
def get_expense_stats():
    """Get expense stats such as total transactions and total value.

    Retorns stats.
    """
    logger.debug(f"Getting expense stats")
    session = Session()
    total_transactions = session.query(Expense).count()
    resp = session.query(func.sum(Expense.value_usd), func.sum(Expense.value_brl)).all()
    total_value_usd = resp[0][0]
    total_value_brl = resp[0][1]
    if not total_transactions or not total_value_usd:
        error_msg = "Error calculating stats :/"
        logger.warning(f"{error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(
            f"Getting expense stats {total_transactions} and {total_value_usd}")
        return {
            "total_transactions": str(total_transactions),
            "total_transactions_perc": str(15.5),
            "total_value_usd": str(total_value_usd),
            "total_value_usd_perc": str(-10.5),
            "total_value_brl": str(total_value_brl),
            "total_value_brl_perc": str(-10.5),
            }, 200


@stats_api.get('/expense_stats_timeseries', tags=[stats_tag],
         responses={"200": ExpenseStatsTimeseriesViewSchema, "404": ErrorSchema})
def get_expense_stats_timeseries():
    """Get expense monthly stats.

    Retorns stats.
    """
    logger.debug(f"Getting expense timeseries stats")

    number_of_months = 11
    try:
        session = Session()
        # Query Transactions
        transactions_month = session.query(
                func.to_char(Expense.created_at, "YYYY-MM-01"), 
                func.count(Expense.id)
            ).group_by(func.to_char(Expense.created_at, "YYYY-MM-01")
            ).order_by(func.to_char(Expense.created_at, "YYYY-MM-01").desc()).limit(number_of_months).all()
        logger.debug(f"transactions_month: {transactions_month}")
        transaction_data, transaction_categories = create_api_response(
            transactions_month, number_of_months)
        
        # Query Value Spent
        value_spent_usd_month = session.query(
                func.to_char(Expense.created_at, "YYYY-MM-01"),
                func.sum(Expense.value_usd)
            ).group_by(
                func.to_char(Expense.created_at, "YYYY-MM-01")
            ).order_by(func.to_char(Expense.created_at, "YYYY-MM-01").desc()
            ).limit(number_of_months).all()
        logger.debug(f"value_spent_usd_month: {value_spent_usd_month}")
        value_spent_usd_data, value_spent_categories = create_api_response(
            value_spent_usd_month, number_of_months)
        
        # Query Value Spent BRL
        value_spent_brl_month = session.query(
                func.to_char(Expense.created_at, "YYYY-MM-01"), 
                func.sum(Expense.value_brl)
            ).group_by(func.to_char(
                Expense.created_at, "YYYY-MM-01")
            ).order_by(func.to_char(Expense.created_at, "YYYY-MM-01").desc()).limit(number_of_months).all()
        logger.debug(f"value_spent_month: {value_spent_brl_month}")
        value_spent_brl_data, value_spent_categories = create_api_response(
            value_spent_brl_month, number_of_months)

        return {
            "transactions": {
                "data": transaction_data,
                "categories": transaction_categories,
            },
            "value_usd": {
                "data": value_spent_usd_data,
                "categories": value_spent_categories,
            },
            "value_brl": {
                "data": value_spent_brl_data,
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