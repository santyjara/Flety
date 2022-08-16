from abc import ABC

from gateways.database.base_nosql import NOSQLDatabase
from gateways.database.base_sql import SQLDatabase
from utils.patterns import Singleton


class DatabaseGateway(Singleton, SQLDatabase, NOSQLDatabase, ABC):
    db_gateway = {}

    def __init_subclass__(cls) -> None:
        return cls.db_gateway.update({cls.name: cls})
