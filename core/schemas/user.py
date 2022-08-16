from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, EmailStr

from core.entities import UserRol


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    rol: Optional[UserRol]
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str
    rol: UserRol


class UserRolesResponse(BaseModel):
    __root__: List[UserRol]
