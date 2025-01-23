#!/usr/bin/python
""" PayMode class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, SmallInteger, Boolean, TIMESTAMP
from sqlalchemy.sql import func
import models
from marshmallow import Schema, fields


class PayMode(BaseModel, Base):
    """
    Representation of Pay Mode.

    This class defines the PayMode model, which stores payment mode information.

    Attributes:
        id (int): Unique payment mode ID.
        mode_name (str): Payment mode name.
        is_active (bool): Payment mode active status.
        datetime (timestamp): Payment mode creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'pay_mode'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique payment mode ID")
        mode_name = Column(String(50), nullable=False, unique=True,
                           doc="Payment mode name")
        is_active = Column(Boolean, nullable=False, default=True,
                           doc="Payment mode active status")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Payment mode creation timestamp")

    def __init__(self, *args, **kwargs):
        """
        PayMode initialization.

        Initializes the PayMode object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class PayModeSchema(Schema):
    """
    PayMode schema.

    This schema defines the structure of the PayMode data.

    Attributes:
        id (int): Unique payment mode ID.
        mode_name (str): Payment mode name.
        is_active (bool): Payment mode active status.
    """
    id = fields.Int(required=False, doc="Unique payment mode ID")
    mode_name = fields.Str(required=True, doc="Payment mode name")
    is_active = fields.Bool(required=False, doc="Payment mode active status")
