from flask_restplus import Namespace, fields

class EnumValue(fields.Raw):
    def format(self, value):
        return value.name[0].upper() + value.name[1:]

class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer_req = api.model('customer', {
        'contact': fields.String(description='customer contact'),
        'name': fields.String(description='customer name'),
        'description': fields.String(description='customer description'),
        'id': fields.String(description='customer identifier'),
        'status': fields.String(description='customer status')
    })
    customer_res = api.model('customer', {
        'contact': fields.String(description='customer contact'),
        'name': fields.String(description='customer name'),
        'description': fields.String(description='customer description'),
        'id': fields.String(description='customer identifier'),
        'status': EnumValue(description='customer status'),
        'created_date': fields.DateTime(description='customer date creation'),
        'notes': fields.List(fields.Nested({
            'id': fields.String(description='note identifier'),
            'customer_id': fields.String(description='parent customer id'),
            'value': fields.String(description='note description'),
        })),
    })

class NoteDto:
    api = Namespace('note', description='note related operations')
    note = api.model('note', {
        'id': fields.String(description='note identifier'),
        'customer_id': fields.String(description='parent customer id'),
        'value': fields.String(description='note description'),
    })