#!/usr/bin/python
""" Depot class """


from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, SmallInteger, Integer, ForeignKey, PrimaryKeyConstraint
)
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class Depot(BaseModel, Base):
    """
    Representation of Depot.

    This class defines the Depot model, which stores depot stock information.

    Attributes:
        depot (int): Depot ID (FK: mole_commerce.depot_detail.id).
        item_id (int): Item ID (FK: mole_commerce.item.id).
        stock (int): Current stock quantity.
    """
    if models.storage_t == "db":
        __tablename__ = 'depot'
        __table_args__ = {'schema': 'mole_commerce'}

        depot = Column(SmallInteger,
                       ForeignKey('mole_commerce.depot_detail.id'),
                       nullable=False,
                       doc="Depot ID")
        item_id = Column(Integer,
                         ForeignKey('mole_commerce.item.id'), nullable=False,
                         doc="Item ID")
        stock = Column(Integer, nullable=False, default=0,
                       doc="Current stock quantity")

        __table_args__ = (
            PrimaryKeyConstraint('depot', 'item_id'),
        )

        depot_rel = relationship('DepotDetail', backref='depot_stock',
                                  doc="Depot relationship")
        item_rel = relationship('Item', backref='depot_stock',
                                 doc="Item relationship")

    def __init__(self, *args, **kwargs):
        """
        Depot initialization.

        Initializes the Depot object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class DepotSchema(Schema):
    """
    Depot schema.

    This schema defines the structure of the Depot data.

    Attributes:
        depot (int): Depot ID.
        item_id (int): Item ID.
        stock (int): Current stock quantity.
    """
    depot = fields.Int(required=True, doc="Depot ID")
    item_id = fields.Int(required=True, doc="Item ID")
    stock = fields.Int(required=True, doc="Current stock quantity")
