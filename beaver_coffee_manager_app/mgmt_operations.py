"""The purpose of this module is to supply functions that gets executed
at particular states in the finite-state-machine concerning buisness-logic
operations like creating statistics reports,
change employee/customer data and update stock quantities.
"""
from pprint import pprint
import print_utils

import statistics.reports
import cru.employee
import cru.customer
import cru.stock


BUISNESS_LOGIC_LAYER = {
    'statistics': {
        '1': statistics.reports.report_1,
        '2': statistics.reports.report_2,
        '3': statistics.reports.report_3,
        '4': statistics.reports.report_4,
        '5': statistics.reports.report_5,
        '6': statistics.reports.report_6,
        '7': statistics.reports.report_7
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


def function_arity(fun):
    import inspect
    return len(inspect.getargspec(fun)[0])


def buisness_logic(db, next_state, user_session):
    print_utils.bll_instructions(next_state)()

    buisness_logic_context = BUISNESS_LOGIC_LAYER.get(next_state, None)
    choice = input('\nType the number of the action to perform: ')
    context_operation = buisness_logic_context.get(choice, None)

    if context_operation:
        # Match what to do depending on the supplied function's arity
        #This matches the cru.customer functions in the buisness_logic_layer
        if function_arity(context_operation) is 1:
            result = context_operation(db)
            print(result)
            print_utils.instructions_after(next_state)()

        #This matches the functions in the buisness_logic_layer
        #
        elif function_arity(context_operation) is 2:
            result = context_operation(db, user_session['shop_id'])
            print(result)
            print_utils.instructions_after(next_state)()
    else:
        print(f'That context operation does not exist: {choice}')
        print_utils.instructions_after(next_state)()
