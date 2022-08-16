from environs import Env
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

env = Env()
env.read_env()

url = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    env("DB_USER"),
    env("DB_PASS"),
    env("DB_HOST"),
    env.int("DB_PORT"),
    env("DB_NAME"),
)

engine = create_async_engine(url)

# `expire_on_commit=False` will prevent attributes from being expired after commit
session_factory = sessionmaker(
    engine, autocommit=False, expire_on_commit=False, class_=AsyncSession
)
