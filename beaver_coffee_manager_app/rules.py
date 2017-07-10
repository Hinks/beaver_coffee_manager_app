from mgmt_operations import (make_report, cru_employee, cru_customer, cru_stock)
import print_utils
from auth.auth import logout


BRANCH_MGMT_TRANSITIONS = {
    'start_screen': {'1': {'next_state': 'reports_mod',  'supplied_func': make_report},
                     '2': {'next_state': 'employee_mod', 'supplied_func': cru_employee},
                     '3': {'next_state': 'customer_mod', 'supplied_func': cru_customer},
                     '4': {'next_state': 'stock_mod',    'supplied_func': cru_stock},
                     '8': {'next_state': 'start_screen', 'supplied_func': logout},
                     '9': {'next_state': 'exit',         'supplied_func': lambda: True}
                     },

    'reports_mod': {'1': {'next_state': 'reports_mod',    'supplied_func': make_report},
                    '2': {'next_state': 'start_screen',   'supplied_func': print_utils.branch_m_start_screen}
                    },

    'employee_mod': {'1': {'next_state': 'employee_mod', 'supplied_func': cru_employee},
                     '2': {'next_state': 'start_screen', 'supplied_func': print_utils.branch_m_start_screen}
                     },

    'customer_mod': {'1': {'next_state': 'customer_mod', 'supplied_func': cru_customer},
                     '2': {'next_state': 'start_screen', 'supplied_func': print_utils.branch_m_start_screen}
                     },

    'stock_mod': {'1': {'next_state': 'stock_mod',    'supplied_func': cru_stock},
                  '2': {'next_state': 'start_screen', 'supplied_func': print_utils.branch_m_start_screen}
                  }
}


SALES_MGMT_TRANSITIONS = {
    'start_screen': {'1': {'next_state': 'reports_mod',  'supplied_func': make_report},
                     '8': {'next_state': 'start_screen', 'supplied_func': logout},
                     '9': {'next_state': 'exit',         'supplied_func': lambda: True}
                     },

    'reports_mod': {'1': {'next_state': 'reports_mod',    'supplied_func': make_report},
                    '2': {'next_state': 'start_screen',   'supplied_func': print_utils.sales_m_start_screen}
                    }
}


default_app_data = {
    'current_rules': None,
    'branch_mgmt_rules': BRANCH_MGMT_TRANSITIONS,
    'sales_mgmt_rules': SALES_MGMT_TRANSITIONS,
    'state': 'start_screen',
    'session': {'is_authenticated': False, 'shop_id': None}
}
