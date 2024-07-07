from pydantic import BaseModel
from typing import Optional, List, Dict, Union


class ExpenseStatsViewSchema(BaseModel):
    """ Define how new expense stats will be represented
    """
    total_transactions: int = 0
    total_transactions_perc: float = 0.0
    total_value_usd: float = 0.0
    total_value_usd_perc: float = 0.0
    total_value_brl: float = 0.0
    total_value_brl_perc: float = 0.0

class ExpenseStatsTimeseriesViewSchema(BaseModel):
    """ Define how new expense stats timeseries will be represented
    """
    transactions: Dict[str, Union[int, str]]
    value: Dict[str, Union[float, str]]