#!/usr/bin/python
""" ItemCategory class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, TIMESTAMP, SmallInteger
from sqlalchemy.sql import func
import models
from marshmallow import Schema, fields


class ItemCategory(BaseModel, Base):
    """
    Representation of Item Category.

    This class defines the ItemCategory model, which stores item category information.

    Attributes:
        id (int): Unique item category ID.
        cat_name (str): Item category name.
        cat_desc (str): Item category description.
        datetime (timestamp): Item category creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'item_cat'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique item category ID")
        cat_name = Column(String(50), nullable=False, unique=True,
                          doc="Item category name")
        cat_desc = Column(Text,
                          doc="Item category description")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Item category creation timestamp")

    def __init__(self, *args, **kwargs):
        """
        ItemCategory initialization.

        Initializes the ItemCategory object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class ItemCategorySchema(Schema):
    """
    ItemCategory schema.

    This schema defines the structure of the ItemCategory data.

    Attributes:
        id (int): Unique item category ID.
        cat_name (str): Item category name.
        cat_desc (str): Item category description.
    """
    id = fields.Int(required=False, doc="Unique item category ID")
    cat_name = fields.Str(required=True, doc="Item category name")
    cat_desc = fields.Str(required=False, doc="Item category description")
