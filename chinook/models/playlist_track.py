"""
playlist_track.py

Defines the PlaylistTrack SQLAlchemy ORM model for the `playlist_track` join table.

This is an association table representing the many-to-many relationship
between playlists and tracks.
"""

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import ForeignKey
from kink import di

BASE = di[DeclarativeBase]


class PlaylistTrack(BASE):
    """
    Represents an association between a playlist and a track.

    This join table connects playlists and tracks in a many-to-many relationship.

    Attributes
    ----------
    playlist_id : Mapped[int]
        Foreign key referencing the `playlists` table.

    track_id : Mapped[int]
        Foreign key referencing the `tracks` table.
    """

    __tablename__ = "playlist_track"

    playlist_id: Mapped[int] = mapped_column(
        ForeignKey("playlists.playlist_id"), primary_key=True)

    track_id: Mapped[int] = mapped_column(
        ForeignKey("tracks.track_id"), primary_key=True, index=True)
