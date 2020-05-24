# import uuid
import datetime

from app.main import db
from app.main.model.customer import Note


def upsert_note(data):
    note = None

    if 'id' in data and data['id'] != '00000000-0000-0000-0000-000000000000':
        note = Note.query.filter_by(id=data['id']).first()

    if not note:
        new_note = Note(
            customer_id=data['customerId'],
            value=data['value']
        )
        save_changes(new_note)
        return new_note, 201
    else:
        note.value = data['value']
        save_changes(note)
        return note, 200


def get_a_note(id):
    return Note.query.filter_by(id=id).first()


def delete_note(id):
    note = Note.query.filter_by(id=id).first()

    if note is not None:
        db.session.delete(Note.query.filter_by(id=id).first())
        db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
