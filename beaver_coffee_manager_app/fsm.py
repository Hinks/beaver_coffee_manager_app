from toolz.dicttoolz import assoc
from auth.auth import authenticate
import print_utils


def function_arity(fun):
    import inspect
    return len(inspect.getargspec(fun)[0])


def accept(app_data, key, db):
    """ Jumps to the next state that is specified in the rules from
    app_data['current_rules'] and runs the supplied function.
    """
    try:
        current_state = app_data['state']
        new_state = app_data['current_rules'][current_state][key].get('next_state')
        supplied_func = app_data['current_rules'][current_state][key].get('supplied_func')

        session = app_data['session']

        # Match what to do depending on the supplied function's arity
        #This matches the lambda function in the rules module
        if function_arity(supplied_func) is 0:
            supplied_func()
            return assoc(app_data, 'state', new_state)

        #This matches the print_utils.start_screen function in the rules module
        elif function_arity(supplied_func) == 1:
            supplied_func(session['logged_in_as'])()
            return assoc(app_data, 'state', new_state)

        #This matches the logout function in the rules module
        elif function_arity(supplied_func) == 2:
            return supplied_func(db, assoc(app_data, 'state', new_state))

        #This matches the buisness_logic function in the rules module
        elif function_arity(supplied_func) == 3:
            supplied_func(db, new_state, session)
            return assoc(app_data, 'state', new_state)

        # Just in case nothing matches, app_data is returned in the state it came in with.
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
