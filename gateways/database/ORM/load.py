from datetime import datetime
from typing import Optional


class Load:
    """Class that defines a single freight. Each freight represents Any shipment
    over 150 lbs. Freight shipping is the transportation of goods, commodities
    and cargo in bulk by ship, aircraft, truck or intermodal via train and road.

    id: unique id of the Load

    """

    id: Optional[int]
    pick_up_date: datetime
    origin_city: str
    origin_department: str
    origin_address_id: Optional[int]
    destiny_city: str
    destiny_department: str
    destiny_address_id: Optional[int]
    weight: int
    length: float
    extra_info: str
    contact_name: str
    contact_phone: str
    contact_email: str
