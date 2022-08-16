from datetime import datetime
from typing import Optional

from pydantic import BaseModel, constr, validator

from core.entities.base import BaseCheckModel


class AddressBase(BaseCheckModel):
    user_id: int
    address_line_1: constr(max_length=100)
    city: constr(max_length=30)
    zipcode: Optional[str]
    country: constr(max_length=30)
    lat: float
    long: float


class Address(AddressBase):
    id: Optional[int]
    created_at: datetime

    @validator("zipcode")
    def zipcode_length(cls, v):
        if len(str(v)) != 6:
            raise ValueError("Pincode must be of six digits")
        return v
