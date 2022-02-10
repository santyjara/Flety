from abc import ABC, abstractmethod

from gateways.database.factory import database_gateway_factory


class Entity(ABC):
    database = database_gateway_factory()

    @abstractmethod
    def create(self):
        pass

    @classmethod
    @abstractmethod
    def read(cls, id_: int):
        pass

    @abstractmethod
    def update(self):
        pass

    @classmethod
    @abstractmethod
    def delete(cls, id_: int):
        pass
