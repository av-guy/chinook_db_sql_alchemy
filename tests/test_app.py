"""
Test bootstrap behavior for the Chinook database setup.

These tests verify the application's ability to initialize the database engine
based on the presence or absence of the CHINOOK_CONN_STRING environment variable.
They also confirm that the Albums table is populated after initialization.
"""

import os

from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine

from kink import di

from chinook import initialize, get_engine
from chinook.models import Albums


def cleanup_env_and_file():
    """Ensure test environment is clean"""
    if os.path.exists("chinook.db"):
        os.remove("chinook.db")

    if "CHINOOK_CONN_STRING" in os.environ:
        del os.environ["CHINOOK_CONN_STRING"]


def test_creates_chinook_db_when_env_not_set():
    """Test that a physical file-based DB is created by default"""
    cleanup_env_and_file()

    assert not os.path.exists("chinook.db")
    initialize()

    assert os.path.exists("chinook.db")
    engine: Engine = get_engine()

    with Session(engine) as session:
        assert session.query(Albums).count() > 0

    engine.dispose()


def test_uses_in_memory_db_when_env_set(monkeypatch):
    """Test that an in-memory DB is used when env var is set"""
    cleanup_env_and_file()

    monkeypatch.setenv("CHINOOK_CONN_STRING", "sqlite:///:memory:")
    initialize()

    engine: Engine = di[Engine]

    with Session(engine) as session:
        assert session.query(Albums).count() > 0

    engine.dispose()
