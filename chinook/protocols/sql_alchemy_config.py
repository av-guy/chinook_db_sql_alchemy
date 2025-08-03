"""
sql_alchemy_config.py

Defines the ISQLAlchemyConfig protocol used to provide SQLAlchemy connection configuration.

This protocol ensures that any implementing class provides a `connection_string` property,
which is required to initialize a SQLAlchemy engine for database access.

Classes
-------
ISQLAlchemyConfig
    Protocol interface that defines the required connection string for SQLAlchemy.
"""

from typing import Protocol


class ISQLAlchemyConfig(Protocol):
    """
    Interface for SQLAlchemy configuration.

    Any class implementing this protocol must provide a `connection_string` property
    that returns the database connection string used to initialize the SQLAlchemy engine.

    Attributes
    ----------
    connection_string : str
        The database connection string used by SQLAlchemy to connect to the database.
    """

    @property
    def connection_string(self) -> str:
        """Returns the connection string to use for the application."""

    @property
    def in_memory(self) -> bool:
        """Returns whether this should be stored in-memory or on disk.

        Notes
        -----
        This only applies to when SQLite is used.
        """
