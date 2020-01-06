import pprint
from toolz.dicttoolz import assoc
from toolz.functoolz import pipe
import print_utils

def authenticate(db, app_data):
    login_as = input('1. Login as Branch Manager \n2. Login as Sales Manager\n') or '1'
    if login_as == '1':
        return branch_manager_login(db, app_data)
    elif login_as == '2':
        return sales_manager_login(db, app_data)
    else:
        print(f'{login_as} is not an option! try again.')
        return app_data


def branch_manager_login(db, app_data):
    ssn = input('authenticate with your ssn: ')
    branch_manager = db.branch_managers.find_one({'ssn': ssn})

    if branch_manager:
        new_app_data = pipe(app_data,
            update_current_rules('branch_mgmt_rules'),
            validate_session(branch_manager['shop_id'], 'branch_manager'))

        print('You logged-in successfully as Branch Manager')
        print_utils.branch_m_start_screen()

        return new_app_data
    else:
        print('Check your ssn, and try again.')
        return app_data


def sales_manager_login(db, app_data):
    ssn = input('authenticate with your ssn: ')
    sales_manager = db.sales_managers.find_one({'ssn': ssn})

    if sales_manager:

        shops = list(fetch_shops(db))
        print_shops(shops)
        shop = select_shop(shops)

        new_app_data = pipe(app_data,
            update_current_rules('sales_mgmt_rules'),
            validate_session(shop['_id'], 'sales_manager'))

        print('You logged-in successfully as Sales Manager')
        print_utils.sales_m_start_screen()

        return new_app_data
    else:
        print('Check your ssn, and try again.')
        return app_data


def logout(db, app_data):
    new_app_data = pipe(app_data,
        # NoneExistingRules doesn't exist as a field in appdata and will because
        # of that return None. So the current_rules field in appdata will be set
        # to None.
        update_current_rules('NoneExistingRules'),
        clear_session)

    print('you logged out')
    return new_app_data


def update_current_rules(mgmt_rules):
    return lambda app_data: assoc(app_data, 'current_rules', app_data.get(mgmt_rules, None))


def validate_session(shop_id, logged_in_as):
    return lambda app_data: assoc(app_data, 'session',
    {'is_authenticated': True, 'logged_in_as': logged_in_as, 'shop_id': shop_id})


def clear_session(app_data):
    return assoc(app_data, 'session',
    {'is_authenticated': False, 'logged_in_as': None, 'shop_id': None})


def fetch_shops(db):
    return db.shops.find()


def select_shop(shops):
    index = input('Select shop by index')
    return shops[int(index)]


def print_shops(shops):
    for index, shop in enumerate(list(shops)):
        item_str = '{}. country: {}, city: {}, street: {}'.format(index, shop['country'], shop['city'], shop['street'])
        print(item_str)
