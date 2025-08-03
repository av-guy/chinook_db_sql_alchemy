"""
albums.py

Defines the Albums SQLAlchemy ORM model for the `albums` table.

This table stores album-level metadata in the Chinook database. Each album may
contain multiple tracks and is optionally linked to an artist.

Classes
-------
Albums
    ORM model for the `albums` table, representing music albums and their associated artists.
"""

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, ForeignKey

from kink import di

BASE = di[DeclarativeBase]


class Albums(BASE):
    """
    Represents a music album in the database.

    Albums are collections of tracks that may be associated with a specific artist.

    Attributes
    ----------
    album_id : Mapped[int]
        Unique identifier for the album. Primary key with auto-increment.

    title : Mapped[str]
        Title of the album. Max length: 160 characters.

    artist_id : Mapped[int]
        Foreign key referencing `artists.artist_id`.
    """

    __tablename__ = "albums"

    album_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(160))

    artist_id: Mapped[int] = mapped_column(
        ForeignKey("artists.artist_id"), index=True)

    def __repr__(self) -> str:
        return f"<Albums(album_id={self.album_id}, title='{self.title}', artist_id={self.artist_id})>"
