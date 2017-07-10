from toolz.dicttoolz import assoc
from auth.auth import authenticate


def function_arity(fun):
    import inspect
    return len(inspect.getargspec(fun)[0])


def accept(app_data, key, db):
    """ Jumps to the next state that is specified in the rules from
    app_data['current_rules'] and runs the supplied function.
    """

    current_state = app_data['state']
    new_state = app_data['current_rules'][current_state][key].get('next_state')
    supplied_func = app_data['current_rules'][current_state][key].get('supplied_func')

    session = app_data['session']

    # Match what to do depending on the supplied function's arity

    # If the supplied function has zero argument, the function(usually a print method)
    # is called before returning the app_data with the next state set.
    if function_arity(supplied_func) == 0:
        supplied_func()
        return assoc(app_data, 'state', new_state)
    # If the supplied function has one argument, the app_data gets updated by the
    # supplied function and then returned. This match is only matched when the user
    # logs out and then the supplied logout function clear the session in app_data.
    elif function_arity(supplied_func) == 1:
        return supplied_func(assoc(app_data, 'state', new_state))
    # If the supplied function has two arguments, the mgmt operations are called.
    # They expect the db connection as the first argument and the shop_id as the
    # second.
    elif function_arity(supplied_func) == 2:
        supplied_func(db, session.get('shop_id'))
        return assoc(app_data, 'state', new_state)
    # Just in case nothing matches, app_data is returned in the state it came in with.
    else:
        return app_data


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
