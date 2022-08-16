from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserRol(str, Enum):
    """
    Class to define the different roles a user can have.
    """

    admin = "admin"
    conductor = "conductor"
    generador = ("generador",)
    propietario = ("propietario",)
    empresa_de_transporte = "empresa de transporte"


class User(BaseModel):
    email: Optional[EmailStr]
    is_active: Optional[bool]
    rol: Optional[UserRol]
    is_superuser: bool
    name: Optional[str]
    last_name: Optional[str]
