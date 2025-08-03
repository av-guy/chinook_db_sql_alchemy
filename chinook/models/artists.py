"""
artists.py

Defines the Artists SQLAlchemy ORM model for the `artists` table.

This table stores artist information in the Chinook database. An artist may be linked
to one or more albums, typically representing a band or solo musician.

Classes
-------
Artists
    ORM model for the `artists` table, representing music artists or bands.
"""

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String

from kink import di

BASE = di[DeclarativeBase]


class Artists(BASE):
    """
    Represents a music artist in the database.

    An artist may have multiple albums and is typically the performer or creator
    of those albums.

    Attributes
    ----------
    artist_id : Mapped[int]
        Unique identifier for the artist. Primary key with auto-increment.

    name : Mapped[str]
        Name of the artist or band. Max length: 120 characters.
    """

    __tablename__ = "artists"

    artist_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(120))

    def __repr__(self) -> str:
        return f"<Artists(artist_id={self.artist_id}, name='{self.name}')>"
