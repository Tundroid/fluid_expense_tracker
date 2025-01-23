#!/usr/bin/python
""" Budget class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Text, TIMESTAMP
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields
from datetime import datetime


class Budget(BaseModel, Base):
    """
    Representation of Budget.

    This class defines the Budget model, which stores budget information.

    Attributes:
        BudgetID (int): Unique budget ID.
        UserID (int): User ID (FK: User.UserID).
        Amount (int): Budget amount.
        Start (date): Budget start date.
        End (date): Budget end date.
        CategoryID (int): Category ID (FK: Category.CategoryID).
        Description (str): Budget description.
        CreatedAt (datetime): Timestamp when the budget was created.
        UpdatedAt (datetime): Timestamp when the budget was last updated.
    """
    if models.storage_t == "db":
        __tablename__ = 'Budget'
        __table_args__ = {'schema': 'fet_db'}

        BudgetID = Column(Integer, primary_key=True, autoincrement=True,
                    doc="Unique budget ID")
        UserID = Column(Integer, ForeignKey('User.UserID'), nullable=False,
                      doc="User ID")
        Amount = Column(Integer, nullable=False,
                          doc="Budget amount")
        Start = Column(Date, nullable=False,
                        doc="Budget start date")
        End = Column(Date, nullable=False,
                      doc="Budget end date")
        CategoryID = Column(Integer, ForeignKey('Category.CategoryID'),
                            doc="Category ID")
        Description = Column(Text,
                              doc="Budget description")
        CreatedAt = Column(TIMESTAMP, default=datetime.utcnow,
                           doc="Timestamp when the budget was created")
        UpdatedAt = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow,
                           doc="Timestamp when the budget was last updated")

        # Establish relationships
        user = relationship('User', backref='budgets',
                            doc="User relationship")
        category = relationship('Category', backref='budgets',
                                 doc="Category relationship")
        expenses = relationship('Expense', backref='budget',
                                 doc="Expense relationship")


    def __init__(self, *args, **kwargs):
        """
        Budget initialization.

        Initializes the Budget object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class BudgetSchema(Schema):
    """
    Budget schema.

    This schema defines the structure of the Budget data.

    Attributes:
        BudgetID (int): Unique budget ID.
        UserID (int): User ID.
        Amount (int): Budget amount.
        Start (date): Budget start date.
        End (date): Budget end date.
        CategoryID (int): Category ID.
        Description (str): Budget description.
        CreatedAt (datetime): Timestamp when the budget was created.
        UpdatedAt (datetime): Timestamp when the budget was last updated.
    """
    BudgetID = fields.Int(required=False, doc="Unique budget ID")
    UserID = fields.Int(required=True, doc="User ID")
    Amount = fields.Int(required=True, doc="Budget amount")
    Start = fields.Date(required=True, doc="Budget start date")
    End = fields.Date(required=True, doc="Budget end date")
    CategoryID = fields.Int(required=False, doc="Category ID")
    Description = fields.Str(required=False, doc="Budget description")
    CreatedAt = fields.DateTime(required=False, doc="Timestamp when the budget was created")
    UpdatedAt = fields.DateTime(required=False, doc="Timestamp when the budget was last updated")