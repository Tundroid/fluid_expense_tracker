#!/usr/bin/python
""" DepotDetail class """


from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, String, Text, Enum, Boolean, TIMESTAMP, SmallInteger
)
from sqlalchemy.sql import func
import models
from marshmallow import Schema, fields


class DepotDetail(BaseModel, Base):
    """
    Representation of DepotDetail.

    This class defines the DepotDetail model, which stores depot information.

    Attributes:
        id (int): Unique depot ID.
        depot_name (str): Depot name.
        depot_desc (str): Depot description.
        depot_type (str): Depot type (Source, Destination, Both).
        is_metered (bool): Metered status.
        datetime (timestamp): Depot creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'depot_detail'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column('id', SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique depot ID")
        depot_name = Column(String(50), nullable=False, unique=True,
                            doc="Depot name")
        depot_desc = Column(Text, nullable=False,
                            doc="Depot description")
        depot_type = Column(Enum('Source', 'Destination', 'Both'),
                            nullable=False,
                            doc="Depot type")
        is_metered = Column(Boolean, nullable=False, default=True,
                            doc="Metered status")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Depot creation timestamp")

    def __init__(self, *args, **kwargs):
        """
        DepotDetail initialization.

        Initializes the DepotDetail object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class DepotDetailSchema(Schema):
    """
    DepotDetail schema.

    This schema defines the structure of the DepotDetail data.

    Attributes:
        id (int): Unique depot ID.
        depot_name (str): Depot name.
        depot_desc (str): Depot description.
        depot_type (str): Depot type.
        is_metered (bool): Metered status.
    """
    id = fields.Int(required=False, doc="Unique depot ID")
    depot_name = fields.Str(required=True, doc="Depot name")
    depot_desc = fields.Str(required=True, doc="Depot description")
    depot_type = fields.Str(required=True, doc="Depot type")
    is_metered = fields.Bool(required=False, doc="Metered status")
