
from typing import Dict
from pydantic import BaseModel

# lo que esta entre parentesis es para decir que estiende de otra clase. userInDB extiende de BaseModel
class UserInDB(BaseModel):  
    # esto define los atributos y el tipo de cada atributo.
    username: str
    password: str
    balance: int


# esto es para la base de datos fictisia para hacer el ejemplo.


# dict dice que entra un tipo string y a ese tipo se le asiga un tipo userInDB.
# acontinuacion lo que se hace es instanciar.
database_users=Dict[str,UserInDB]

database_users={
    "camilo24":UserInDB(**{ "username":"camilo24",
                            "password":"root",
                            "balance":12000}),
    "andres18":UserInDB(**{ "username":"andres18",
                            "password":"hola",
                            "balance":34000}), 
}
# los dos asteriscos hace un mapeo dice que es el tipo userInDB (como si fuera el constructor)

# esto da las funciones sobre la base de datos.
# esta funciones optiene un usuario y actualiza un usuario.
# la primera funcion retorna todos los datos de ese usuario. (get)
# la segunda funcion actualiza. (set)

def get_user(username: str):

    #recordar la funcion keys que trae todas las llaves del diccionario. es decir dentor del diccionario esta buscando
    # el valor
    if username in database_users.keys():  
        
        return database_users[username]

    else:
        return None

def update_user(user_in_db: UserInDB):

    database_users[user_in_db.username] = user_in_db
    return user_in_db




