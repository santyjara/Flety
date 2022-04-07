from typing import Optional

from pydantic import BaseModel, constr, validator


class Address(BaseModel):
    id: Optional[int]
    address_line_1: constr(max_length=100)
    city: constr(max_length=30)
    zipcode: Optional[str]
    country: constr(max_length=30)
    lat: float
    long: float
    user_id: Optional[int]

    @validator("zipcode")
    def zipcode_length(cls, v):
        if len(str(v)) != 6:
            raise ValueError("Pincode must be of six digits")
        return v
