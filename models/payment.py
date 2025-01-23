#!/usr/bin/python
""" Payment class """


from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, Integer, SmallInteger, String, Date,
    Text, TIMESTAMP, ForeignKey, Boolean
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class Payment(BaseModel, Base):
    """
    Representation of Payment.

    This class defines the Payment model, which stores payment information.

    Attributes:
        id (int): Unique payment ID.
        invoice (str): Invoice number (FK: mole_commerce.record_detail.batch).
        amount (int): Payment amount.
        pay_date (date): Payment date.
        is_instant (bool): Instant payment status.
        mode (int): Payment mode ID (FK: mole_commerce.pay_mode.id).
        app_user (int): User account ID (FK: mole_commerce.user_account.id).
        pay_desc (str): Payment description.
        datetime (timestamp): Payment creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'payment'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(Integer, primary_key=True, autoincrement=True,
                    doc="Unique payment ID")
        invoice = Column(String(50),
                         ForeignKey('mole_commerce.record_detail.batch'),
                         doc="Invoice number")
        amount = Column(Integer, nullable=False,
                        doc="Payment amount")
        pay_date = Column(Date, nullable=False,
                          doc="Payment date")
        is_instant = Column(Boolean, nullable=False, default=True,
                            doc="Instant payment status")
        mode = Column(SmallInteger,
                      ForeignKey('mole_commerce.pay_mode.id'), default=1,
                      doc="Payment mode ID")
        app_user = Column(SmallInteger,
                          ForeignKey('mole_commerce.user_account.id'),
                          doc="User account ID")
        pay_desc = Column(Text,
                          doc="Payment description")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Payment creation timestamp")

        # Establish relationships
        invoice_rel = relationship('RecordDetail', backref='payments',
                                    doc="Invoice relationship")
        mode_rel = relationship('PayMode', backref='payments',
                                 doc="Payment mode relationship")
        app_user_rel = relationship('UserAccount', backref='payments',
                                     doc="User account relationship")

    def __init__(self, *args, **kwargs):
        """
        Payment initialization.

        Initializes the Payment object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class PaymentSchema(Schema):
    """
    Payment schema.

    This schema defines the structure of the Payment data.

    Attributes:
        id (int): Unique payment ID.
        invoice (str): Invoice number.
        amount (int): Payment amount.
        pay_date (date): Payment date.
        is_instant (bool): Instant payment status.
        mode (int): Payment mode ID.
        app_user (int): User account ID.
        pay_desc (str): Payment description.
    """
    id = fields.Int(required=False, doc="Unique payment ID")
    invoice = fields.Str(required=True, doc="Invoice number")
    amount = fields.Int(required=True, doc="Payment amount")
    pay_date = fields.Date(required=True, doc="Payment date")
    is_instant = fields.Bool(required=False, doc="Instant payment status")
    mode = fields.Int(required=True, doc="Payment mode ID")
    app_user = fields.Int(required=False, doc="User account ID")
    pay_desc = fields.Str(required=False, doc="Payment description")
