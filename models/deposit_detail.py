#!/usr/bin/python
""" DepositDetail class """


from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, String, Date, SmallInteger, TIMESTAMP, ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class DepositDetail(BaseModel, Base):
    """
    Representation of Deposit Detail.

    This class defines the DepositDetail model, which stores deposit detail information.

    Attributes:
        batch (str): Unique deposit batch.
        d_date (date): Deposit date.
        app_user (int): User account ID (FK: mole_commerce.user_account.id).
        datetime (timestamp): Deposit detail creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'deposit_detail'
        __table_args__ = {'schema': 'mole_commerce'}

        batch = Column(String(50), primary_key=True,
                       doc="Unique deposit batch")
        d_date = Column(Date, nullable=False,
                        doc="Deposit date")
        app_user = Column(SmallInteger,
                          ForeignKey('mole_commerce.user_account.id'),
                          nullable=False,
                          doc="User account ID")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Deposit detail creation timestamp")

        user_account = relationship('UserAccount', backref='deposit_details',
                                    doc="User account relationship")

    def __init__(self, *args, **kwargs):
        """
        DepositDetail initialization.

        Initializes the DepositDetail object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class DepositDetailSchema(Schema):
    """
    DepositDetail schema.

    This schema defines the structure of the DepositDetail data.

    Attributes:
        batch (str): Unique deposit batch.
        d_date (date): Deposit date.
        app_user (int): User account ID.
    """
    batch = fields.Str(required=True, doc="Unique deposit batch")
    d_date = fields.Date(required=True, doc="Deposit date")
    app_user = fields.Int(required=True, doc="User account ID")
