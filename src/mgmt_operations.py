from pprint import pprint
import print_utils

import statistics.reports
import cru.employee
import cru.customer
import cru.stock


MGMT_OPERATIONS = {
    'statistics': {
        '1': statistics.reports.product_sales,
        '2': statistics.reports.specific_product_sales,
        '3': statistics.reports.avg_sales_per_city,
        '4': statistics.reports.stock_quantities,
        '5': statistics.reports.serverd_orders_employee,
        '6': statistics.reports.employee_listing,
        '7': statistics.reports.customer_listing
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

def select_mgmt_operation(db, next_state, user_session):
    print_utils.mgmt_instructions(next_state)()

    buisness_logic_context = MGMT_OPERATIONS.get(next_state, None)
    choice = input('\nType the number of the action to perform: ')

    try:
        context_operation = buisness_logic_context[choice]

        if next_state == 'statistics' or 'cru_employee' or 'cru_customer':
            result = context_operation(db, user_session['shop_id'])
            print(result)
            print_utils.instructions_after(next_state)()
        elif next_state == 'cru_stock':
            result = context_operation(db)
            print(result)
            print_utils.instructions_after(next_state)()
    except KeyError as e:
        print(f'Operation: {choice} does not exist:')
        print_utils.instructions_after(next_state)()
