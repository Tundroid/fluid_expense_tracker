#!/usr/bin/python
""" UserAccount class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, SmallInteger, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class UserAccount(BaseModel, Base):
    """
    Representation of User Account.

    This class defines the UserAccount model, which stores user account information.

    Attributes:
        id (int): Unique user account ID (FK: mole_account.account.id).
        acc_type (int): Account type ID (FK: mole_account.acc_type.id).
        is_active (bool): Account status.
        datetime (timestamp): User account creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'user_account'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, ForeignKey('mole_account.account.id'),
                    primary_key=True,
                    doc="Unique user account ID")
        acc_type = Column(SmallInteger, ForeignKey('mole_account.acc_type.id'),
                          nullable=False, default=3,
                          doc="Account type ID")
        is_active = Column(Boolean, nullable=False, default=True,
                           doc="Account status")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="User account creation timestamp")

        acc_type_rel = relationship('AccountType', backref='user_accounts',
                                    doc="Account type relationship")
        account_rel = relationship('Account', backref='user_account',
                                   doc="Account relationship")

    def __init__(self, *args, **kwargs):
        """
        UserAccount initialization.

        Initializes the UserAccount object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class UserAccountSchema(Schema):
    """
    UserAccount schema.

    This schema defines the structure of the UserAccount data.

    Attributes:
        id (int): Unique user account ID.
        acc_type (int): Account type ID.
        is_active (bool): Account status.
    """
    id = fields.Int(required=False, doc="Unique user account ID")
    acc_type = fields.Int(required=True, doc="Account type ID")
    is_active = fields.Bool(required=True, doc="Account status")
