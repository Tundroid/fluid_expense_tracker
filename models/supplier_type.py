#!/usr/bin/python
""" SupplierType class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, SmallInteger, TIMESTAMP
from sqlalchemy.sql import func
import models
from marshmallow import Schema, fields


class SupplierType(BaseModel, Base):
    """
    Representation of Supplier Type.

    This class defines the SupplierType model, which stores supplier type information.

    Attributes:
        id (int): Unique supplier type ID.
        st_name (str): Supplier type name.
        st_desc (str): Supplier type description.
        datetime (timestamp): Supplier type creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'sup_type'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique supplier type ID")
        st_name = Column(String(50), nullable=False, unique=True,
                         doc="Supplier type name")
        st_desc = Column(Text, nullable=False,
                         doc="Supplier type description")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Supplier type creation timestamp")

    def __init__(self, *args, **kwargs):
        """
        SupplierType initialization.

        Initializes the SupplierType object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class SupplierTypeSchema(Schema):
    """
    SupplierType schema.

    This schema defines the structure of the SupplierType data.

    Attributes:
        id (int): Unique supplier type ID.
        st_name (str): Supplier type name.
        st_desc (str): Supplier type description.
    """
    id = fields.Int(required=False, doc="Unique supplier type ID")
    st_name = fields.Str(required=True, doc="Supplier type name")
    st_desc = fields.Str(required=True, doc="Supplier type description")
