from gateways.database.base import DatabaseGateway


def database_gateway_factory(database: str = "postgres_dynamodb") -> DatabaseGateway:
    try:
        return DatabaseGateway.db_gateway[database]()
    except NotImplementedError:
        raise NotImplementedError(f"{database} has been not implemented")
