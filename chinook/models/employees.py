"""
employees.py

Defines the Employees SQLAlchemy ORM model for the `employees` table.

This table stores employee information in the Chinook database, including personal
details and organizational hierarchy through a self-referencing manager field.

Classes
-------
Employees
    ORM model for the `employees` table, representing staff members and their reporting structure.
"""

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, DateTime, ForeignKey

from kink import di

BASE = di[DeclarativeBase]


class Employees(BASE):
    """
    Represents an employee in the database.

    Employees may hold various job titles and can optionally report to another employee,
    forming a hierarchical reporting structure via a self-referential foreign key.

    Attributes
    ----------
    employee_id : Mapped[int]
        Unique identifier for the employee. Primary key with auto-increment.

    last_name : Mapped[str]
        Employee's last name. Max length: 20 characters.

    first_name : Mapped[str]
        Employee's first name. Max length: 20 characters.

    title : Mapped[str]
        Job title of the employee. Max length: 30 characters.

    reports_to : Mapped[int]
        Optional foreign key referencing `employees.employee_id`, indicating the employee's manager.

    birth_date : Mapped[DateTime]
        Date of birth of the employee.

    hire_date : Mapped[DateTime]
        Date the employee was hired.

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
    """

    __tablename__ = "employees"

    employee_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True)
    last_name: Mapped[str] = mapped_column(String(20))
    first_name: Mapped[str] = mapped_column(String(20))
    title: Mapped[str] = mapped_column(String(30))
    reports_to: Mapped[int] = mapped_column(
        ForeignKey("employees.employee_id"), index=True, nullable=True)
    birth_date: Mapped[datetime] = mapped_column()
    hire_date: Mapped[datetime] = mapped_column()
    address: Mapped[str] = mapped_column(String(70))
    city: Mapped[str] = mapped_column(String(40))
    state: Mapped[str] = mapped_column(String(40))
    country: Mapped[str] = mapped_column(String(40))
    postal_code: Mapped[str] = mapped_column(String(10))
    phone: Mapped[str] = mapped_column(String(24))
    fax: Mapped[str] = mapped_column(String(24))
    email: Mapped[str] = mapped_column(String(60))
