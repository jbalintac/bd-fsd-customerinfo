from flask import request
from flask_restplus import Resource
from flask_cors import cross_origin

from ..util.dto import CustomerDto
from ..service.customer_service import upsert_customer, get_all_customers, get_a_customer

api = CustomerDto.api
_customer_req = CustomerDto.customer_req
_customer_res = CustomerDto.customer_res


@api.route('/')
class customerList(Resource):
    @api.doc('list_of_registered_customers')
    @api.marshal_list_with(_customer_res)
    def get(self):
        """List all registered customers"""
        return get_all_customers()

    @api.response(201, 'customer successfully created.')
    @api.doc('create or update customer')
    @api.marshal_with(_customer_res)
    @api.expect(_customer_req, validate=True)
    def post(self):
        """Creates or update customer """
        data = request.json
        return upsert_customer(data=data)


@api.route('/<id>')
@api.param('id', 'The customer identifier')
@api.response(404, 'customer not found.')
class customer(Resource):
    @api.doc('get a customer')
    @api.marshal_with(_customer_res)
    def get(self, id):
        """get a customer given its identifier"""
        customer = get_a_customer(id)
        if not customer:
            api.abort(404)
        else:
            return customer

    @api.response(200, 'customer successfully updated.')
    @api.doc('create or update customer')
    @api.marshal_with(_customer_res)
    @api.expect(_customer_req, validate=True)
    def put(self, id):
        """Creates or update customer """
        data = request.json
        data['id'] = id
        return upsert_customer(data=data)