from datetime import datetime
from functools import reduce

from statistics.queries import (
    sales_all_products_by_dates,
    sales_choosen_products_by_dates,
    avg_sales_per_customer_per_city,
    stock_quantities_by_dates,
    orders_served_by_employee,
    list_employees_by_dates,
    list_customer_by_dates)


def build_report(title, reduce_fn, cursor ):
    full_title = f'---------Report---------\n{title}\n'
    content = reduce(reduce_fn, cursor, "")
    report_end = '\n---------End---------'
    return full_title + content + report_end

def product_sales(db, shop_id):
    date1_str, date2_str = enter_time_period()
    cursor = sales_all_products_by_dates(db, shop_id, time_period(date1_str, date2_str))

    title = f'Products sold between {date1_str} and {date2_str}'

    def total_sales(acc, current_element):
        width = 25
        product_name = current_element['name']
        total_sale = current_element['count']
        return acc + f'{product_name:{width}} amount: {total_sale} \n'

    return build_report(title=title, reduce_fn=total_sales, cursor=cursor)

def specific_product_sales(db, shop_id):
    date1_str, date2_str = enter_time_period()
    skus_string = input('select products by sku, format: 1001, 1002: ')
    sku_list = unpack_sku_list(skus_string)
    cursor = sales_choosen_products_by_dates(db, shop_id, sku_list, time_period(date1_str, date2_str))

    title = f'Products:{skus_string} sold between {date1_str} and {date2_str}'
    def total_sales(acc, current_element):
        width = 25
        product_name = current_element['name']
        total_sale = current_element['count']
        return acc + f'{product_name:{width}} amount: {total_sale} \n'

    return build_report(title=title, reduce_fn=total_sales, cursor=cursor)

def avg_sales_per_city(db, shop_id):
    cursor = avg_sales_per_customer_per_city(db, shop_id)

    title = f'Average sales per customer per city'
    def avg_sales_city(acc, current_element):
        #'\n{0:10} amount: {1}'.format(item['_id'], item['avg_sales_per_customer'])
        width = 10
        sku = current_element['_id']
        avg_sale = current_element['avg_sales_per_customer']
        return acc + f'{sku:{width}} amount: {avg_sale} \n'

    return build_report(title=title, reduce_fn=avg_sales_city, cursor=cursor)


def stock_quantities(db, shop_id):
    date1_str, date2_str = enter_time_period()
    cursor = stock_quantities_by_dates(db, shop_id, time_period(date1_str, date2_str))

    title = f'Stock quantities between {date1_str} and {date2_str}'

    def stock_values_by_day(stock_values):
        def build(acc, sku_and_qty):
            sku = sku_and_qty[0]
            qty = sku_and_qty[1]
            sku_width = 6
            qty_width = 5
            return acc + f'sku: {sku:{sku_width}} qty: {qty:{qty_width}}\n'

        return reduce(build, stock_values, '')

    def stock_values_full_history(acc, day_stock_values_doc):
        date_width = 10
        date_str = day_stock_values_doc['date'].strftime("%Y-%m-%d")
        stock_values = day_stock_values_doc['stock_quantities'].items()
        date_stock_values_str = stock_values_by_day(list(stock_values))
        return acc + '\n\n' + f'date: {date_str:{date_width}}\n{date_stock_values_str}'


    return build_report(title=title, reduce_fn=stock_values_full_history, cursor=cursor)


def serverd_orders_employee(db, shop_id):
    employee_id = input('Enter id for employee: ')
    date1_str, date2_str = enter_time_period()

    cursor = orders_served_by_employee(db, shop_id, employee_id, time_period(date1_str, date2_str))

    title = f'Orders served by employee between {date1_str} and {date2_str}'

    def served_orders(order_ids):
        def build(acc, order_id):
            order_id_str = str(order_id)
            return acc + f'\n{order_id_str}'

        return reduce(build, order_ids, '')

    def orders_by_employee_string(acc, current_element):
        total_served = current_element['amount']
        orders = served_orders(current_element['served_orders'])
        return acc + f'Orders served: {total_served}.\nOrder ids:{orders} '


    return build_report(title=title, reduce_fn=orders_by_employee_string, cursor=cursor)


def employee_listing(db, shop_id):
    date1_str, date2_str = enter_time_period()
    cursor = list_employees_by_dates(db, shop_id, time_period(date1_str, date2_str))

    title = f'Employees listing for shop, between {date1_str} and {date2_str}'

    def empoyee_list(acc, current_element):
        ssn = current_element['ssn']
        name = current_element['name']
        entry_date = current_element['entry_date']
        return acc + f'\nssn: {ssn}\nname: {name}\nstarted to work: {entry_date}\n'

    return build_report(title=title, reduce_fn=empoyee_list, cursor=cursor)


def customer_listing(db, shop_id):
    date1_str, date2_str = enter_time_period()
    cursor = list_customer_by_dates(db, shop_id, time_period(date1_str, date2_str))

    title = f'Active buying customers at the shop between {date1_str} and {date2_str} \nListing of customers id:'

    def customer_list(acc, current_element):
        cust_id = current_element['_id']
        return acc + f'{cust_id}\n'

    return build_report(title=title, reduce_fn=customer_list, cursor=cursor)


def time_period(start_date_str, end_date_str):
    start_date = convert_to_datetime(start_date_str)
    end_date   = convert_to_datetime(end_date_str)
    return (start_date, end_date)


def convert_to_datetime(date_str):
    year, month, day = map(int, date_str.split('-'))
    return datetime(year, month, day)


def unpack_sku_list(skus_str):
    convert_to_sku_dict = lambda sku: {'order_items.sku': sku.strip()}
    skus = map(convert_to_sku_dict, skus_str.split(','))
    return list(skus)


def enter_time_period():
    default_start_date = '2000-1-1'
    default_end_date='2020-1-1'

    input_date1 = input('Enter start date, format: yyyy-m-d: ')
    input_date2 = input('Enter end date, format: yyyy-m-d: ')

    if len(input_date1.split('-')) == 3 and len(input_date2.split('-')) == 3:
        return (input_date1, input_date2)
    else:
        return (default_start_date, default_end_date)
