from datetime import datetime
from report.build_result import (report_1_string, report_3_string, report_4_string, report_5_string,
report_6_string, report_7_string)
from report.queries import (sales_all_products_by_dates,
                            sales_choosen_products_by_dates,
                            avg_sales_per_customer_per_city,
                            stock_quantities_by_dates,
                            orders_served_by_employee,
                            list_employees_by_dates,
                            list_customer_by_dates)


def report_1(db, shop_id):
    date1_str, date2_str = enter_time_period()
    cursor = sales_all_products_by_dates(db, shop_id, time_period(date1_str, date2_str))

    result = report_1_string(cursor, date1_str, date2_str)
    return result


def report_2(db, shop_id):
    date1_str, date2_str = enter_time_period()
    skus_string = input('select products by sku, format: 1001, 1002: ')
    sku_list = unpack_sku_list(skus_string)
    cursor = sales_choosen_products_by_dates(db, shop_id, sku_list, time_period(date1_str, date2_str))

    result = report_1_string(cursor, date1_str, date2_str)
    return result


def report_3(db, shop_id):
    cursor = avg_sales_per_customer_per_city(db, shop_id)
    result = report_3_string(cursor)
    return result


def report_4(db, shop_id):
    date1_str, date2_str = enter_time_period()
    cursor = stock_quantities_by_dates(db, shop_id, time_period(date1_str, date2_str))
    result = report_4_string(cursor, date1_str, date2_str)
    return result


def report_5(db, shop_id):
    #pmela id: 59410e4aa81610932dc471c1
    employee_id = input('Enter id for employee: ')
    date1_str, date2_str = enter_time_period()

    cursor = orders_served_by_employee(db, shop_id, employee_id, time_period(date1_str, date2_str))
    result = report_5_string(cursor, date1_str, date2_str)
    return result


def report_6(db, shop_id):
    date1_str, date2_str = enter_time_period()
    cursor = list_employees_by_dates(db, shop_id, time_period(date1_str, date2_str))
    result = report_6_string(cursor, date1_str, date2_str)
    return result

def report_7(db, shop_id):
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
