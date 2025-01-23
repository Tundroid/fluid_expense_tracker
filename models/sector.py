#!/usr/bin/python
""" Sector class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, SmallInteger, TIMESTAMP
from sqlalchemy.sql import func
import models
from marshmallow import Schema, fields


class Sector(BaseModel, Base):
    """
    Representation of Sector.

    This class defines the Sector model, which stores sector information.

    Attributes:
        id (int): Unique sector ID.
        sec_name (str): Sector name.
        sec_desc (str): Sector description.
        datetime (timestamp): Sector creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'sector'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique sector ID")
        sec_name = Column(String(50), nullable=False, unique=True,
                          doc="Sector name")
        sec_desc = Column(Text,
                          doc="Sector description")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Sector creation timestamp")

    def __init__(self, *args, **kwargs):
        """
        Sector initialization.

        Initializes the Sector object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class SectorSchema(Schema):
    """
    Sector schema.

    This schema defines the structure of the Sector data.

    Attributes:
        id (int): Unique sector ID.
        sec_name (str): Sector name.
        sec_desc (str): Sector description.
    """
    id = fields.Int(required=False, doc="Unique sector ID")
    sec_name = fields.Str(required=True, doc="Sector name")
    sec_desc = fields.Str(required=False, doc="Sector description")
