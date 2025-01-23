#!/usr/bin/python
""" Income class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Time, Text, TIMESTAMP
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields
from datetime import datetime


class Income(BaseModel, Base):
    """
    Representation of Income.

    This class defines the Income model, which stores income information.

    Attributes:
        IncomeID (int): Unique income ID.
        UserID (int): User ID (FK: User.UserID).
        CategoryID (int): Category ID (FK: Category.CategoryID).
        Description (str): Income description.
        Amount (int): Income amount.
        Date (date): Income date.
        Time (time): Income time.
        CreatedAt (datetime): Timestamp when the income was created.
        UpdatedAt (datetime): Timestamp when the income was last updated.
    """
    if models.storage_t == "db":
        __tablename__ = 'Income'
        __table_args__ = {'schema': 'fet_db'}

        IncomeID = Column(Integer, primary_key=True, autoincrement=True,
                    doc="Unique income ID")
        UserID = Column(Integer, ForeignKey('User.UserID'), nullable=False,
                      doc="User ID")
        CategoryID = Column(Integer, ForeignKey('Category.CategoryID'), nullable=False,
                            doc="Category ID")
        Description = Column(Text,
                              doc="Income description")
        Amount = Column(Integer, nullable=False,
                          doc="Income amount")
        Date = Column(Date, nullable=False,
                      doc="Income date")
        Time = Column(Time, nullable=False,
                       doc="Income time")
        CreatedAt = Column(TIMESTAMP, default=datetime.utcnow,
                           doc="Timestamp when the income was created")
        UpdatedAt = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow,
                           doc="Timestamp when the income was last updated")

        # Establish relationships
        user = relationship('User', backref='incomes',
                            doc="User relationship")
        category = relationship('Category', backref='incomes',
                                 doc="Category relationship")


    def __init__(self, *args, **kwargs):
        """
        Income initialization.

        Initializes the Income object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class IncomeSchema(Schema):
    """
    Income schema.

    This schema defines the structure of the Income data.

    Attributes:
        IncomeID (int): Unique income ID.
        UserID (int): User ID.
        CategoryID (int): Category ID.
        Description (str): Income description.
        Amount (int): Income amount.
        Date (date): Income date.
        Time (time): Income time.
        CreatedAt (datetime): Timestamp when the income was created.
        UpdatedAt (datetime): Timestamp when the income was last updated.
    """
    IncomeID = fields.Int(required=False, doc="Unique income ID")
    UserID = fields.Int(required=True, doc="User ID")
    CategoryID = fields.Int(required=True, doc="Category ID")
    Description = fields.Str(required=False, doc="Income description")
    Amount = fields.Int(required=True, doc="Income amount")
    Date = fields.Date(required=True, doc="Income date")
    Time = fields.Time(required=True, doc="Income time")
    CreatedAt = fields.DateTime(required=False, doc="Timestamp when the income was created")
    UpdatedAt = fields.DateTime(required=False, doc="Timestamp when the income was last updated")
