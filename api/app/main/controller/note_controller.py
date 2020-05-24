from flask import request
from flask_restplus import Resource
from flask_cors import cross_origin

from ..util.dto import NoteDto
from ..service.note_service import upsert_note, get_a_note, delete_note

api = NoteDto.api
_note = NoteDto.note


@api.route('/')
class noteList(Resource):
    @api.response(201, 'note successfully created.')
    @api.doc('create a new note')
    @api.marshal_with(_note)
    @api.expect(_note, validate=True)
    def post(self):
        """Creates or update a note """
        data = request.json
        return upsert_note(data=data)


@api.route('/<id>')
@api.param('id', 'The note identifier')
@api.response(404, 'note not found.')
class note(Resource):
    @api.doc('get a note')
    @api.marshal_with(_note)
    def get(self, id):
        """get a note given its identifier"""
        note = get_a_note(id)
        if not note:
            api.abort(404)
        else:
            return note

    @api.response(200, 'customer successfully updated.')
    @api.doc('create or update customer')
    @api.marshal_with(_note)
    @api.expect(_note, validate=True)
    def put(self, id):
        """Creates or update a note """
        data = request.json
        data['id'] = id
        return upsert_note(data=data)

    @api.response(200, 'customer successfully deleted.')
    @api.doc('delete customer')
    def delete(self, id):
        """Delete a note """
        return delete_note(id)