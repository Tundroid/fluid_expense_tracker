#!/usr/bin/python
""" Barcode class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class Barcode(BaseModel, Base):
    """
    Representation of Barcode.

    This class defines the Barcode model, which stores barcode information.

    Attributes:
        barcode (str): Unique barcode.
        item (int): Item ID (FK: mole_commerce.item.id).
    """
    if models.storage_t == "db":
        __tablename__ = 'barcode'
        __table_args__ = {'schema': 'mole_commerce'}

        barcode = Column(String(50), primary_key=True,
                         doc="Unique barcode")
        item = Column(Integer, ForeignKey('mole_commerce.item.id'),
                      nullable=False,
                      doc="Item ID")

        item_rel = relationship('Item', backref='barcodes',
                                doc="Item relationship")

    def __init__(self, *args, **kwargs):
        """
        Barcode initialization.

        Initializes the Barcode object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class BarcodeSchema(Schema):
    """
    Barcode schema.

    This schema defines the structure of the Barcode data.

    Attributes:
        barcode (str): Unique barcode.
        item (int): Item ID.
    """
    barcode = fields.Str(required=True, doc="Unique barcode")
    item = fields.Int(required=True, doc="Item ID")
