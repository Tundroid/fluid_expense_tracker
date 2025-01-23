#!/usr/bin/python
""" Saving class """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Text, TIMESTAMP
from sqlalchemy.orm import relationship
import models
from marshmallow import Schema, fields
from datetime import datetime


class Saving(BaseModel, Base):
    """
    Representation of Saving.

    This class defines the Saving model, which stores saving information.

    Attributes:
        SavingID (int): Unique saving ID.
        UserID (int): User ID (FK: User.UserID).
        SavingGoalID (int): Saving goal ID (FK: SavingGoal.SavingGoalID).
        Amount (int): Saving amount.
        Date (date): Saving date.
        Location (str): Saving location.
        Description (str): Saving description.
        CreatedAt (datetime): Timestamp when the saving was created.
        UpdatedAt (datetime): Timestamp when the saving was last updated.
    """
    if models.storage_t == "db":
        __tablename__ = 'Saving'
        __table_args__ = {'schema': 'fet_db'}

        SavingID = Column(Integer, primary_key=True, autoincrement=True,
                    doc="Unique saving ID")
        UserID = Column(Integer, ForeignKey('User.UserID'), nullable=False,
                      doc="User ID")
        SavingGoalID = Column(Integer, ForeignKey('SavingGoal.SavingGoalID'),
                               doc="Saving goal ID")
        Amount = Column(Integer, nullable=False,
                          doc="Saving amount")
        Date = Column(Date, nullable=False,
                      doc="Saving date")
        Location = Column(Text,
                           doc="Saving location")
        Description = Column(Text,
                              doc="Saving description")
        CreatedAt = Column(TIMESTAMP, default=datetime.utcnow,
                           doc="Timestamp when the saving was created")
        UpdatedAt = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow,
                           doc="Timestamp when the saving was last updated")

        # Establish relationships
        user = relationship('User', backref='savings',
                            doc="User relationship")
        saving_goal = relationship('SavingGoal', backref='savings',
                                    doc="Saving goal relationship")


    def __init__(self, *args, **kwargs):
        """
        Saving initialization.

        Initializes the Saving object with the given arguments.
        """
        super().__init__(*args, **kwargs)


class SavingSchema(Schema):
    """
    Saving schema.

    This schema defines the structure of the Saving data.

    Attributes:
        SavingID (int): Unique saving ID.
        UserID (int): User ID.
        SavingGoalID (int): Saving goal ID.
        Amount (int): Saving amount.
        Date (date): Saving date.
        Location (str): Saving location.
        Description (str): Saving description.
        CreatedAt (datetime): Timestamp when the saving was created.
        UpdatedAt (datetime): Timestamp when the saving was last updated.
    """
    SavingID = fields.Int(required=False, doc="Unique saving ID")
    UserID = fields.Int(required=True, doc="User ID")
    SavingGoalID = fields.Int(required=False, doc="Saving goal ID")
    Amount = fields.Int(required=True, doc="Saving amount")
    Date = fields.Date(required=True, doc="Saving date")
    Location = fields.Str(required=False, doc="Saving location")
    Description = fields.Str(required=False, doc="Saving description")
    CreatedAt = fields.DateTime(required=False, doc="Timestamp when the saving was created")
    UpdatedAt = fields.DateTime(required=False, doc="Timestamp when the saving was last updated")
