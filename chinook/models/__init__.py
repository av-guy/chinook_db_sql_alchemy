""" Module used to initialize all available models and create the database """

from kink import di
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import inspect

from .engine import create_db_engine, Engine
from .albums import Albums
from .artists import Artists
from .customers import Customers
from .employees import Employees
from .genres import Genres
from .invoice_items import InvoiceItems
from .invoices import Invoices
from .media_types import MediaTypes
from .tracks import Tracks
from .playlists import Playlists
from .playlist_track import PlaylistTrack


def init_db():
    """ Initialize the SQLAlchemy engine and create the database """
    base = di[DeclarativeBase]

    engine = create_db_engine()
    di[Engine] = engine

    base.metadata.create_all(engine)
