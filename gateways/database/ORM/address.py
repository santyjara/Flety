from typing import Optional

from pydantic import BaseModel, PositiveInt, constr, validator

from core import Entity


class Address(BaseModel, Entity):
    id: Optional[int]
    address_line_1: constr(max_length=50)
    city: constr(max_length=30)
    zipcode: Optional[PositiveInt] = None
    country: constr(max_length=30)
    lat: float
    long: float

    @validator("zipcode")
    def zipcode_length(cls, v):
        if len(str(v)) != 6:
            raise ValueError("Pincode must be of six digits")
        return v

    def create(self):
        pass

    @classmethod
    def read(cls, id_: int):
        pass

    def update(self):
        pass

    @classmethod
    def delete(cls, id_: int):
        pass
