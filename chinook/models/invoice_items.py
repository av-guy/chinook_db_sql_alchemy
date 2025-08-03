"""
invoice_items.py

Defines the InvoiceItems SQLAlchemy ORM model for the `invoice_items` table.

This table stores the individual line items on each invoice in the Chinook database.
Each record links an invoice to a track and specifies quantity and price.

Classes
-------
InvoiceItems
    ORM model for the `invoice_items` table, representing track-level purchases on invoices.
"""

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import ForeignKey

from kink import di

BASE = di[DeclarativeBase]


class InvoiceItems(BASE):
    """
    Represents an individual line item on an invoice.

    Each record associates a track with an invoice, including unit price and quantity.

    Attributes
    ----------
    invoice_line_id : Mapped[int]
        Unique identifier for the invoice line item. Primary key with auto-increment.

    invoice_id : Mapped[int]
        Foreign key referencing `invoices.invoice_id`.

    track_id : Mapped[int]
        Foreign key referencing `tracks.track_id`.

    unit_price : Mapped[float]
        Price per unit (track) in USD.

    quantity : Mapped[int]
        Number of units (tracks) purchased.
    """

    __tablename__ = "invoice_items"

    invoice_line_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.invoice_id"), index=True)
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.track_id"), index=True)
    unit_price: Mapped[float] = mapped_column()
    quantity: Mapped[int] = mapped_column()
