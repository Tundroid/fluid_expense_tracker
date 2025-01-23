#!/usr/bin/python
""" Operation class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, CHAR, Text, SmallInteger
import models
from marshmallow import Schema, fields


class Operation(BaseModel, Base):
    """
    Representation of Operation.

    This class defines the Operation model, which stores operation information.

    Attributes:
        id (int): Unique operation ID.
        op_name (str): Operation name.
        op_sign (str): Operation sign (+/-).
        op_desc (str): Operation description.
    """
    if models.storage_t == "db":
        __tablename__ = 'operation'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True,
                    doc="Unique operation ID")
        op_name = Column(String(50), nullable=False, unique=True,
                         doc="Operation name")
        op_sign = Column(CHAR(1), nullable=False, default='+',
                         doc="Operation sign (+/-)")
        op_desc = Column(Text, nullable=False,
                         doc="Operation description")
    else:
        pass

    def __init__(self, *args, **kwargs):
        """
        Operation initialization.

        Initializes the Operation object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class OperationSchema(Schema):
    """
    Operation schema.

    This schema defines the structure of the Operation data.

    Attributes:
        id (int): Unique operation ID.
        op_name (str): Operation name.
        op_sign (str): Operation sign (+/-).
        op_desc (str): Operation description.
    """
    id = fields.Int(required=False, doc="Unique operation ID")
    op_name = fields.Str(required=True, doc="Operation name")
    op_sign = fields.Str(required=True, doc="Operation sign (+/-)")
    op_desc = fields.Str(required=True, doc="Operation description")
