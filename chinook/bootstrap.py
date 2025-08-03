# pylint: disable=all

""" Kink bootstrapping module """

from os import getenv
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import Engine

from kink import di

from .protocols.sql_alchemy_config import ISQLAlchemyConfig


class Base(DeclarativeBase):
    """ DeclarativeBase for the application """


di[DeclarativeBase] = Base


def initialize():
    """ Bootstrap the application for setup """
    from .models import init_db as init_db
    from .commit_samples import commit_sample_data

    use_sqlite = getenv("CHINOOK_SQLITE", "1")
    db_name = getenv("CHINOOK_SQLITE_DB_NAME", "chinook")
    in_memory = getenv("CHINOOK_SQLITE_IN_MEMORY", "1")

    try:
        use_sqlite = int(use_sqlite)
    except ValueError:
        raise ValueError("CHINOOK_SQLITE expects a value of 0 or 1.")

    try:
        in_memory = int(in_memory)
    except ValueError:
        raise ValueError("CHINOOK_SQLITE_IN_MEMORY expects a value of 0 or 1.")

    conn_string = getenv("CHINOOK_CONN_STRING", "")

    if use_sqlite:
        conn_string = f"sqlite:///db/{db_name}.db" if not in_memory else "sqlite:///:memory:"

    SQLAlchemyConfig = type(
        "SQLAlchemyConfig",
        (),
        {
            "connection_string": property(lambda self: conn_string)
        }
    )

    di[ISQLAlchemyConfig] = SQLAlchemyConfig()

    engine = init_db()
    commit_sample_data(engine)

    di[Engine] = engine
