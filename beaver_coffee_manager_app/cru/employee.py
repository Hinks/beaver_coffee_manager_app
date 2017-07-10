from bson.objectid import ObjectId
from toolz.dicttoolz import assoc
import json
import datetime

def create(db, shop_id):
    new_employee = create_employee(shop_id)
    return db.employees.insert_one(new_employee)


def create_employee(shop_id):
    name = input('Enter name: ')
    ssn = input('Enter ssn: ')
    emp_document = {
        'name': name,
        'ssn': ssn,
        'work_in_shop': shop_id,
        'entry_date': datetime.datetime.utcnow(),
        'employment_history': [],
        'comments': []
    }
    return emp_document


def read(db, shop_id):
    emp_id_str = input('Enter id for employee to read: ')
    emp_id = ObjectId(emp_id_str)
    emp = db.employees.find_one({'_id': emp_id, 'work_in_shop': shop_id})

    if emp:
        return employee_info_str(emp)
    else:
        return 'No found employee with that id, works here.'


def employee_info_str(emp):
    info_str = '\
    \nid: {0}\
    \nname: {1}\
    \nssn: {2}\
    \nentry date: {3}\
    '.format(
        emp['_id'],
        emp['name'],
        emp['ssn'],
        emp['entry_date'].strftime("%Y-%m-%d"))
    return info_str


def update(db, shop_id):
    emp_id_str = input('Enter id for employee to read: ')
    emp_id = ObjectId(emp_id_str)

    instruction_str = 'Enter a json string to update or create new keys/values.\n \
    Use: \" to surround key-names and string-values\n \
    Example: {"name": "new name"}:\n'

    json_input= input(instruction_str)

    try:
        new_emp_data = contains_entry_date(json.loads(json_input))
        db.employees.update({'_id': emp_id}, {'$set': new_emp_data})
        return 'Employee update successful'
    except json.JSONDecodeError as e:
        return 'Invalid json string, nothing is changed'


def contains_entry_date(input_json_dict):
    if 'entry_date' in input_json_dict:
        y, m, d = input_json_dict['entry_date'].split('-')
        return assoc(input_json_dict, 'entry_date', datetime.datetime(int(y), int(m), int(d)))
    else:
        return input_json_dict
