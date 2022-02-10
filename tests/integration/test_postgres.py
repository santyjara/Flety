from gateways.database.factory import database_gateway_factory


def test_database_gateway_is_singleton():
    gateway_1 = database_gateway_factory()
    gateway_2 = database_gateway_factory()
    assert gateway_1 == gateway_2
