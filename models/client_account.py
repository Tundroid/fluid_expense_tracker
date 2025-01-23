#!/usr/bin/python
""" ClientAccount class """


from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, String, SmallInteger, Enum, Boolean, Integer, TIMESTAMP
)
from sqlalchemy.sql import func
import models
from marshmallow import Schema, fields


class ClientAccount(BaseModel, Base):
    """
    Representation of Client Account.

    This class defines the ClientAccount model, which stores client account information.

    Attributes:
        id (int): Unique client account ID.
        acc_name (str): Client account name.
        acc_type (str): Client account type (Consumer, Worker, Both).
        is_active (bool): Client account active status.
        credit_limit (int): Client account credit limit.
        datetime (timestamp): Client account creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'client_account'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique client account ID")
        acc_name = Column(String(50), nullable=False, unique=True,
                          doc="Client account name")
        acc_type = Column(Enum('Consumer', 'Worker', 'Both'),
                          nullable=False, default='Consumer',
                          doc="Client account type")
        is_active = Column(Boolean, nullable=False, default=True,
                           doc="Client account active status")
        credit_limit = Column(Integer, nullable=False, default=25000,
                              doc="Client account credit limit")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Client account creation timestamp")

    def __init__(self, *args, **kwargs):
        """
        ClientAccount initialization.

        Initializes the ClientAccount object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class ClientAccountSchema(Schema):
    """
    ClientAccount schema.

    This schema defines the structure of the ClientAccount data.

    Attributes:
        id (int): Unique client account ID.
        acc_name (str): Client account name.
        acc_type (str): Client account type.
        is_active (bool): Client account active status.
        credit_limit (int): Client account credit limit.
    """
    id = fields.Int(required=False, doc="Unique client account ID")
    acc_name = fields.Str(required=True, doc="Client account name")
    acc_type = fields.Str(required=True, doc="Client account type")
    is_active = fields.Bool(required=False, doc="Client account active status")
    credit_limit = fields.Int(required=False, doc="Client account credit limit")
