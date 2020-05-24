from sqlalchemy import Enum
from sqlalchemy.dialects.postgresql import UUID
from .. import db

import enum, uuid

class Status(enum.Enum):
    prospective = 0
    current = 1
    nonActive = 2

class Customer(db.Model):
    """ Customer Model for storing customer related details """
    __tablename__ = "customer"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_date = db.Column(db.DateTime, nullable=False)
    contact = db.Column(db.String(50))
    name = db.Column(db.String(200))
    description = db.Column(db.Text)
    status = db.Column(Enum(Status))
    notes = db.relationship("Note")

    def __repr__(self):
        return "<Customer '{}'>".format(self.name)


class Note(db.Model):
    """ Note Model for storing note related details """
    __tablename__ = "note"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    customer_id = db.Column(UUID(as_uuid=True), db.ForeignKey('customer.id'))
    value = db.Column(db.Text)

    def __repr__(self):
        return "<Note '{}'>".format(self.id)