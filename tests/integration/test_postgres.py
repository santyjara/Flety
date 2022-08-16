import pytest

from gateways.database import PostgresDynamoDBDatabaseGateway


@pytest.mark.asyncio
async def test_fetch_vehicle_types():
    database = PostgresDynamoDBDatabaseGateway()
    result = await database.fetch_vehicle_types()
    assert len(result) > 0
    # check the returned type is a dict, not a tuple
    assert all(map(lambda x: isinstance(x, dict), result))
    # check NPR is in response list
    assert "NPR" in [x["name"] for x in result]


@pytest.mark.asyncio
async def test_fetch_load_types():
    database = PostgresDynamoDBDatabaseGateway()
    result = await database.fetch_load_types()

    assert isinstance(result, list)
    assert len(result) > 0
    # check the returned type is a str list
    assert all(map(lambda x: isinstance(x, str), result))
    # check combustible is in response list
    assert "combustible" in result


@pytest.mark.asyncio
async def test_fetch_trailer_types():
    database = PostgresDynamoDBDatabaseGateway()
    result = await database.fetch_trailer_types()

    assert isinstance(result, list)
    assert len(result) > 0
    # Check the returned type is a list of strings:
    assert all(map(lambda x: isinstance(x, str), result))
    # Check `estacas` is in the response list:
    assert "estacas" in result


@pytest.mark.asyncio
async def test_fetch_user_roles():
    database = PostgresDynamoDBDatabaseGateway()
    result = await database.fetch_user_roles()

    assert isinstance(result, list)
    assert len(result) > 0
    # Check the returned type is a list of strings:
    assert all(map(lambda x: isinstance(x, str), result))
    # Check `conductor` is in the response list:
    assert "conductor" in result
