""" Module used to load sample CSV data """

from pathlib import Path
import pandas as pd


SAMPLES_DIR = Path(__file__).parent / "samples"


def load_album_data() -> pd.DataFrame:
    """
    Loads album data from a CSV file and standardizes column names.

    Returns
    -------
    pd.DataFrame
        DataFrame containing albums with columns: 'album_id', 'title', 'artist_id'.
    """
    albums = pd.read_csv(SAMPLES_DIR / "albums.csv")

    albums.rename(columns={
        "AlbumId": "album_id",
        "Title": "title",
        "ArtistId": "artist_id"
    }, inplace=True)

    return albums


def load_artist_data() -> pd.DataFrame:
    """
    Loads artist data from a CSV file and standardizes column names.

    Returns
    -------
    pd.DataFrame
        DataFrame containing artists with columns: 'artist_id', 'name'.
    """
    artists = pd.read_csv(SAMPLES_DIR / "artists.csv")

    artists.rename(columns={
        "ArtistId": "artist_id",
        "Name": "name"
    }, inplace=True)

    return artists


def load_customer_data() -> pd.DataFrame:
    """
    Loads customer data from a CSV file and standardizes column names.

    Returns
    -------
    pd.DataFrame
        DataFrame containing customers with columns:
        'customer_id', 'first_name', 'last_name', 'company', 'address',
        'city', 'state', 'country', 'postal_code', 'phone', 'fax', 'email', 'support_rep_id'.
    """
    customers = pd.read_csv(SAMPLES_DIR / "customers.csv")

    customers.rename(columns={
        "CustomerId": "customer_id",
        "FirstName": "first_name",
        "LastName": "last_name",
        "Company": "company",
        "Address": "address",
        "City": "city",
        "State": "state",
        "Country": "country",
        "PostalCode": "postal_code",
        "Phone": "phone",
        "Fax": "fax",
        "Email": "email",
        "SupportRepId": "support_rep_id"
    }, inplace=True)

    return customers


def load_genre_data() -> pd.DataFrame:
    """
    Loads genre data from a CSV file and standardizes column names.

    Returns
    -------
    pd.DataFrame
        DataFrame containing genres with columns: 'genre_id', 'name'.
    """
    genres = pd.read_csv(SAMPLES_DIR / "genres.csv")

    genres.rename(columns={
        "GenreId": "genre_id",
        "Name": "name"
    }, inplace=True)

    return genres


def load_invoice_data() -> pd.DataFrame:
    """
    Loads invoice data from a CSV file and standardizes column names.

    Returns
    -------
    pd.DataFrame
        DataFrame containing invoices with columns:
        'invoice_id', 'customer_id', 'invoice_date', 'billing_address', 'billing_city',
        'billing_state', 'billing_country', 'billing_postal_code', 'total'.
    """
    invoices = pd.read_csv(SAMPLES_DIR / "invoices.csv")

    invoices.rename(columns={
        "InvoiceId": "invoice_id",
        "CustomerId": "customer_id",
        "InvoiceDate": "invoice_date",
        "BillingAddress": "billing_address",
        "BillingCity": "billing_city",
        "BillingState": "billing_state",
        "BillingCountry": "billing_country",
        "BillingPostalCode": "billing_postal_code",
        "Total": "total"
    }, inplace=True)

    invoices["invoice_date"] = pd.to_datetime(invoices["invoice_date"])

    return invoices


def load_invoice_item_data() -> pd.DataFrame:
    """
    Loads invoice item data from a CSV file and standardizes column names.

    Returns
    -------
    pd.DataFrame
        DataFrame containing invoice items with columns:
        'invoice_line_id', 'invoice_id', 'track_id', 'unit_price', 'quantity'.
    """
    invoice_items = pd.read_csv(SAMPLES_DIR / "invoice_items.csv")

    invoice_items.rename(columns={
        "InvoiceLineId": "invoice_line_id",
        "InvoiceId": "invoice_id",
        "TrackId": "track_id",
        "UnitPrice": "unit_price",
        "Quantity": "quantity"
    }, inplace=True)

    return invoice_items


def load_media_type_data() -> pd.DataFrame:
    """
    Loads media type data from a CSV file and standardizes column names.

    Returns
    -------
    pd.DataFrame
        DataFrame containing media types with columns: 'media_type_id', 'name'.
    """
    media_types = pd.read_csv(SAMPLES_DIR / "media_types.csv")

    media_types.rename(columns={
        "MediaTypeId": "media_type_id",
        "Name": "name"
    }, inplace=True)

    return media_types


def load_playlist_data() -> pd.DataFrame:
    """
    Loads playlist data from a CSV file and standardizes column names.

    Returns
    -------
    pd.DataFrame
        DataFrame containing playlists with columns: 'playlist_id', 'name'.
    """
    playlists = pd.read_csv(SAMPLES_DIR / "playlists.csv")

    playlists.rename(columns={
        "PlaylistId": "playlist_id",
        "Name": "name"
    }, inplace=True)

    return playlists


def load_playlist_track_data() -> pd.DataFrame:
    """
    Loads playlist-track association data from a CSV file and standardizes column names.

    Returns
    -------
    pd.DataFrame
        DataFrame containing playlist-track mappings with columns: 'playlist_id', 'track_id'.
    """
    playlist_track = pd.read_csv(SAMPLES_DIR / "playlist_track.csv")

    playlist_track.rename(columns={
        "PlaylistId": "playlist_id",
        "TrackId": "track_id"
    }, inplace=True)

    return playlist_track


def load_track_data() -> pd.DataFrame:
    """
    Loads track data from a CSV file and standardizes column names.

    Returns
    -------
    pd.DataFrame
        DataFrame containing tracks with columns:
        'track_id', 'name', 'album_id', 'media_type_id', 'genre_id',
        'composer', 'milliseconds', 'total_bytes', 'unit_price'.
    """
    tracks = pd.read_csv(SAMPLES_DIR / "tracks.csv")

    tracks.rename(columns={
        "TrackId": "track_id",
        "Name": "name",
        "AlbumId": "album_id",
        "MediaTypeId": "media_type_id",
        "GenreId": "genre_id",
        "Composer": "composer",
        "Milliseconds": "milliseconds",
        "Bytes": "total_bytes",
        "UnitPrice": "unit_price"
    }, inplace=True)

    return tracks


def load_employees_data() -> pd.DataFrame:
    """Load sample employee data from CSV."""
    employees = pd.read_csv(SAMPLES_DIR / "employees.csv")

    employees.rename(columns={
        "EmployeeId": "employee_id",
        "LastName": "last_name",
        "FirstName": "first_name",
        "Title": "title",
        "ReportsTo": "reports_to",
        "BirthDate": "birth_date",
        "HireDate": "hire_date",
        "Address": "address",
        "City": "city",
        "State": "state",
        "Country": "country",
        "PostalCode": "postal_code",
        "Phone": "phone",
        "Fax": "fax",
        "Email": "email"
    }, inplace=True)

    employees["birth_date"] = pd.to_datetime(employees["birth_date"])
    employees["hire_date"] = pd.to_datetime(employees["hire_date"])

    return employees
