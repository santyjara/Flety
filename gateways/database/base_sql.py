from abc import ABC, abstractmethod
from typing import Any, Dict

from core.entities import Load
from utils.patterns import Singleton


class SQLDatabase(ABC, Singleton):
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
        pass

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
        pass

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
        pass

    @abstractmethod
    def delete_load(self, _id: str) -> str:
        """
        Parameters
        ----------
        _id: str
            Order id

        Returns
        -------
        str
            Deleted load id
        """
        pass
