from datetime import datetime

from core.crud.base import CRUDBase
from core.entities import Address
from core.schemas.address import AddressCreate


class CRUDLoad(CRUDBase[Address, AddressCreate, None]):
    async def create(self, obj_in: AddressCreate) -> int:

        obj_in.created_at = datetime.utcnow()
        obj_in.check()

        obj_out = await self.database.create_address(obj_in)

        return obj_out


address = CRUDLoad(Address)
