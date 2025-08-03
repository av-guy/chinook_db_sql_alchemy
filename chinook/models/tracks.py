"""
tracks.py

Defines the Tracks SQLAlchemy ORM model for the `tracks` table.

This table stores individual audio track records in the Chinook database, including
metadata such as name, album, media type, genre, duration, size, and price.

Classes
-------
Tracks
    ORM model for the `tracks` table, including track-level metadata such as name,
    album ID, media type, genre, composer, duration, file size, and price.
"""

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, ForeignKey

from kink import di

BASE = di[DeclarativeBase]


class Tracks(BASE):
    """
    Represents an individual audio track in the database.

    This table contains metadata for audio tracks such as the track name, album ID,
    media type, genre, composer, duration, size, and price. Foreign keys are used 
    to associate tracks with media types and genres, but album_id is not enforced 
    as a foreign key.

    Attributes
    ----------
    track_id : Mapped[int]
        Unique identifier for the track. Primary key with auto-increment.

    name : Mapped[str]
        Name or title of the track. Max length: 200 characters.

    album_id : Mapped[int]
        Identifier for the album to which the track belongs. Not a foreign key.

    media_type_id : Mapped[int]
        Foreign key referencing `media_types.media_type_id`.

    genre_id : Mapped[int]
        Foreign key referencing `genres.genre_id`.

    composer : Mapped[str]
        Name of the composer or creator of the track. Max length: 220 characters.

    milliseconds : Mapped[int]
        Length of the track in milliseconds.

    total_bytes : Mapped[int]
        File size of the track in bytes.

    unit_price : Mapped[float]
        Price of the track in USD.
    """
    __tablename__ = "tracks"

    track_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200))
    album_id: Mapped[int] = mapped_column(
        ForeignKey("albums.album_id"), index=True)

    media_type_id: Mapped[int] = mapped_column(
        ForeignKey("media_types.media_type_id"), index=True)

    genre_id: Mapped[int] = mapped_column(
        ForeignKey("genres.genre_id"), index=True)
    composer: Mapped[str] = mapped_column(String(220), nullable=True)

    milliseconds: Mapped[int] = mapped_column()
    total_bytes: Mapped[int] = mapped_column()
    unit_price: Mapped[float] = mapped_column()

    def __repr__(self) -> str:
        return (
            f"<Tracks(track_id={self.track_id}, name='{self.name}', "
            f"album_id={self.album_id}, media_type_id={self.media_type_id}, "
            f"genre_id={self.genre_id}, unit_price={self.unit_price})>"
        )
