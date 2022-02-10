from abc import ABC, abstractmethod

from utils.patterns import Singleton


class NOSQLDatabase(ABC, Singleton):
    @abstractmethod
    def update_coordinates(self, _id: int, latitude: str, longitude: str):
        """Update vehicle coordinates

        Parameters
        ----------
        _id : str
        latitude :
        longitude

        Returns
        -------

        """
        pass
