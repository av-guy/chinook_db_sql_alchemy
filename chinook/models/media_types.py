"""
media_types.py

Defines the MediaTypes SQLAlchemy ORM model for the `media_types` table.

This table stores the various types of media formats associated with audio tracks
in the Chinook database, such as MPEG audio, AAC audio files, etc.

Classes
-------
MediaTypes
    ORM model for the `media_types` table, including ID and name of each media type.
"""

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String

from kink import di

BASE = di[DeclarativeBase]


class MediaTypes(BASE):
    """
    Represents a media type entity in the database.

    This table stores types of media formats used by tracks, such as MPEG audio, AAC, etc.
    Each record corresponds to a single media type.

    Attributes
    ----------
    media_type_id : Mapped[int]
        Unique identifier for the media type. Primary key with auto-increment.

    name : Mapped[str]
        Descriptive name of the media type (e.g., 'MPEG audio file'). Max length: 120 characters.
    """

    __tablename__ = "media_types"

    media_type_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(120))
