#!/usr/bin/python
""" RecordDetail class """


from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, String, SmallInteger, Integer,
    Date, Text, TIMESTAMP, ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields


class RecordDetail(BaseModel, Base):
    """
    Representation of Record Detail.

    This class defines the RecordDetail model, which stores record detail information.

    Attributes:
        batch (str): Unique batch number (primary key).
        operation (int): Operation ID (FK: mole_commerce.operation.id).
        receiver (int): Client account ID (FK: mole_commerce.client_account.id).
        source_depot (int): Source depot ID (FK: mole_commerce.depot_detail.id).
        dest_depot (int): Destination depot ID (FK: mole_commerce.depot_detail.id).
        rec_date (date): Record date.
        ref (str): Reference number.
        app_user (int): User account ID (FK: mole_commerce.user_account.id).
        rec_desc (str): Record description.
        datetime (timestamp): Record creation timestamp.
    """
    if models.storage_t == "db":
        __tablename__ = 'record_detail'
        __table_args__ = {'schema': 'mole_commerce'}

        batch = Column(String(50), primary_key=True,
                       doc="Unique batch number")
        operation = Column(SmallInteger,
                           ForeignKey('mole_commerce.operation.id'),
                           doc="Operation ID")
        receiver = Column(Integer,
                          ForeignKey('mole_commerce.client_account.id'),
                          doc="Client account ID")
        source_depot = Column(SmallInteger,
                              ForeignKey('mole_commerce.depot_detail.id'),
                              doc="Source depot ID")
        dest_depot = Column(SmallInteger,
                            ForeignKey('mole_commerce.depot_detail.id'),
                            doc="Destination depot ID")
        rec_date = Column(Date, nullable=False,
                          doc="Record date")
        ref = Column(String(50), nullable=False,
                     doc="Reference number")
        app_user = Column(SmallInteger,
                          ForeignKey('mole_commerce.user_account.id'),
                          doc="User account ID")
        rec_desc = Column(Text,
                          doc="Record description")
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp(),
                          doc="Record creation timestamp")

        # Establish relationships
        operation_rel = relationship('Operation', backref='record_details',
                                      doc="Operation relationship")
        receiver_rel = relationship('ClientAccount', backref='record_details',
                                     doc="Client account relationship")
        source_depot_rel = relationship('DepotDetail',
                                        foreign_keys=[source_depot],
                                        backref='source_record_details',
                                        doc="Source depot relationship")
        dest_depot_rel = relationship('DepotDetail',
                                      foreign_keys=[dest_depot],
                                      backref='dest_record_details',
                                      doc="Destination depot relationship")
        app_user_rel = relationship('UserAccount', backref='record_details',
                                     doc="User account relationship")

    def __init__(self, *args, **kwargs):
        """
        RecordDetail initialization.

        Initializes the RecordDetail object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class RecordDetailSchema(Schema):
    """
    RecordDetail schema.

    This schema defines the structure of the RecordDetail data.

    Attributes:
        batch (str): Unique batch number.
        operation (int): Operation ID.
        receiver (int): Client account ID.
        source_depot (int): Source depot ID.
        dest_depot (int): Destination depot ID.
        rec_date (date): Record date.
        ref (str): Reference number.
        app_user (int): User account ID.
        rec_desc (str): Record description.
    """
    batch = fields.Str(required=True, doc="Unique batch number")
    operation = fields.Int(required=True, doc="Operation ID")
    receiver = fields.Int(required=True, doc="Client account ID")
    source_depot = fields.Int(required=True, doc="Source depot ID")
    dest_depot = fields.Int(required=True, doc="Destination depot ID")
    rec_date = fields.Date(required=True, doc="Record date")
    ref = fields.Str(required=True, doc="Reference number")
    app_user = fields.Int(required=True, doc="User account ID")
    rec_desc = fields.Str(required=False, doc="Record description")
