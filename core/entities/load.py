from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .address import Address


class Load(BaseModel):
    pick_up_date: Optional[datetime]
    origin_city: str
    origin_department: str
    origin_address: Address
    destiny_address: Address
    weight: float
    length: float
    extra_info: str
    contact_name: str
    contact_phone: str
    contact_email: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
