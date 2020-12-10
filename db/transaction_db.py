
from datetime import datetime 
from pydantic import BaseModel 


# esta creando las clases con sus tributos con su respectivo tipo de dato.

class TransactionInDB(BaseModel):
    id_transaction:int=0
    username:str
    date:datetime=datetime.now()
    value: int
    intactual_balance:int



database_transactions= []
generator = {"id":0}

def save_transaction(transaction_in_db: TransactionInDB):
    generator["id"] = generator ["id"] + 1
    transaction_in_db = generator["id"]
    database_transactions.append(transaction_in_db)
    return transaction_in_db