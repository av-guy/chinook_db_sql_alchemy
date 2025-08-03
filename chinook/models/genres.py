"""
genres.py

Defines the Genres SQLAlchemy ORM model for the `genres` table.

This table contains the different music genres associated with tracks in the Chinook
database, such as Rock, Jazz, Classical, etc.

Classes
-------
Genres
    ORM model for the `genres` table, representing distinct musical categories.
"""

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String

from kink import di

BASE = di[DeclarativeBase]


class Genres(BASE):
    """
    Represents a music genre in the database.

    Each genre defines a category of music used to classify tracks, such as Rock or Jazz.

    Attributes
    ----------
    genre_id : Mapped[int]
        Unique identifier for the genre. Primary key with auto-increment.

    name : Mapped[str]
        Name of the music genre. Max length: 120 characters.
    """

    __tablename__ = "genres"

    genre_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120))
