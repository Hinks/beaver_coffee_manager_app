from mgmt_operations import (buisness_logic)
import print_utils
from auth.auth import logout


BRANCH_MGMT_TRANSITIONS = {
    'start_screen': {'1': {'next_state': 'statistics',   'supplied_func': ('mgmt_operation', buisness_logic)},
                     '2': {'next_state': 'cru_employee', 'supplied_func': ('mgmt_operation', buisness_logic)},
                     '3': {'next_state': 'cru_customer', 'supplied_func': ('mgmt_operation', buisness_logic)},
                     '4': {'next_state': 'cru_stock',    'supplied_func': ('mgmt_operation', buisness_logic)},
                     '8': {'next_state': 'start_screen', 'supplied_func': ('unauth', logout)},
                     '9': {'next_state': 'exit',         'supplied_func': ('exit_app',)}
                     },

    'statistics': {'1': {'next_state': 'statistics',    'supplied_func': ('mgmt_operation', buisness_logic)},
                    '2': {'next_state': 'start_screen',   'supplied_func': ('print_start_screen', print_utils.start_screen)}
                    },

    'cru_employee': {'1': {'next_state': 'cru_employee', 'supplied_func': ('mgmt_operation', buisness_logic)},
                     '2': {'next_state': 'start_screen', 'supplied_func': ('print_start_screen', print_utils.start_screen)}
                     },

    'cru_customer': {'1': {'next_state': 'cru_customer', 'supplied_func': ('mgmt_operation', buisness_logic)},
                     '2': {'next_state': 'start_screen', 'supplied_func': ('print_start_screen', print_utils.start_screen)}
                     },

    'cru_stock': {'1': {'next_state': 'cru_stock',    'supplied_func': ('mgmt_operation', buisness_logic)},
                  '2': {'next_state': 'start_screen', 'supplied_func': ('print_start_screen', print_utils.start_screen)}
                  }
}


SALES_MGMT_TRANSITIONS = {
    'start_screen': {'1': {'next_state': 'statistics',   'supplied_func': ('mgmt_operation', buisness_logic)},
                     '8': {'next_state': 'start_screen', 'supplied_func': ('unauth', logout)},
                     '9': {'next_state': 'exit',         'supplied_func': ('exit_app',)}
                     },

    'statistics': {'1': {'next_state': 'statistics',    'supplied_func': ('mgmt_operation', buisness_logic)},
                   '2': {'next_state': 'start_screen',  'supplied_func': ('print_start_screen', print_utils.start_screen)}
                   }
}


default_app_data = {
    'current_rules': None,
    'branch_mgmt_rules': BRANCH_MGMT_TRANSITIONS,
    'sales_mgmt_rules': SALES_MGMT_TRANSITIONS,
    'state': 'start_screen',
    'session': {
        'is_authenticated': False,
        'logged_in_as': None,
        'shop_id': None
    }
}
