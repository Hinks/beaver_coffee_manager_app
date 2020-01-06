def start_screen(logged_in_as):
    screens = {
        'branch_manager': branch_m_start_screen,
        'sales_manager': sales_m_start_screen
    }
    return screens[logged_in_as]


def mgmt_instructions(next_state):
    instructions = {
        'statistics': instructions_statistics,
        'cru_employee': instructions_cru_employee,
        'cru_customer': instructions_cru_customer,
        'cru_stock': instructions_cru_stock
    }
    return instructions[next_state]


def instructions_after(next_state):
    instructions = {
        'statistics': instructions_after_statistics,
        'cru_employee': instructions_after_cru_employee,
        'cru_customer': instructions_after_cru_customer,
        'cru_stock': instructions_after_cru_stock
    }
    return instructions[next_state]


def branch_m_start_screen():
    msg = '\nBM: Start screen:\n{}\n{}\n{}\n{}\n{}\n{}'.format(
        '1. Generate Reports',
        '2. Create,Read,Update Employee data',
        '3. Create,Read,Update Customer data',
        '4. Create,Read,Update product stock quantities',
        '8. Logout',
        '9. Exit')
    print(msg)


def sales_m_start_screen():
    msg = '\nSM: Start screen:\n{}\n{}\n{}'.format(
        '1. Generate Reports',
        '8. Logout',
        '9. Exit')
    print(msg)


def instructions_statistics():
    instructions = '\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(
        '1. Sales for any specified time period',
        '2. Sales for of one or more products over a time period',
        '3. Sales per customer per city or occupation',
        '4. Stock quantities of a product for any specified time period',
        '5. Orders served by an employee for any specified time period',
        '6. Employees listing for any specified time period',
        '7. Customers listing for any specified time period')
    print(instructions)


def instructions_cru_employee():
    msg = '\n{}\n{}\n{}'.format(
        '1. Create new employee',
        '2. Read employee',
        '3. Update employee')
    print(msg)


def instructions_cru_customer():
    msg = '\n{}\n{}\n{}'.format(
        '1. Create new customer',
        '2. Read customer',
        '3. Update customer')
    print(msg)


def instructions_cru_stock():
    msg = '\n{}\n{}'.format(
        '1. Read current stock',
        '2. Update existing product stock qty or add new product by inserting non existing sku')
    print(msg)


def instructions_after_statistics():
    msg = '\n{}\n{}'.format(
        '1. Generate Reports',
        '2. Start screen')
    print(msg)


def instructions_after_cru_stock():
    msg = '\n{}\n{}'.format(
        '1. Create, Read, Update stock',
        '2. Start screen')
    print(msg)


def instructions_after_cru_employee():
    msg = '\n{}\n{}'.format(
        '1. Create, Read, Update employee',
        '2. Start screen')
    print(msg)


def instructions_after_cru_customer():
    msg = '\n{}\n{}'.format(
        '1. Create, Read, Update customer',
        '2. Start screen')
    print(msg)
