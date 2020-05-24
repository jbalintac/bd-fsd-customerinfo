# import uuid
import datetime, uuid

from flask import jsonify

from app.main import db
from app.main.model.customer import Customer


def upsert_customer(data):
    customer = None

    if 'id' in data and data['id'] != '00000000-0000-0000-0000-000000000000':
        customer = Customer.query.filter_by(id=data['id']).first()

    if not customer:
        new_customer = Customer(
            contact = data['contact'],
            name = data['name'],
            description = data['description'],
            created_date = datetime.datetime.utcnow(),
            status = data['status'][0].lower() + data['status'][1:]
        )
        save_changes(new_customer)
        return new_customer, 201
    else:
        customer.contact = data['contact']
        customer.name = data['name']
        customer.description = data['description']
        customer.status = data['status'][0].lower() + data['status'][1:]
        save_changes(customer)
        return customer, 200


def get_all_customers():
    return Customer.query.all()


def get_a_customer(id):
    return Customer.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
