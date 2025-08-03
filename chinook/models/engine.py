"""
engine.py

Defines a factory function for creating a SQLAlchemy Engine using a provided configuration.

The function is dependency-injected via `kink`, using an implementation of
`ISQLAlchemyConfig` that supplies the database connection string.

Functions
---------
create_db_engine(sql_config: ISQLAlchemyConfig) -> Engine
    Creates and returns a SQLAlchemy Engine using the provided connection string.
"""
from typing import Optional

from kink import inject
from sqlalchemy import create_engine, Engine

from ..protocols.sql_alchemy_config import ISQLAlchemyConfig


@inject()
def create_db_engine(sql_config: Optional[ISQLAlchemyConfig] = None) -> Engine:
    """
    Creates a SQLAlchemy Engine using the provided configuration.

    Parameters
    ----------
    sql_config : ISQLAlchemyConfig
        An object implementing the `ISQLAlchemyConfig` protocol, providing
        a database connection string.

    Returns
    -------
    Engine
        A SQLAlchemy Engine object configured to connect to the specified database.

    Raises
    ------
    ValueError
        If the `sql_config` is not provided via depdendency injection.

    Note
    ----
    If an error is raised from this method, this is likely an issue with the package.
    """
    if sql_config is None:
        raise ValueError("`sql_config` must be provided.")

    return create_engine(sql_config.connection_string)
