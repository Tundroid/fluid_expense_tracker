#!/usr/bin/python
""" Account class """


from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, SmallInteger, String, Boolean,
    ForeignKey, TIMESTAMP
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class Account(BaseModel, Base):
    """
    Representation of Account.

    This class defines the Account model, which stores account information.

    Attributes:
        id (int): Unique account ID.
        acc_name (str): Account name.
        acc_pwd (str): Account password.
        acc_type (int): Account type ID (FK: mole_account.acc_type.id).
        is_active (bool): Account active status.
        datetime (timestamp): Account creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'account'
        __table_args__ = {'schema': 'mole_account'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique account ID")
        acc_name = Column(String(50), nullable=False, unique=True,
                          doc="Account name")
        acc_pwd = Column(String(256), nullable=False, default='shopend',
                         doc="Account password")
        acc_type = Column(SmallInteger, ForeignKey('mole_account.acc_type.id'),
                          nullable=False, default=3,
                          doc="Account type ID")
        is_active = Column(Boolean, nullable=False, default=True,
                           doc="Account active status")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Account creation timestamp")

        acc_type_rel = relationship('AccountType', backref='accounts',
                                    doc="Account type relationship")

    def __init__(self, *args, **kwargs):
        """
        Account initialization.

        Initializes the Account object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class AccountSchema(Schema):
    """
    Account schema.

    This schema defines the structure of the Account data.

    Attributes:
        id (int): Unique account ID.
        acc_name (str): Account name.
        acc_pwd (str): Account password.
        acc_type (int): Account type ID.
        is_active (bool): Account active status.
    """
    id = fields.Int(required=False, doc="Unique account ID")
    acc_name = fields.Str(required=True, doc="Account name")
    acc_pwd = fields.Str(required=False, doc="Account password")
    acc_type = fields.Int(required=False, doc="Account type ID")
    is_active = fields.Bool(required=False, doc="Account active status")
