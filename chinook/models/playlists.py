"""
playlists.py

Defines the Playlists SQLAlchemy ORM model for the `playlists` table.

Each record represents a named collection of tracks, allowing users to group
their favorite songs together under one playlist.
"""

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String
from kink import di

BASE = di[DeclarativeBase]


class Playlists(BASE):
    """
    Represents a playlist in the database.

    This table stores user-defined or pre-defined playlists, each with a unique ID and a name.

    Attributes
    ----------
    playlist_id : Mapped[int]
        Unique identifier for the playlist. Primary key with auto-increment.

    name : Mapped[str]
        Name of the playlist (e.g., 'Workout Mix', 'Favorites'). Max length: 120 characters.
    """

    __tablename__ = "playlists"

    playlist_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(120))
