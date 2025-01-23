#!/usr/bin/python
""" AccountType class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, SmallInteger, String
import models
from marshmallow import Schema, fields


class AccountType(BaseModel, Base):
    """
    Representation of Account Type.

    This class defines the AccountType model, which stores different account types.

    Attributes:
        id (int): Unique account type ID.
        type_name (str): Name of the account type.
    """
    if models.storage_t == "db":
        __tablename__ = 'acc_type'
        __table_args__ = {'schema': 'mole_account'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique account type ID")
        type_name = Column(String(50), nullable=False, unique=True,
                           doc="Name of the account type")

    def __init__(self, *args, **kwargs):
        """
        AccountType initialization.

        Initializes the AccountType object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class AccountTypeSchema(Schema):
    """
    AccountType schema.

    This schema defines the structure of the AccountType data.

    Attributes:
        id (int): Unique account type ID.
        type_name (str): Name of the account type.
    """
    id = fields.Int(required=False, doc="Unique account type ID")
    type_name = fields.Str(required=True, doc="Name of the account type")
