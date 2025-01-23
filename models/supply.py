#!/usr/bin/python
""" Supply class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class Supply(BaseModel, Base):
    """
    Representation of Supply.

    This class defines the Supply model, which stores supply information.

    Attributes:
        id (int): Unique supply ID.
        item (int): Item ID (FK: mole_commerce.item.id).
        quantity (int): Supply quantity.
        unit_cost (int): Unit cost.
        expiry (date): Expiry date.
        batch (str): Supply batch number (FK: mole_commerce.supply_detail.batch).
    """
    if models.storage_t == "db":
        __tablename__ = 'supply'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(BigInteger, primary_key=True, autoincrement=True,
                    doc="Unique supply ID")
        item = Column(Integer, ForeignKey('mole_commerce.item.id'),
                      doc="Item ID")
        quantity = Column(Integer, nullable=False,
                          doc="Supply quantity")
        unit_cost = Column(Integer, nullable=False,
                           doc="Unit cost")
        expiry = Column(Date, nullable=False,
                        doc="Expiry date")
        batch = Column(String(50),
                       ForeignKey('mole_commerce.supply_detail.batch'),
                       doc="Supply batch number")

        # Establish relationships
        item_rel = relationship('Item', backref='supplies',
                                doc="Item relationship")
        batch_rel = relationship('SupplyDetail', backref='supplies',
                                 doc="Supply detail relationship")

        # Virtual column (not explicitly defined)
        @property
        def total(self):
            """
            Computed total cost.

            Returns:
                int: Total cost (quantity * unit_cost)
            """
            return self.quantity * self.unit_cost

    def __init__(self, *args, **kwargs):
        """
        Supply initialization.

        Initializes the Supply object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class SupplySchema(Schema):
    """
    Supply schema.

    This schema defines the structure of the Supply data.

    Attributes:
        id (int): Unique supply ID.
        item (int): Item ID.
        quantity (int): Supply quantity.
        unit_cost (int): Unit cost.
        expiry (date): Expiry date.
        batch (str): Supply batch number.
        total (int): Computed total cost.
    """
    id = fields.Int(required=False, doc="Unique supply ID")
    item = fields.Int(required=True, doc="Item ID")
    quantity = fields.Int(required=True, doc="Supply quantity")
    unit_cost = fields.Int(required=True, doc="Unit cost")
    expiry = fields.Date(required=True, doc="Expiry date")
    batch = fields.Str(required=True, doc="Supply batch number")
