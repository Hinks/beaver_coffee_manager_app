from bson.objectid import ObjectId
from toolz.dicttoolz import assoc
from random import randint
import json
import datetime

def create(db, shop_id):
    new_customer = create_customer()
    return db.reg_customers.insert_one(new_customer)


def create_customer():
    ssn = input('Enter ssn: ')
    occupation = input('Enter occupation: ') or 'no_work'
    country = input('Enter country: ') or 'no_country'
    city = input('Enter city: ') or 'no city'
    postal_code = input('Enter postal_code: ') or '00000'
    customer_document = {
        'ssn': ssn,
        'occupation': occupation,
        'personal_card': {
            'code': ''.join([f'{randint(0, 9)}' for num in range(0, 9)]),
            'country': country
        },
        'address': {
            'country': country,
            'city': city,
            'postal_code': postal_code
        },
        'entry_date': datetime.datetime.utcnow(),
    }
    return customer_document


def read(db, shop_id):
    customer_id_str = input('Enter id for customer to read: ')
    customer_id = ObjectId(customer_id_str)
    customer = db.reg_customers.find_one({'_id': customer_id})

    if customer:
        return customer_info_str(customer)
    else:
        return 'No found customer with that id'


def customer_info_str(customer):
    info_str = '\nCusotmer Info:\
    \nssn: {0}\
    \noccupation: {1}\
    \naddress: {2}\
    \npersonal_card: {3}\
    \nentry date: {4}\
    '.format(
        customer['ssn'],
        customer['occupation'],
        customer['address'],
        customer['personal_card'],
        customer['entry_date'].strftime("%Y-%m-%d"))
    return info_str


def update(db, shop_id):
    customer_id_str = input('Enter id for customer to read: ')
    customer_id = ObjectId(customer_id_str)

    instruction_str = 'Enter a json string to update or create new keys/values.\n \
    Use: \" to surround key-names and string-values\n \
    Example: {"key": "stringvalue"}:\n'

    json_input= input(instruction_str)

    try:
        new_customer_data = contains_entry_date(json.loads(json_input))
        db.reg_customers.update({'_id': customer_id}, {'$set': new_customer_data})
        return 'Customer update successful'
    except json.JSONDecodeError as e:
        return 'Invalid json string, nothing is changed'


def contains_entry_date(input_json_dict):
    if 'entry_date' in input_json_dict:
        y, m, d = input_json_dict['entry_date'].split('-')
        return assoc(input_json_dict, 'entry_date', datetime.datetime(int(y), int(m), int(d)))
    else:
        return input_json_dict
