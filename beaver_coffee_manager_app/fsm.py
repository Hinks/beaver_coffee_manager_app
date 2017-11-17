from toolz.dicttoolz import assoc
from auth.auth import authenticate
import print_utils


def accept(app_data, key, db):
    """ Jumps to the next state that is specified in the rules from
    app_data['current_rules'] and runs the supplied function.
    """
    try:
        current_state = app_data['state']
        next_state = app_data['current_rules'][current_state][key].get('next_state')

        supplied_state_func = app_data['current_rules'][current_state][key].get('supplied_func')
        func_description = supplied_state_func[0]

        session = app_data['session']

        if func_description == 'exit_app':
            # Returns appdata with the state-field set to exit, which will exit
            # the application inside the run-next function.
            return assoc(app_data, 'state', next_state)

        elif func_description == 'print_start_screen':
            print_func = supplied_state_func[1]
            print_func(session['logged_in_as'])()
            return assoc(app_data, 'state', next_state)

        elif func_description == 'unauth':
            logout_func = supplied_state_func[1]
            #Returns a new app_data with rules removed.
            return logout_func(db, assoc(app_data, 'state', next_state))

        elif func_description == 'mgmt_operation':
            buisness_operation = supplied_state_func[1]
            buisness_operation(db, next_state, session)
            return assoc(app_data, 'state', next_state)
        else:
            return app_data
    except KeyError as e:
        print(f'{key} is not a valid option.')
        print_utils.start_screen(app_data['session']['logged_in_as'])()
        return  assoc(app_data, 'state', 'start_screen')


def run_next(db, app_data):
    """ This is the application loop. It stops and closes the db connection
    then the state is set to: exit. The user has to sign in before he/she can enter
    the "finite state machine".
    """
    if app_data['state'] == 'exit':
        db.client.close()
        print('db-connection closed')
        raise SystemExit
    elif app_data['session']['is_authenticated'] == False:
        run_next(db, authenticate(db, app_data))
    else:
        key = input() or '1'
        run_next(db, accept(app_data, key, db))
