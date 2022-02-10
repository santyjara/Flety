from gateways.database.base import DatabaseGateway
from gateways.database.dynamodb import DynamoDBDatabase
from gateways.database.postgres import PostgresDatabase


class PostgresDynamoDBDatabaseGateway(
    DatabaseGateway, PostgresDatabase, DynamoDBDatabase
):
    name = "postgres_dynamodb"

    def __init__(self):
        super().__init__()
