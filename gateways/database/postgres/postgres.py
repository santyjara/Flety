from typing import Any, Dict

from gateways.database.base_sql import SQLDatabase
from gateways.database.postgres.postgres_config import session_factory


class PostgresDatabase(SQLDatabase):
    def __init__(self):
        super().__init__()
        self.session_factory = session_factory

    async def create_load(self, load: Dict[str, Any]) -> str:
        async with self.session_factory() as db:
            pass

    def read_load(self, _id: str) -> Dict[str, Any]:
        pass

    def update_load(self, load: Dict[str, Any]) -> str:
        pass

    def delete_load(self, _id: str) -> str:
        pass
