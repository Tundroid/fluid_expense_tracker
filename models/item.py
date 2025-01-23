#!/usr/bin/python
""" Item class """


from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, String, Integer, SmallInteger, ForeignKey, Boolean, TIMESTAMP
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class Item(BaseModel, Base):
    """
    Representation of Item.

    This class defines the Item model, which stores item information.

    Attributes:
        id (int): Unique item ID.
        item_name (str): Item name.
        item_cat (int): Item category ID (FK: mole_commerce.item_cat.id).
        cost_price (int): Item cost price.
        selling_price (int): Item selling price.
        min_sell_price (int): Minimum selling price.
        min_order_qty (int): Minimum order quantity.
        family (int): Family ID (FK: mole_commerce.family.id).
        sector (int): Sector ID (FK: mole_commerce.sector.id).
        is_active (bool): Item active status.
        is_metered (bool): Item metered status.
        datetime (timestamp): Item creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'item'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(Integer, primary_key=True, autoincrement=True,
                    doc="Unique item ID")
        item_name = Column(String(50), nullable=False, unique=True,
                           doc="Item name")
        item_cat = Column(SmallInteger,
                          ForeignKey('mole_commerce.item_cat.id'),
                          nullable=False, default=1,
                          doc="Item category ID")
        cost_price = Column(Integer, nullable=False, default=0,
                            doc="Item cost price")
        selling_price = Column(Integer, nullable=False, default=0,
                               doc="Item selling price")
        min_sell_price = Column(Integer, nullable=False, default=0,
                                doc="Minimum selling price")
        min_order_qty = Column(Integer, nullable=False, default=5,
                               doc="Minimum order quantity")
        family = Column(SmallInteger,
                        ForeignKey('mole_commerce.family.id'),
                        nullable=False, default=1,
                        doc="Family ID")
        sector = Column(SmallInteger,
                        ForeignKey('mole_commerce.sector.id'),
                        nullable=False, default=1,
                        doc="Sector ID")
        is_active = Column(Boolean, nullable=False, default=True,
                           doc="Item active status")
        is_metered = Column(Boolean, nullable=False, default=True,
                            doc="Item metered status")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Item creation timestamp")

        item_cat_rel = relationship('ItemCategory', backref='items',
                                    doc="Item category relationship")
        family_rel = relationship('Family', backref='items',
                                  doc="Family relationship")
        sector_rel = relationship('Sector', backref='items',
                                  doc="Sector relationship")

    def __init__(self, *args, **kwargs):
        """
        Item initialization.

        Initializes the Item object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class ItemSchema(Schema):
    """
    Item schema.

    This schema defines the structure of the Item data.

    Attributes:
        id (int): Unique item ID.
        item_name (str): Item name.
        item_cat (int): Item category ID.
        cost_price (int): Item cost price.
        selling_price (int): Item selling price.
        min_sell_price (int): Minimum selling price.
        min_order_qty (int): Minimum order quantity.
        family (int): Family ID.
        sector (int): Sector ID.
        is_active (bool): Item active status.
        is_metered (bool): Item metered status.
    """
    id = fields.Int(required=False, doc="Unique item ID")
    item_name = fields.Str(required=True, doc="Item name")
    item_cat = fields.Int(required=True, doc="Item category ID")
    cost_price = fields.Int(required=True, doc="Item cost price")
    selling_price = fields.Int(required=True, doc="Item selling price")
    min_sell_price = fields.Int(required=True, doc="Minimum selling price")
    min_order_qty = fields.Int(required=True, doc="Minimum order quantity")
    family = fields.Int(required=True, doc="Family ID")
    sector = fields.Int(required=True, doc="Sector ID")
    is_active = fields.Bool(required=False, doc="Item active status")
    is_metered = fields.Bool(required=False, doc="Item metered status")
