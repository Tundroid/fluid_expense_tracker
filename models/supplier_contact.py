#!/usr/bin/python
""" SupplierContact class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, SmallInteger, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class SupplierContact(BaseModel, Base):
    """
    Representation of Supplier Contact.

    This class defines the SupplierContact model, which stores supplier contact information.

    Attributes:
        id (int): Unique supplier contact ID.
        con_name (str): Contact name.
        con_phone (str): Contact phone number.
        con_email (str): Contact email.
        supplier (int): Supplier ID (FK: mole_commerce.supplier.id).
        datetime (timestamp): Supplier contact creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'sup_contact'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique supplier contact ID")
        con_name = Column(String(50), nullable=False, unique=True,
                          doc="Contact name")
        con_phone = Column(String(50), nullable=False,
                           doc="Contact phone number")
        con_email = Column(String(50), nullable=False,
                           doc="Contact email")
        supplier = Column(SmallInteger,
                          ForeignKey('mole_commerce.supplier.id'),
                          nullable=False,
                          doc="Supplier ID")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Supplier contact creation timestamp")

        supplier_rel = relationship('Supplier', backref='sup_contacts',
                                     doc="Supplier relationship")

    def __init__(self, *args, **kwargs):
        """
        SupplierContact initialization.

        Initializes the SupplierContact object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class SupplierContactSchema(Schema):
    """
    SupplierContact schema.

    This schema defines the structure of the SupplierContact data.

    Attributes:
        id (int): Unique supplier contact ID.
        con_name (str): Contact name.
        con_phone (str): Contact phone number.
        con_email (str): Contact email.
        supplier (int): Supplier ID.
    """
    id = fields.Int(required=False, doc="Unique supplier contact ID")
    con_name = fields.Str(required=True, doc="Contact name")
    con_phone = fields.Str(required=True, doc="Contact phone number")
    con_email = fields.Email(required=True, doc="Contact email")
    supplier = fields.Int(required=True, doc="Supplier ID")
