#!/usr/bin/python
""" Record class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class Record(BaseModel, Base):
    """
    Representation of Record.

    This class defines the Record model, which stores record information.

    Attributes:
        id (int): Unique record ID.
        item (int): Item ID (FK: mole_commerce.item.id).
        quantity (int): Record quantity.
        source_stock (int): Source stock quantity.
        dest_stock (int): Destination stock quantity.
        amount (int): Record amount.
        batch (str): Batch number (FK: mole_commerce.record_detail.batch).
    """
    if models.storage_t == "db":
        __tablename__ = 'record'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(BigInteger, primary_key=True, autoincrement=True,
                    doc="Unique record ID")
        item = Column(Integer, ForeignKey('mole_commerce.item.id'),
                      doc="Item ID")
        quantity = Column(Integer, nullable=False,
                          doc="Record quantity")
        source_stock = Column(Integer, nullable=False,
                              doc="Source stock quantity")
        dest_stock = Column(Integer, nullable=False,
                            doc="Destination stock quantity")
        amount = Column(Integer, nullable=False,
                        doc="Record amount")
        batch = Column(String(50),
                       ForeignKey('mole_commerce.record_detail.batch'),
                       doc="Batch number")

        # Establish relationships
        item_rel = relationship('Item', backref='records',
                                doc="Item relationship")
        batch_rel = relationship('RecordDetail', backref='records',
                                 doc="Batch relationship")

        # Virtual column (not explicitly defined)
        @property
        def total(self):
            """
            Computed total amount.

            Returns:
                int: Total amount (quantity * amount)
            """
            return self.quantity * self.amount

    def __init__(self, *args, **kwargs):
        """
        Record initialization.

        Initializes the Record object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class RecordSchema(Schema):
    """
    Record schema.

    This schema defines the structure of the Record data.

    Attributes:
        id (int): Unique record ID.
        item (int): Item ID.
        quantity (int): Record quantity.
        source_stock (int): Source stock quantity.
        dest_stock (int): Destination stock quantity.
        amount (int): Record amount.
        batch (str): Batch number.
        total (int): Computed total amount.
    """
    id = fields.Int(required=False, doc="Unique record ID")
    item = fields.Int(required=True, doc="Item ID")
    quantity = fields.Int(required=True, doc="Record quantity")
    source_stock = fields.Int(required=False, doc="Source stock quantity")
    dest_stock = fields.Int(required=False, doc="Destination stock quantity")
    amount = fields.Int(required=True, doc="Record amount")
    batch = fields.Str(required=True, doc="Batch number")
