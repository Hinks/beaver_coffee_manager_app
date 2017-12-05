from datetime import datetime
from functools import reduce
from statistics.build_result import (
    report_5_string,
    report_6_string,
    report_7_string)

from statistics.queries import (
    sales_all_products_by_dates,
    sales_choosen_products_by_dates,
    avg_sales_per_customer_per_city,
    stock_quantities_by_dates,
    orders_served_by_employee,
    list_employees_by_dates,
    list_customer_by_dates)


def product_sales(db, shop_id):
    date1_str, date2_str = enter_time_period()
    cursor = sales_all_products_by_dates(db, shop_id, time_period(date1_str, date2_str))

    title = f'---------Report---------\nProducts sold between {date1_str} and {date2_str}\n'
    ending = '\n---------End---------'
    product_sold_total_times = lambda acc, item: acc + '\n{0:25} amount: {1}'.format(item['name'], item['count'])
    statistic_string = reduce(product_sold_total_times, cursor, title) + ending

    return statistic_string


def specific_product_sales(db, shop_id):
    date1_str, date2_str = enter_time_period()
    skus_string = input('select products by sku, format: 1001, 1002: ')
    sku_list = unpack_sku_list(skus_string)
    cursor = sales_choosen_products_by_dates(db, shop_id, sku_list, time_period(date1_str, date2_str))

    title = f'---------Report---------\nProducts:{skus_string} sold between {date1_str} and {date2_str}\n'
    ending = '\n---------End---------'
    product_sold_total_times = lambda acc, item: acc + '\n{0:25} amount: {1}'.format(item['name'], item['count'])
    statistic_string = reduce(product_sold_total_times, cursor, title) + ending

    return statistic_string


def avg_sales_per_city(db, shop_id):
    cursor = avg_sales_per_customer_per_city(db, shop_id)

    title = f'---------Report---------\nAverage sales per customer per city\n'
    ending = '\n---------End---------'
    avg_sales_per_city = lambda acc, item: acc + '\n{0:10} amount: {1}'.format(item['_id'], item['avg_sales_per_customer'])
    statistic_string = reduce(avg_sales_per_city, cursor, title) + ending

    return statistic_string


def stock_quantities(db, shop_id):
    date1_str, date2_str = enter_time_period()
    cursor = stock_quantities_by_dates(db, shop_id, time_period(date1_str, date2_str))

    title = ('---------Report---------\n'
            f'Stock quantities between {date1_str} and {date2_str}\n')

    stock = lambda x: reduce(lambda acc, prod: acc + '\nsku: {0:6} qty: {1:5}'.format(prod[0], prod[1]), x, '')
    fun = lambda acc, x: acc + '\n\ndate: {0:10} \n {1}'.format(x['date'].strftime("%Y-%m-%d"), stock(list(x['stock_quantities'].items())))
    result = reduce(fun, cursor, title)
    return result + '\n---------End---------'


def serverd_orders_employee(db, shop_id):
    employee_id = input('Enter id for employee: ')
    date1_str, date2_str = enter_time_period()

    cursor = orders_served_by_employee(db, shop_id, employee_id, time_period(date1_str, date2_str))
    result = report_5_string(cursor, date1_str, date2_str)
    return result


def employee_listing(db, shop_id):
    date1_str, date2_str = enter_time_period()
    cursor = list_employees_by_dates(db, shop_id, time_period(date1_str, date2_str))
    result = report_6_string(cursor, date1_str, date2_str)
    return result

def customer_listing(db, shop_id):
    date1_str, date2_str = enter_time_period()
    cursor = list_customer_by_dates(db, shop_id, time_period(date1_str, date2_str))
    result = report_7_string(cursor, date1_str, date2_str)
    return result


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
