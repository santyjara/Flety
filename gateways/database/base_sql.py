from abc import ABC, abstractmethod
from typing import Any, Dict

from core.entities import Load
from core.schemas.address import AddressCreate


class SQLDatabase(ABC):
    # _____ CRUD Load
    @abstractmethod
    def create_load(self, load: Load) -> int:
        """
        Parameters
        ----------
        load: Load
            Load entity

        Returns
        -------
        int
            Order id
        """

    @abstractmethod
    def read_load(self, _id: str) -> Dict[str, Any]:
        """
        Parameters
        ----------
        _id: str
            Order id

        Returns
        -------
        Dict[str, Any]
            Order body
        """

    @abstractmethod
    def update_load(self, load: Load) -> int:
        """
        Parameters
        ----------
        load: Dict[str, Any]
            Order body

        Returns
        -------
        int
            Updated load id
        """

    @abstractmethod
    def delete_load(self, _id: str) -> int:
        """
        Parameters
        ----------
        _id: str
            Order id

        Returns
        -------
        int
            Deleted load id
        """

    # _____ CRUD Address
    @abstractmethod
    def create_address(self, address: AddressCreate) -> int:
        ...

    @abstractmethod
    def read_address(self, _id: str) -> Dict[str, Any]:
        ...

    @abstractmethod
    def update_address(self, address: Dict[str, Any]) -> str:
        ...

    @abstractmethod
    def delete_address(self, _id: str) -> str:
        ...

    # _____ CRUD Common
    @abstractmethod
    def fetch_vehicle_types(self):
        ...

    @abstractmethod
    def fetch_load_types(self):
        ...

    @abstractmethod
    def fetch_trailer_types(self):
        ...

    @abstractmethod
    def fetch_user_roles(self):
        ...
