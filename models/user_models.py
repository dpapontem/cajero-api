

from pydantic import BaseModel

# crea la s clases con sus atributos.

class UserIn(BaseModel):

    username: str
    password: str


class UserOut(BaseModel):

    username: str
    balance: int




