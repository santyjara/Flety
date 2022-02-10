from abc import ABC

from utils.patterns import Singleton


class DatabaseGateway(ABC, Singleton):
    db_gateway = {}

    def __init_subclass__(cls) -> None:
        return cls.db_gateway.update({cls.name: cls})
