from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, Field


class AddressRequestModel(BaseModel):
    address: str = Field(
        description="Corresponds to physical address validated with google and user approval"
    )
    int: str = Field(
        description="Corresponds to the number of any building inside (apartment, block, warehouse, gate)"
    )
    city: str
    country: str
    latitude: float
    longitude: float


class LoadRequestModel(BaseModel):
    pick_up_date: datetime
    origin_city: str
    origin_department: str
    origin_address: AddressRequestModel
    destiny_address: AddressRequestModel
    weight: float
    length: float
    extra_info: str
    contact_name: str
    contact_phone: str
    contact_email: str
