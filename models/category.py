#!/usr/bin/python
""" Category class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields
from datetime import datetime


class Category(BaseModel, Base):
    """
    Representation of Category.

    This class defines the Category model, which stores category information.

    Attributes:
        CategoryID (int): Unique category ID.
        Name (str): Category name.
        Type (str): Category type (Expense or Income).
        Description (str): Category description.
        CreatedAt (datetime): Timestamp when the category was created.
        UpdatedAt (datetime): Timestamp when the category was last updated.
    """
    if models.storage_t == "db":
        __tablename__ = 'Category'
        __table_args__ = {'schema': 'fet_db'}

        CategoryID = Column(Integer, primary_key=True, autoincrement=True,
                    doc="Unique category ID")
        Name = Column(String(100), nullable=False,
                          doc="Category name")
        Type = Column(Enum('Expense', 'Income'), nullable=False,
                      doc="Category type (Expense or Income)")
        Description = Column(String(255),
                              doc="Category description")
        CreatedAt = Column(TIMESTAMP, default=datetime.utcnow,
                           doc="Timestamp when the category was created")
        UpdatedAt = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow,
                           doc="Timestamp when the category was last updated")

        # Establish relationships
        budgets = relationship('Budget', backref='category',
                                doc="Budget relationship")
        expenses = relationship('Expense', backref='category',
                                 doc="Expense relationship")
        incomes = relationship('Income', backref='category',
                                doc="Income relationship")


    def __init__(self, *args, **kwargs):
        """
        Category initialization.

        Initializes the Category object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class CategorySchema(Schema):
    """
    Category schema.

    This schema defines the structure of the Category data.

    Attributes:
        CategoryID (int): Unique category ID.
        Name (str): Category name.
        Type (str): Category type (Expense or Income).
        Description (str): Category description.
        CreatedAt (datetime): Timestamp when the category was created.
        UpdatedAt (datetime): Timestamp when the category was last updated.
    """
    CategoryID = fields.Int(required=False, doc="Unique category ID")
    Name = fields.Str(required=True, doc="Category name")
    Type = fields.Str(required=True, doc="Category type (Expense or Income)")
    Description = fields.Str(required=False, doc="Category description")
    CreatedAt = fields.DateTime(required=False, doc="Timestamp when the category was created")
    UpdatedAt = fields.DateTime(required=False, doc="Timestamp when the category was last updated")
