# pylint: disable=all

""" Kink bootstrapping module """

from os import getenv
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import Engine

from kink import di
from .protocols.sql_alchemy_config import ISQLAlchemyConfig


class Base(DeclarativeBase):
    """ DeclarativeBase for the application """


di[DeclarativeBase] = Base


SQLAlchemyConfig = type(
    "SQLAlchemyConfig",
    (),
    {
        "connection_string": property(
            lambda self: getenv(
                "CHINOOK_CONN_STRING") or "sqlite:///chinook.db"
        )
    }
)

di[ISQLAlchemyConfig] = SQLAlchemyConfig()


def initialize():
    """ Bootstrap the application for setup """
    from .models import init_db as init_db

    from .sample_data import (
        load_album_data,
        load_media_type_data,
        load_genre_data,
        load_playlist_data,
        load_artist_data,
        load_employees_data,
        load_customer_data,
        load_invoice_data,
        load_track_data,
        load_playlist_track_data,
        load_invoice_item_data
    )

    init_db()

    from .models import (
        MediaTypes,
        Genres,
        Playlists,
        Artists,
        Employees,
        Customers,
        Invoices,
        Albums,
        Tracks,
        PlaylistTrack,
        InvoiceItems
    )

    media_types = load_media_type_data()
    genres = load_genre_data()
    playlists = load_playlist_data()
    artists = load_artist_data()
    employees = load_employees_data()
    customers = load_customer_data()
    invoices = load_invoice_data()
    albums = load_album_data()
    tracks = load_track_data()
    playlist_tracks = load_playlist_track_data()
    invoice_items = load_invoice_item_data()

    engine: Engine = di[Engine]

    with Session(engine) as session:
        for _, row in media_types.iterrows():
            session.add(MediaTypes(
                media_type_id=row["media_type_id"],
                name=row["name"]
            ))

        for _, row in genres.iterrows():
            session.add(Genres(
                genre_id=row["genre_id"],
                name=row["name"]
            ))

        for _, row in playlists.iterrows():
            session.add(Playlists(
                playlist_id=row["playlist_id"],
                name=row["name"]
            ))

        for _, row in artists.iterrows():
            session.add(Artists(
                artist_id=row["artist_id"],
                name=row["name"]
            ))

        for _, row in employees.iterrows():
            session.add(Employees(
                employee_id=row["employee_id"],
                last_name=row["last_name"],
                first_name=row["first_name"],
                title=row["title"],
                reports_to=row["reports_to"],
                birth_date=row["birth_date"],
                hire_date=row["hire_date"],
                address=row["address"],
                city=row["city"],
                state=row["state"],
                country=row["country"],
                postal_code=row["postal_code"],
                phone=row["phone"],
                fax=row["fax"],
                email=row["email"]
            ))

        for _, row in customers.iterrows():
            session.add(Customers(
                customer_id=row["customer_id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                company=row["company"],
                address=row["address"],
                city=row["city"],
                state=row["state"],
                country=row["country"],
                postal_code=row["postal_code"],
                phone=row["phone"],
                fax=row["fax"],
                email=row["email"],
                support_rep_id=row["support_rep_id"]
            ))

        for _, row in invoices.iterrows():
            session.add(Invoices(
                invoice_id=row["invoice_id"],
                customer_id=row["customer_id"],
                invoice_date=row["invoice_date"],
                billing_address=row["billing_address"],
                billing_city=row["billing_city"],
                billing_state=row["billing_state"],
                billing_country=row["billing_country"],
                billing_postal_code=row["billing_postal_code"],
                total=row["total"]
            ))

        for _, row in albums.iterrows():
            session.add(Albums(
                album_id=row["album_id"],
                title=row["title"],
                artist_id=row["artist_id"]
            ))

        for _, row in tracks.iterrows():
            session.add(Tracks(
                track_id=row["track_id"],
                name=row["name"],
                album_id=row["album_id"],
                media_type_id=row["media_type_id"],
                genre_id=row["genre_id"],
                composer=row["composer"],
                milliseconds=row["milliseconds"],
                total_bytes=row["total_bytes"],
                unit_price=row["unit_price"]
            ))

        for _, row in playlist_tracks.iterrows():
            session.add(PlaylistTrack(
                playlist_id=row["playlist_id"],
                track_id=row["track_id"]
            ))

        for _, row in invoice_items.iterrows():
            session.add(InvoiceItems(
                invoice_line_id=row["invoice_line_id"],
                invoice_id=row["invoice_id"],
                track_id=row["track_id"],
                unit_price=row["unit_price"],
                quantity=row["quantity"]
            ))

        session.commit()
