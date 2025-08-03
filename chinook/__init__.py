import os

from kink import di
from sqlalchemy import Engine
from .bootstrap import initialize


def get_engine() -> Engine:
    """
    Retrieve the SQLAlchemy Engine instance.

    This engine is configured to connect to the Chinook database and is 
    registered with the dependency injection container.

    Returns
    -------
    Engine
        The SQLAlchemy Engine connected to the Chinook database.
    """
    return di[Engine]


def remove_sqlite_database(db_name: str):
    """
    Dispose of the active SQLAlchemy engine and delete the specified SQLite database file.

    Parameters
    ----------
    db_name : str
        Name of the SQLite database file (without the `.db` extension) located in the `db`
        directory.
    """
    engine = get_engine()
    engine.dispose()

    if os.path.exists(f"db\\{db_name}.db"):
        os.remove(f"db\\{db_name}.db")
