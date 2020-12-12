

from pydantic import BaseModel
from datetime import datetime

# se crea las clase

class TransactionIn(BaseModel):

    username: str
    value: int


class TransactionOut(BaseModel):

    id_transactiion: int
    username: str
    date: datetime
    value: int
    actual_balance: int
