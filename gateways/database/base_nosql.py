from abc import ABC, abstractmethod


class NOSQLDatabase(ABC):
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
