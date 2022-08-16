from datetime import datetime
from typing import Optional

from core.entities.address import AddressBase


class AddressCreate(AddressBase):
    user_id: Optional[int]
    created_at: Optional[datetime]


class AddressInDataBase(AddressBase):
    ...
