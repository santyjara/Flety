from datetime import datetime

from core.crud.base import CRUDBase
from core.entities import Load
from core.schemas.load import LoadCreate, LoadUpdate


class CRUDLoad(CRUDBase[Load, LoadCreate, LoadUpdate]):
    async def create(self, obj_in: LoadCreate) -> Load:
        print(self.model)
        db_obj = self.model(
            **(obj_in.dict()),
            created_at=datetime.utcnow(),
        )
        obj_out = await self.database.create_load(db_obj)

        return obj_out


load = CRUDLoad(Load)
