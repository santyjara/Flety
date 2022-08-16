from core.crud.base import CRUDBase


class CRUDCommon(CRUDBase):
    async def fetch_vehicle_types(self):
        obj_out = await self.database.fetch_vehicle_types()

        return obj_out

    async def fetch_load_types(self):
        obj_out = await self.database.fetch_load_types()

        return obj_out

    async def fetch_trailer_types(self):
        obj_out = await self.database.fetch_trailer_types()

        return obj_out

    async def fetch_user_roles(self):
        obj_out = await self.database.fetch_user_roles()

        return obj_out


common = CRUDCommon(None)
