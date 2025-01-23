#!/usr/bin/python
""" Family class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, TIMESTAMP, SmallInteger
from sqlalchemy.sql import func
import models
from marshmallow import Schema, fields


class Family(BaseModel, Base):
    """
    Representation of Family.

    This class defines the Family model, which stores family information.

    Attributes:
        id (int): Unique family ID.
        fam_name (str): Family name.
        fam_desc (str): Family description.
        datetime (timestamp): Family creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'family'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique family ID")
        fam_name = Column(String(50), nullable=False, unique=True,
                          doc="Family name")
        fam_desc = Column(Text,
                          doc="Family description")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Family creation timestamp")

    def __init__(self, *args, **kwargs):
        """
        Family initialization.

        Initializes the Family object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class FamilySchema(Schema):
    """
    Family schema.

    This schema defines the structure of the Family data.

    Attributes:
        id (int): Unique family ID.
        fam_name (str): Family name.
        fam_desc (str): Family description.
    """
    id = fields.Int(required=False, doc="Unique family ID")
    fam_name = fields.Str(required=True, doc="Family name")
    fam_desc = fields.Str(required=False, doc="Family description")
