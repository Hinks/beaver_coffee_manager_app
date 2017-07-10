def branch_m_start_screen():
    msg = '\n{}\n{}\n{}\n{}\n{}\n{}'.format(
        '1. Generate Reports',
        '2. Create,Read,Update Employee data',
        '3. Create,Read,Update Customer data',
        '4. Create,Read,Update product stock quantities',
        '8. Logout',
        '9. Exit')
    print(msg)

def sales_m_start_screen():
    msg = '\n{}\n{}\n{}'.format(
        '1. Generate Reports',
        '8. Logout',
        '9. Exit')
    print(msg)

#---------------Print methods for mgnt-operations------------------
def report_instructions():
    instructions = '\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(
        '1. Sales for any specified time period',
        '2. Sales for of one or more products over a time period',
        '3. Sales per customer per city or occupation',
        '4. Stock quantities of a product for any specified time period',
        '5. Orders served by an employee for any specified time period',
        '6. Employees listing for any specified time period',
        '7. Customers listing for any specified time period')
    print(instructions)


def instructions_after_made_report():
    msg = '\n{}\n{}'.format(
        '1. Generate Reports',
        '2. Start screen')
    print(msg)


def instructions_cru_stock():
    msg = '\n{}\n{}'.format(
        '1. Read current stock',
        '2. Update existing product stock qty or add new product by inserting non existing sku')
    print(msg)


def instructions_after_cru_stock():
    msg = '\n{}\n{}'.format(
        '1. Create, Read, Update stock',
        '2. Start screen')
    print(msg)


def instructions_cru_employee():
    msg = '\n{}\n{}\n{}'.format(
        '1. Create new employee',
        '2. Read employee',
        '3. Update employee')
    print(msg)


def instructions_after_cru_employee():
    msg = '\n{}\n{}'.format(
        '1. Create, Read, Update employee',
        '2. Start screen')
    print(msg)


def instructions_cru_customer():
    msg = '\n{}\n{}\n{}'.format(
        '1. Create new customer',
        '2. Read customer',
        '3. Update customer')
    print(msg)


def instructions_after_cru_customer():
    msg = '\n{}\n{}'.format(
        '1. Create, Read, Update customer',
        '2. Start screen')
    print(msg)
