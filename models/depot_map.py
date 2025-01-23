#!/usr/bin/python
""" DepotMap class """


import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint, SmallInteger
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields


class DepotMap(BaseModel, Base):
    """
    Representation of Depot Map.

    This class defines the DepotMap model, which maps depot sources to destinations
    via specific operations.

    Attributes:
        source (int): The source depot ID (FK: mole_commerce.depot_detail.id).
        destination (int): The destination depot ID (FK: mole_commerce.depot_detail.id).
        operation (int): The operation ID (FK: mole_commerce.operation.id).
    """
    if models.storage_t == "db":
        __tablename__ = 'depot_map'
        __table_args__ = {'schema': 'mole_commerce'}

        source = Column(SmallInteger,
                        ForeignKey('mole_commerce.depot_detail.id'),
                        nullable=False,
                        doc="Source depot ID")
        destination = Column(SmallInteger,
                             ForeignKey('mole_commerce.depot_detail.id'),
                             nullable=False,
                             doc="Destination depot ID")
        operation = Column(SmallInteger,
                           ForeignKey('mole_commerce.operation.id'),
                           nullable=False,
                           doc="Operation ID")

        __table_args__ = (
            PrimaryKeyConstraint('source', 'destination', 'operation'),
        )

        depot_source_rel = relationship('DepotDetail', foreign_keys=[source],
                                        backref='depot_map_sources',
                                        doc="Depot source relationship")
        depot_destination_rel = relationship('DepotDetail',
                                             foreign_keys=[destination],
                                             backref='depot_map_destinations',
                                             doc="Depot destination relationship")
        operation_rel = relationship('Operation', backref='depot_maps',
                                      doc="Operation relationship")

    def __init__(self, *args, **kwargs):
        """
        DepotMap initialization.

        Initializes the DepotMap object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class DepotMapSchema(Schema):
    """
    DepotMap schema.

    This schema defines the structure of the DepotMap data.

    Attributes:
        source (int): The source depot ID.
        destination (int): The destination depot ID.
        operation (int): The operation ID.
    """
    source = fields.Int(required=True, doc="Source depot ID")
    destination = fields.Int(required=True, doc="Destination depot ID")
    operation = fields.Int(required=True, doc="Operation ID")
