from typing import Any, Dict

from sqlalchemy.future import select

from core.entities import Address, Load
from core.schemas.address import AddressCreate
from gateways.database.base_sql import SQLDatabase
from gateways.database.ORM import AddressORM, LoadORM, VehicleTypeORM
from gateways.database.postgres.postgres_config import session_factory


class PostgresDatabase(SQLDatabase):
    def __init__(self):
        super().__init__()
        self.session_factory = session_factory

    # _____ CRUD Load
    async def create_load(self, load: Load) -> int:
        async with self.session_factory() as db:
            load_orm = LoadORM(**load.dict())
            db.add(load_orm)
            await db.commit()
            print(load_orm)

        return load_orm.id

    def read_load(self, _id: str) -> Dict[str, Any]:
        pass

    def update_load(self, load: Dict[str, Any]) -> str:
        pass

    def delete_load(self, _id: str) -> str:
        pass

    # _____ CRUD Address
    async def create_address(self, address: AddressCreate) -> int:
        async with self.session_factory() as db:
            address_orm = AddressORM(**address.dict())
            db.add(address_orm)
            await db.commit()

        return address_orm.id

    def read_address(self, _id: str) -> Dict[str, Any]:
        ...

    def update_address(self, address: Dict[str, Any]) -> str:
        ...

    def delete_address(self, _id: str) -> str:
        ...

    # _____ CRUD Common
    async def fetch_vehicle_types(self):
        async with self.session_factory() as db:
            statement = select(VehicleTypeORM)
            result = await db.execute(statement)
            data = result.scalars().all()

        vehicle_types = [inst.as_dict(only=["id", "name"]) for inst in data]

        return vehicle_types

    async def fetch_load_types(self):
        async with self.session_factory() as db:
            statement = "SELECT enum_range(NULL::load_type)"
            result = await db.execute(statement)
            load_types = result.scalar_one()

        return load_types

    async def fetch_trailer_types(self):
        async with self.session_factory() as db:
            statement = "SELECT enum_range(NULL::trailer_type)"
            result = await db.execute(statement)
            trailer_types = result.scalar_one()

        return trailer_types

    async def fetch_user_roles(self):
        async with self.session_factory() as db:
            statement = "SELECT enum_range(NULL::user_rol)"
            result = await db.execute(statement)
            user_roles = result.scalar_one()

        return user_roles
