"""
customers.py

Defines the Customers SQLAlchemy ORM model for the `customers` table.

This table stores information about customers in the Chinook database, including
contact details and optional association with a support representative.

Classes
-------
Customers
    ORM model for the `customers` table, representing individuals who make purchases.
"""

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, ForeignKey

from kink import di

BASE = di[DeclarativeBase]


class Customers(BASE):
    """
    Represents a customer in the database.

    Each customer has contact and location information, and may be associated with an
    employee who serves as their support representative.

    Attributes
    ----------
    customer_id : Mapped[int]
        Unique identifier for the customer. Primary key with auto-increment.

    first_name : Mapped[str]
        Customer's first name. Max length: 40 characters.

    last_name : Mapped[str]
        Customer's last name. Max length: 20 characters.

    company : Mapped[str]
        Name of the customer’s company, if applicable. Max length: 80 characters.

    address : Mapped[str]
        Street address. Max length: 70 characters.

    city : Mapped[str]
        City of residence. Max length: 40 characters.

    state : Mapped[str]
        State or province. Max length: 40 characters.

    country : Mapped[str]
        Country of residence. Max length: 40 characters.

    postal_code : Mapped[str]
        Postal or ZIP code. Max length: 10 characters.

    phone : Mapped[str]
        Phone number. Max length: 24 characters.

    fax : Mapped[str]
        Fax number. Max length: 24 characters.

    email : Mapped[str]
        Email address. Max length: 60 characters.

    support_rep_id : Mapped[int]
        Foreign key referencing `employees.employee_id`.
    """

    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(20))
    company: Mapped[str] = mapped_column(String(80), nullable=True)
    address: Mapped[str] = mapped_column(String(70), nullable=True)
    city: Mapped[str] = mapped_column(String(40), nullable=True)
    state: Mapped[str] = mapped_column(String(40), nullable=True)
    country: Mapped[str] = mapped_column(String(40), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(10), nullable=True)
    phone: Mapped[str] = mapped_column(String(24), nullable=True)
    fax: Mapped[str] = mapped_column(String(24), nullable=True)
    email: Mapped[str] = mapped_column(String(60), nullable=True)
    support_rep_id: Mapped[int] = mapped_column(ForeignKey(
        "employees.employee_id"), index=True, nullable=True)

    def __repr__(self) -> str:
        return (
            f"<Customers(customer_id={self.customer_id}, "
            f"name='{self.first_name} {self.last_name}', "
            f"email='{self.email}')>"
        )
