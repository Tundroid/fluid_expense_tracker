#!/usr/bin/python
""" SupplyDetail class """


from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, String, SmallInteger, Integer, Date, Text,
    TIMESTAMP, ForeignKey, Boolean
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class SupplyDetail(BaseModel, Base):
    """
    Representation of Supply Detail.

    This class defines the SupplyDetail model, which stores supply detail information.

    Attributes:
        batch (str): Unique supply batch number.
        supplier (int): Supplier ID (FK: mole_commerce.supplier.id).
        sup_date (date): Supply date.
        receiver (int): Client account ID (FK: mole_commerce.client_account.id).
        ref (str): Reference number.
        app_user (int): User account ID (FK: mole_commerce.user_account.id).
        is_stocked (bool): Stock status.
        sup_desc (str): Supply description.
        datetime (timestamp): Supply detail creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'supply_detail'
        __table_args__ = {'schema': 'mole_commerce'}

        batch = Column(String(50), primary_key=True, unique=True,
                       doc="Unique supply batch number")
        supplier = Column(SmallInteger,
                          ForeignKey('mole_commerce.supplier.id'),
                          doc="Supplier ID")
        sup_date = Column(Date, nullable=False,
                          doc="Supply date")
        receiver = Column(Integer,
                          ForeignKey('mole_commerce.client_account.id'),
                          doc="Client account ID")
        ref = Column(String(50), nullable=False,
                     doc="Reference number")
        app_user = Column(Integer,
                          ForeignKey('mole_commerce.user_account.id'),
                          doc="User account ID")
        is_stocked = Column(Boolean, nullable=False, default=False,
                            doc="Stock status")
        sup_desc = Column(Text,
                          doc="Supply description")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Supply detail creation timestamp")

        # Establish relationships
        supplier_rel = relationship('Supplier', backref='supply_details',
                                     doc="Supplier relationship")
        receiver_rel = relationship('ClientAccount', backref='supply_details',
                                     doc="Client account relationship")
        app_user_rel = relationship('UserAccount', backref='supply_details',
                                     doc="User account relationship")

    def __init__(self, *args, **kwargs):
        """
        SupplyDetail initialization.

        Initializes the SupplyDetail object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class SupplyDetailSchema(Schema):
    """
    SupplyDetail schema.

    This schema defines the structure of the SupplyDetail data.

    Attributes:
        batch (str): Unique supply batch number.
        supplier (int): Supplier ID.
        sup_date (date): Supply date.
        receiver (int): Client account ID.
        ref (str): Reference number.
        app_user (int): User account ID.
        is_stocked (bool): Stock status.
        sup_desc (str): Supply description.
    """
    batch = fields.Str(required=True, doc="Unique supply batch number")
    supplier = fields.Int(required=True, doc="Supplier ID")
    sup_date = fields.Date(required=True, doc="Supply date")
    receiver = fields.Int(required=True, doc="Client account ID")
    ref = fields.Str(required=True, doc="Reference number")
    app_user = fields.Int(required=True, doc="User account ID")
    is_stocked = fields.Bool(required=True, doc="Stock status")
    sup_desc = fields.Str(required=False, doc="Supply description")
