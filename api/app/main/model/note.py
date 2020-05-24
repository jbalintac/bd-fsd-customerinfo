# from sqlalchemy.dialects.postgresql import UUID
# from .. import db

# import uuid

# class Note(db.Model):
#     """ Note Model for storing note related details """
#     __tablename__ = "note"

#     id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     customer_id = db.Column(UUID(as_uuid=True), db.ForeignKey('customer.id'))
#     value = db.Column(db.Text)

#     def __repr__(self):
#         return "<Note '{}'>".format(self.id)


