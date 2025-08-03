"""
invoices.py

Defines the Invoices SQLAlchemy ORM model for the `invoices` table.

This table stores invoice records in the Chinook database, representing customer purchases.
Each invoice includes billing information, a customer reference, and a timestamp.

Classes
-------
Invoices
    ORM model for the `invoices` table, representing sales transactions made by customers.
"""
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, DateTime, ForeignKey

from kink import di

BASE = di[DeclarativeBase]


class Invoices(BASE):
    """
    Represents a customer invoice in the database.

    Each invoice records a purchase, including billing details and a reference to
    the customer who made the purchase.

    Attributes
    ----------
    invoice_id : Mapped[int]
        Unique identifier for the invoice. Primary key with auto-increment.

    customer_id : Mapped[int]
        Foreign key referencing `customers.customer_id`.

    invoice_date : Mapped[DateTime]
        Date and time the invoice was issued.

    billing_address : Mapped[str]
        Address to which the invoice was billed. Max length: 70 characters.

    billing_city : Mapped[str]
        City of the billing address. Max length: 40 characters.

    billing_state : Mapped[str]
        State of the billing address. Max length: 40 characters.

    billing_country : Mapped[str]
        Country of the billing address. Max length: 40 characters.

    billing_postal_code : Mapped[str]
        Postal code of the billing address. Max length: 10 characters.

    total : Mapped[float]
        Total amount of the invoice in USD.
    """

    __tablename__ = "invoices"

    invoice_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.customer_id"), index=True)
    invoice_date: Mapped[datetime] = mapped_column()
    billing_address: Mapped[str] = mapped_column(String(70), nullable=True)
    billing_city: Mapped[str] = mapped_column(String(40), nullable=True)
    billing_state: Mapped[str] = mapped_column(String(40), nullable=True)
    billing_country: Mapped[str] = mapped_column(String(40), nullable=True)
    billing_postal_code: Mapped[str] = mapped_column(String(10), nullable=True)
    total: Mapped[float] = mapped_column()
