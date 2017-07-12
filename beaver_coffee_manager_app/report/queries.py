from bson.objectid import ObjectId
from bson.son import SON

def sales_all_products_by_dates(db, shop_id, time_period):
    pipeline = [
        {'$match': {'$and': [
            {'shop_id': shop_id},
            {'state': 'finished'},
            {'entry_date': {'$gte': time_period[0]}},
            {'entry_date': {'$lte': time_period[1]}}
        ]
        }
        },
        {'$project': {'_id': 0, 'order_items': 1}},
        {'$unwind': '$order_items'},
        {'$group': {'_id': '$order_items.sku',
                    'count': {'$sum': '$order_items.quantity'},
                    'name': {'$first': '$order_items.name'}
                    }
         },
        {'$sort': SON([('count', -1), ('_id', -1)])}
    ]
    return db.orders.aggregate(pipeline)


def sales_choosen_products_by_dates(db, shop_id, sku_list, time_period):
    pipeline = [
        {'$match': {'$and': [
            {'shop_id': shop_id},
            {'state': 'finished'},
            {'entry_date': {'$gte': time_period[0]}},
            {'entry_date': {'$lte': time_period[1]}}
        ]}},
        {'$project': {'_id': 0, 'order_items': 1}},
        {'$unwind': '$order_items'},
        {'$match': {'$or': sku_list}
         },
        {'$group': {'_id': '$order_items.sku',
                    'count': {'$sum': '$order_items.quantity'},
                    'name': {'$first': '$order_items.name'}
                    }
         },
        {'$sort': SON([('count', -1), ('_id', -1)])}
    ]
    return db.orders.aggregate(pipeline)


def avg_sales_per_customer_per_city(db, shop_id):
    pipeline = [
        {'$match': {'$and': [
            {'shop_id': shop_id},
            {'customer_id': {'$ne': 'none'}},
            {'state': 'finished'}
        ]
        }
        },
        {'$project': {'_id': 0, 'customer_id': 1, 'order_items': 1}},
        {'$lookup': {
            'from': 'reg_customers',
            'localField': 'customer_id',
            'foreignField': '_id',
            'as': 'customer'
        }
        },
        {'$unwind': '$customer'},
        {'$project': {'customer_id': 1,
                      'order_items': 1,
                      'city': '$customer.address.city'
                      }
         },
        {'$unwind': '$order_items'},
        {'$group': {
            '_id': '$city',
         'total_sales': {'$sum': '$order_items.quantity'},
         'unique_users': {'$addToSet': '$customer_id'}
         }
         },
        {'$project': {'_id': 1,
                      'avg_sales_per_customer': {'$divide': ['$total_sales', {'$size': '$unique_users'}]}}
         }
    ]
    return db.orders.aggregate(pipeline)


def stock_quantities_by_dates(db, shop_id, time_period):
    pipeline = [
        {'$match': {'$and': [
            {'shop_id': shop_id},
            {'date': {'$gte': time_period[0]}},
            {'date': {'$lte': time_period[1]}}
        ]
        }
        }#,
        #{'$sort': SON([('count', -1), ('_id', -1)])}
    ]
    return db.stock_history.aggregate(pipeline)


def orders_served_by_employee(db, shop_id ,employee_id, time_period):
    pipeline = [
        {'$match': {'$and': [
            {'employee_id': ObjectId(employee_id)},
            {'shop_id': shop_id},
            {'state': 'finished'},
            {'entry_date': {'$gte': time_period[0]}},
            {'entry_date': {'$lte': time_period[1]}}
        ]
        }
        },
        {'$project': {'_id': 1, 'employee_id': 1, 'order_items': 1}},
        {'$group': {'_id': '$employee_id',
                  'served_orders': {'$addToSet': '$_id'},
                  'amount': {'$sum': 1}
                  }
         }
    ]
    return db.orders.aggregate(pipeline)


def list_employees_by_dates(db, shop_id, time_period):
    query = {
      '$and': [
        {'shop_id': shop_id},
        {'entry_date': {'$gte': time_period[0]} },
        {'entry_date': {'$lte': time_period[1]} }
      ]
    }
    result_fields = {'_id': 0, 'name': 1, 'ssn': 1, 'entry_date': 1}
    return db.employees.find(query, result_fields)


def list_customer_by_dates(db, shop_id, time_period):
    pipeline = [
        {'$match': {'$and': [
            {'shop_id': shop_id},
            {'customer_id': { '$ne': 'none'}},
            {'state': 'finished'},
            {'entry_date': {'$gte': time_period[0]}},
            {'entry_date': {'$lte': time_period[1]}}
        ]
        }
        },
        {'$group': {'_id': '$customer_id'}
        }
    ]
    return db.orders.aggregate(pipeline)
