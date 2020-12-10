from db.user_db import UserInDB
from db.user_db import update_user, get_user

from db.transaction_db import TransactionInDB
from db. transaction_db import save_transaction

from models.user_models import UserIn, UserOut

from models.transaction_models import TransactiionIn, TransactionOut

# importa paquetes.

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

# esto implementa la operacion auth_user.
# el post crea ver diapositivas con el simil del crud clase 9. consulta.
# no se utiliza un get pues cualquier persona lo veria y seria una falla de seguridad
# se utiliza un post para que los parametros esten ocultos.

@api.post("/user/auth/")

async def auth_user(Userin: UserIn):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail='El usuario no existe')

    if user_in_db.password != user_in.password:

        return {"Autentificado": False}

    return {"Autenticado": True}

# Implementando operacion get_balance (consulta)

@api.get("/user/blance/{username}")

async def get_balance(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException( status_code = 404, 
                            detail='El usuario no existe')

    user_out = UserOut(**user_in_db.dict())
    return user_out


# implementa la operacion make_transaction.
# hace la transaccion, es decir es posible que modifique el estado de la cuenta
# es una actualizacion.

@api.put("/user/transaction")

async def make_transaction(transaction_in: TransactiionIn):

    user_in_db = get_user(transaction_in.username)

    if user_in_db == None:
        raise HTTPException(status_code = 404, 
                            detail='El usuario no existe')

    if user_in_db.balance < transaction_in.value:
        raise HTTPException(status_code = 400,
                            detail= "Sin fondos suficientes")

    user_in_db.balance = user_in_db.balance - transaction_in.value
    update_user(user_in_db)

    transaction_in_db = TransactionInDB(**transaction_in.dict(),
                             actual_balance = user_in_db.balance)

    transaction_in_db = save_transaction(transaction_in_db)

    transaction_out =TransactionOut(**transaction_in_db.dict())

    return transaction_out
