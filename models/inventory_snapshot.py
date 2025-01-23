#!/usr/bin/python
""" InventorySnapshot class """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class InventorySnapshot(BaseModel, Base):
    """
    Representation of Inventory Snapshot.

    This class defines the InventorySnapshot model, which stores inventory snapshots.

    Attributes:
        batch (str): Batch number.
        item_id (int): Item ID.
        stock (int): Stock quantity.
    """
    if models.storage_t == "db":
        __tablename__ = 'inventory_snapshot'
        __table_args__ = {'schema': 'mole_commerce'}

        batch = Column(String(50), primary_key=True)
        item_id = Column(Integer, primary_key=True)
        stock = Column(Integer, nullable=False)

        # Foreign key relationships
        record_detail = relationship("RecordDetail", backref="inventory_snapshots")
        item = relationship("Item", backref="inventory_snapshots")

        # Constraints
        __table_args__ = (
            ForeignKeyConstraint(
                [batch], ["mole_commerce.record_detail.batch"], 
                ondelete="RESTRICT", onupdate="CASCADE"
            ),
            ForeignKeyConstraint(
                [item_id], ["mole_commerce.item.id"], 
                ondelete="RESTRICT", onupdate="CASCADE"
            ),
        )


    def __init__(self, *args, **kwargs):
        """
        InventorySnapshot initialization.

        Initializes the InventorySnapshot object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class InventorySnapshotSchema(Schema):
    """
    InventorySnapshot schema.

    This schema defines the structure of the InventorySnapshot data.

    Attributes:
        batch (str): Batch number.
        item_id (int): Item ID.
        stock (int): Stock quantity.
    """
    batch = fields.Str(required=True)
    item_id = fields.Int(required=True)
    stock = fields.Int(required=True)
