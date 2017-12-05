

def report_4_string(cursor, date1_str, date2_str):
    result = f'---------Report---------\nStock quantities between {date1_str} and {date2_str}\n'
    for item in cursor:
        date = item['date']
        stock_quantities = item['stock_quantities']

        stock_quantities_string = ''
        for k,v in stock_quantities.items():
            item_str = '\nsku: {0:6} qty: {1:5}'.format(k, v)
            stock_quantities_string += item_str

        item_str = '\n\ndate: {0:10} \n {1}'.format(date.strftime("%Y-%m-%d"), stock_quantities_string)
        result += item_str

    return result + '\n---------End---------'


def report_5_string(cursor, date1_str, date2_str):
    result = f'---------Report---------\nOrders served by employee between {date1_str} and {date2_str}\n'
    for item in cursor:
        amount = item['amount']
        order_ids = item['served_orders']

        serverd_order_ids_string = ''.join('\n' + str(id) for id in order_ids)

        item_str = 'Orders served: {0}.\nOrder ids:{1} '.format(amount, serverd_order_ids_string)
        result += item_str

    return result + '\n---------End---------'


def report_6_string(cursor, date1_str, date2_str):
    result = f'---------Report---------\nEmployees listing for shop, between {date1_str} and {date2_str}\n'
    for employee in cursor:
        ssn = employee['ssn'],
        name = employee['name'],
        entry_date = employee['entry_date']

        item_str = '\nssn: {0}\nname: {1}\nStarted to work: {2}\n'.format(ssn, name, entry_date)
        result += item_str

    return result + '\n---------End---------'


def report_7_string(cursor, date1_str, date2_str):
    result = f'---------Report---------\nActive buying customers at the shop between {date1_str} and {date2_str}\n'
    result = result + 'Listing of customers id:'
    for item in cursor:
        customer_id = item['_id']
        item_str = '\n{0}'.format(customer_id)
        result += item_str

    return result + '\n---------End---------'
