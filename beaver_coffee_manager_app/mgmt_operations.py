from pprint import pprint
import print_utils


def select_type_of_report(choice):
    import report.type
    reports = {
        '1': report.type.report_1,
        '2': report.type.report_2,
        '3': report.type.report_3,
        '4': report.type.report_4,
        '5': report.type.report_5,
        '6': report.type.report_6,
        '7': report.type.report_7
    }
    return reports[choice]


def make_report(db, shop_id):
    print_utils.report_instructions()

    choice = input('\nType the number of the action to perform: ') or '1'
    action = select_type_of_report(choice)
    report_result = action(db, shop_id)
    print(report_result)
    print_utils.instructions_after_made_report()


def select_employee_operation(choice):
    import cru.employee
    operations = {
        '1': cru.employee.create,
        '2': cru.employee.read,
        '3': cru.employee.update
    }
    return operations[choice]


def cru_employee(db, shop_id):
    print_utils.instructions_cru_employee()

    choice = input('\nType the number of the action to perform: ') or '1'
    action = select_employee_operation(choice)
    result = action(db, shop_id)
    print(result)
    print_utils.instructions_after_cru_employee()


def select_customer_operation(choice):
    import cru.customer
    operations = {
        '1': cru.customer.create,
        '2': cru.customer.read,
        '3': cru.customer.update
    }
    return operations[choice]


def cru_customer(db, shop_id):
    print_utils.instructions_cru_customer()

    choice = input('\nType the number of the action to perform: ') or '1'
    action = select_customer_operation(choice)
    result = action(db)
    print(result)
    print_utils.instructions_after_cru_customer()


def select_stock_operation(choice):
    import cru.stock
    operations = {
        '1': cru.stock.read,
        '2': cru.stock.update
    }
    return operations[choice]


def cru_stock(db, shop_id):
    print_utils.instructions_cru_stock()

    choice = input('\nType the number of the action to perform: ') or '1'
    action = select_stock_operation(choice)
    result = action(db, shop_id)
    pprint(result)
    print_utils.instructions_after_cru_stock()
