from gateways.database.base_nosql import NOSQLDatabase


class DynamoDBDatabase(NOSQLDatabase):
    def __init__(self):
        pass

    def update_coordinates(self, _id: int, latitude: str, longitude: str):
        pass
