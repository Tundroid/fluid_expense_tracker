#!/usr/bin/python
""" Expense class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Time, Text, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields
from datetime import datetime


class Expense(BaseModel, Base):
    """
    Representation of Expense.

    This class defines the Expense model, which stores expense information.

    Attributes:
        ExpenseID (int): Unique expense ID.
        UserID (int): User ID (FK: User.UserID).
        CategoryID (int): Category ID (FK: Category.CategoryID).
        Description (str): Expense description.
        Amount (int): Expense amount.
        Date (date): Expense date.
        Time (time): Expense time.
        BudgetID (int): Budget ID (FK: Budget.BudgetID).
        Recurring (bool): Whether the expense is recurring.
        CreatedAt (datetime): Timestamp when the expense was created.
        UpdatedAt (datetime): Timestamp when the expense was last updated.
    """
    if models.storage_t == "db":
        __tablename__ = 'Expense'
        __table_args__ = {'schema': 'fet_db'}

        ExpenseID = Column(Integer, primary_key=True, autoincrement=True,
                    doc="Unique expense ID")
        UserID = Column(Integer, ForeignKey('User.UserID'), nullable=False,
                      doc="User ID")
        CategoryID = Column(Integer, ForeignKey('Category.CategoryID'), nullable=False,
                            doc="Category ID")
        Description = Column(Text,
                              doc="Expense description")
        Amount = Column(Integer, nullable=False,
                          doc="Expense amount")
        Date = Column(Date, nullable=False,
                      doc="Expense date")
        Time = Column(Time, nullable=False,
                       doc="Expense time")
        BudgetID = Column(Integer, ForeignKey('Budget.BudgetID'),
                          doc="Budget ID")
        Recurring = Column(Boolean, default=False,
                            doc="Whether the expense is recurring")
        CreatedAt = Column(TIMESTAMP, default=datetime.utcnow,
                           doc="Timestamp when the expense was created")
        UpdatedAt = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow,
                           doc="Timestamp when the expense was last updated")

        # Establish relationships
        user = relationship('User', backref='expenses',
                            doc="User relationship")
        category = relationship('Category', backref='expenses',
                                 doc="Category relationship")
        budget = relationship('Budget', backref='expenses',
                               doc="Budget relationship")


    def __init__(self, *args, **kwargs):
        """
        Expense initialization.

        Initializes the Expense object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class ExpenseSchema(Schema):
    """
    Expense schema.

    This schema defines the structure of the Expense data.

    Attributes:
        ExpenseID (int): Unique expense ID.
        UserID (int): User ID.
        CategoryID (int): Category ID.
        Description (str): Expense description.
        Amount (int): Expense amount.
        Date (date): Expense date.
        Time (time): Expense time.
        BudgetID (int): Budget ID.
        Recurring (bool): Whether the expense is recurring.
        CreatedAt (datetime): Timestamp when the expense was created.
        UpdatedAt (datetime): Timestamp when the expense was last updated.
    """
    ExpenseID = fields.Int(required=False, doc="Unique expense ID")
    UserID = fields.Int(required=True, doc="User ID")
    CategoryID = fields.Int(required=True, doc="Category ID")
    Description = fields.Str(required=False, doc="Expense description")
    Amount = fields.Int(required=True, doc="Expense amount")
    Date = fields.Date(required=True, doc="Expense date")
    Time = fields.Time(required=True, doc="Expense time")
    BudgetID = fields.Int(required=False, doc="Budget ID")
    Recurring = fields.Bool(required=False, doc="Whether the expense is recurring")
    CreatedAt = fields.DateTime(required=False, doc="Timestamp when the expense was created")
    UpdatedAt = fields.DateTime(required=False, doc="Timestamp when the expense was last updated")
