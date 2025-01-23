#!/usr/bin/python
""" Supplier class """


from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, String, Text, SmallInteger, ForeignKey, TIMESTAMP, Integer
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class Supplier(BaseModel, Base):
    """
    Representation of Supplier.

    This class defines the Supplier model, which stores supplier information.

    Attributes:
        id (int): Unique supplier ID.
        sup_name (str): Supplier name.
        sup_type (int): Supplier type ID (FK: mole_commerce.sup_type.id).
        sup_desc (str): Supplier description.
        datetime (timestamp): Supplier creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'supplier'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique supplier ID")
        sup_name = Column(String(50), nullable=False, unique=True,
                          doc="Supplier name")
        sup_type = Column(SmallInteger,
                          ForeignKey('mole_commerce.sup_type.id'),
                          nullable=False,
                          doc="Supplier type ID")
        sup_desc = Column(Text,
                          doc="Supplier description")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Supplier creation timestamp")

        sup_type_rel = relationship('SupplierType', backref='suppliers',
                                     doc="Supplier type relationship")

    def __init__(self, *args, **kwargs):
        """
        Supplier initialization.

        Initializes the Supplier object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class SupplierSchema(Schema):
    """
    Supplier schema.

    This schema defines the structure of the Supplier data.

    Attributes:
        id (int): Unique supplier ID.
        sup_name (str): Supplier name.
        sup_type (int): Supplier type ID.
        sup_desc (str): Supplier description.
    """
    id = fields.Int(required=False, doc="Unique supplier ID")
    sup_name = fields.Str(required=True, doc="Supplier name")
    sup_type = fields.Int(required=True, doc="Supplier type ID")
    sup_desc = fields.Str(required=False, doc="Supplier description")
