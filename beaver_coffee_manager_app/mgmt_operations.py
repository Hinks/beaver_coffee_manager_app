"""The purpose of this module is to supply functions that gets executed
at particular states in the finite-state-machine concerning buisness-logic
operations like creating statistics reports,
change employee/customer data and update stock quantities.
"""
from pprint import pprint
import print_utils

import report.type
import cru.employee
import cru.customer
import cru.stock


BUISNESS_LOGIC_LAYER = {
    'report_operations': {
        '1': report.type.report_1,
        '2': report.type.report_2,
        '3': report.type.report_3,
        '4': report.type.report_4,
        '5': report.type.report_5,
        '6': report.type.report_6,
        '7': report.type.report_7
    },
    'cru_employee': {
        '1': cru.employee.create,
        '2': cru.employee.read,
        '3': cru.employee.update
    },
    'cru_customer': {
        '1': cru.customer.create,
        '2': cru.customer.read,
        '3': cru.customer.update
    },
    'cru_stock': {
        '1': cru.stock.read,
        '2': cru.stock.update
    }
}


def make_report(db, shop_id):
    print_utils.report_instructions()

    buisness_logic_context = BUISNESS_LOGIC_LAYER.get('report_operations', None)
    choice = input('\nType the number of the action to perform: ')
    context_operation = buisness_logic_context.get(choice, None)

    if context_operation:
        statistics_report = context_operation(db, shop_id)
        print(statistics_report)
        print_utils.instructions_after_made_report()
    else:
        print(f'That context operation does not exist: {choice}')
        print_utils.instructions_after_made_report()


def cru_employee(db, shop_id):
    print_utils.instructions_cru_employee()

    buisness_logic_context = BUISNESS_LOGIC_LAYER.get('cru_employee', None)
    choice = input('\nType the number of the action to perform: ')
    context_operation = buisness_logic_context.get(choice, None)

    if context_operation:
        response = context_operation(db, shop_id)
        print(response)
        print_utils.instructions_after_cru_employee()
    else:
        print(f'That context operation does not exist: {choice}')
        print_utils.instructions_after_cru_employee()


def cru_customer(db, shop_id):
    print_utils.instructions_cru_customer()

    buisness_logic_context = BUISNESS_LOGIC_LAYER.get('cru_customer', None)
    choice = input('\nType the number of the action to perform: ')
    context_operation = buisness_logic_context.get(choice, None)

    if context_operation:
        response = context_operation(db)
        print(response)
        print_utils.instructions_after_cru_customer()
    else:
        print(f'That context operation does not exist: {choice}')
        print_utils.instructions_after_cru_customer()

def cru_stock(db, shop_id):
    print_utils.instructions_cru_stock()

    buisness_logic_context = BUISNESS_LOGIC_LAYER.get('cru_stock', None)
    choice = input('\nType the number of the action to perform: ')
    context_operation = buisness_logic_context.get(choice, None)

    if context_operation:
        response = context_operation(db, shop_id)
        print(response)
        print_utils.instructions_after_cru_stock()
    else:
        print(f'That context operation does not exist: {choice}')
        print_utils.instructions_after_cru_stock()
