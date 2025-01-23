#!/usr/bin/python
""" Deposit class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class Deposit(BaseModel, Base):
    """
    Representation of Deposit.

    This class defines the Deposit model, which stores deposit information.

    Attributes:
        payment (int): Payment ID (FK: mole_commerce.payment.id).
        batch (str): Deposit batch (FK: mole_commerce.deposit_detail.batch).
    """
    if models.storage_t == "db":
        __tablename__ = 'deposit'
        __table_args__ = {'schema': 'mole_commerce'}

        payment = Column(Integer, ForeignKey('mole_commerce.payment.id'),
                         primary_key=True,
                         doc="Payment ID")
        batch = Column(String(50),
                       ForeignKey('mole_commerce.deposit_detail.batch'),
                       doc="Deposit batch")

        # Establish relationships
        payment_rel = relationship('Payment', backref='deposit',
                                    doc="Payment relationship")
        batch_rel = relationship('DepositDetail', backref='deposits',
                                  doc="Deposit detail relationship")

    def __init__(self, *args, **kwargs):
        """
        Deposit initialization.

        Initializes the Deposit object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class DepositSchema(Schema):
    """
    Deposit schema.

    This schema defines the structure of the Deposit data.

    Attributes:
        payment (int): Payment ID.
        batch (str): Deposit batch.
    """
    payment = fields.Int(required=True, doc="Payment ID")
    batch = fields.Str(required=True, doc="Deposit batch")
