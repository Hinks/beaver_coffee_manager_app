//Insert initial data to the database
//type this in shell: mongo localhost:27017/beaver db_init_script.js
conn = new Mongo();
db = conn.getDB("beaver");

db.dropDatabase()
db = db.getSiblingDB('beaver')

//insert
var init_date = ISODate("2017-06-00T00:00:00Z")

var product_id_1 = ObjectId()
var product_id_2 = ObjectId()
var product_id_3 = ObjectId()
var product_id_4 = ObjectId()
var product_id_5 = ObjectId()
try {
   db.products.insertMany( [
     {
       "_id": product_id_1,
       "sku": "1001",
       "name": "Esspresso Roast",
       "description": "Whole-Bean Coffee",
       "pricing": {
         "retail": 5
       }
     },
     {
       "_id": product_id_2,
       "sku": "1002",
       "name": "Brewed Coffee",
       "description": "Whole-Bean Coffee",
       "pricing": {
         "retail": 3
       }
     },
     {
       "_id": product_id_3,
       "sku": "1003",
       "name": "Latte",
       "description": "Whole-Bean Coffee",
       "pricing": {
         "retail": 4
       }
     },
     {
       "_id": product_id_4,
       "sku": "1004",
       "name": "Hot Chocolate",
       "description": "Whole-Bean Coffee (Cocoa Mix)",
       "pricing": {
         "retail": 5
       }
     },
     {
       "_id": product_id_5,
       "sku": "1005",
       "name": "Whole Bean French Roast",
       "description": "Whole-Bean Coffee",
       "pricing": {
         "retail": 7
       }
     }
   ] );
} catch (e) {
   print (e)
}

//insert shops
var shop_id_1 = ObjectId()
var shop_id_2 = ObjectId()
try {
  db.shops.insertMany([
    {
      "_id": shop_id_1,
      "country": "sweden",
      "city": "malmo",
      "street": "lilla torg",
      "stock_quantities": {
        "1001": 4997,
        "1002": 4994,
        "1003": 5000,
        "1004": 4999,
        "1005": 4999
      }
    },
    {
      "_id": shop_id_2,
      'country': 'sweden',
      'city': 'malmo',
      'street': 'centralen',
      'stock_quantities': {
        "1001" : 1000,
        "1002" : 1000,
        "1003" : 1000,
        "1004" : 1000,
        "1005" : 1000
    	}}
  ])
} catch (e) {
  print (e)
}

//branch managers
var branch_manager_id_1 = ObjectId()
try {
  db.branch_managers.insertOne({
    '_id': branch_manager_id_1,
    'name': 'James King',
    'ssn': '19551212-9999',
    'shop_id': shop_id_1
  })
} catch (e) {
  console.log();
}

var branch_manager_id_2 = ObjectId()
try {
  db.branch_managers.insertOne({
    '_id': branch_manager_id_2,
    'name': 'James Junior',
    'ssn': '19551212-8888',
    'shop_id': shop_id_2
  })
} catch (e) {
  console.log();
}

//sales managers
var sales_manager_id_1 = ObjectId()
try {
  db.sales_managers.insertOne({
    '_id': sales_manager_id_1,
    'name': 'Amanda Daylight',
    'ssn': '19620303-2222',
  })
} catch (e) {
  print (e)
}

//customers
var customer_id_1 = ObjectId()
var customer_id_2 = ObjectId()
var customer_id_3 = ObjectId()
var customer_id_4 = ObjectId()
var customer_id_5 = ObjectId()
try {
  db.reg_customers.insertMany([
    {
      "_id": customer_id_1,
      "ssn": "19600505-1234",
      "address": {
        "country": "sweden",
        "city": "malmo"
      },
      "occupation": "Truck driver",
      "entry_date": init_date,
      "personal_card": {
        "code": "111111111",
        "country": "sweden"
      }
    },
    {
      "_id": customer_id_2,
      "ssn": "19700101-6789",
      "address": {
        "country": "sweden",
        "city": "lund"
      },
      "occupation": "Programmer",
      "entry_date": init_date,
      "personal_card": {
        "code": "111111112",
        "country": "sweden"
      }
    },
    {
      "_id": customer_id_3,
      "ssn": "19750211-9090",
      "address": {
        "country": "sweden",
        "city": "stockholm"
      },
      "occupation": "Teacher",
      "entry_date": init_date,
      "personal_card": {
        "code": "111111113",
        "country": "sweden"
      }
    },
    {
      "_id": customer_id_4,
      "ssn": "19850211-9191",
      "address": {
        "country": "sweden",
        "city": "stockholm",
        "postal_code": "08308"
      },
      "occupation": "Teacher",
      "entry_date": init_date,
      "personal_card": {
        "code": "111111114",
        "country": "sweden"
      }
    },
    {
      "_id": customer_id_5,
      "ssn": "19950211-9294",
      "address": {
        "country": "sweden",
        "city": "stockholm",
        "postal_code": "08308"
      },
      "occupation": "Bay Watcher",
      "entry_date": init_date,
      "personal_card": {
        "code": "111111115",
        "country": "sweden"
      }
    }
  ])
} catch (e) {
  print (e)
}

//employee
var employee_id_1 = ObjectId()
var employee_id_2 = ObjectId()
try {
  db.employees.insertMany([
    {
      "_id": employee_id_1,
      "name": "Emma Thomsson",
      "ssn": "19751010-5544",
      "shop_id": shop_id_1,
      "entry_date": init_date,
      "employment_history": [],
      "comments": []
    },
    {
      "_id": employee_id_2,
      "name": "Polly Larsson",
      "ssn": "19780303-6677",
      "shop_id": shop_id_1,
      "entry_date": init_date,
      "employment_history": [],
      "comments": []
    }
  ])
} catch (e) {
  print (e)
}

//orders
var order_id_1 = ObjectId()
var order_id_2 = ObjectId()
var order_id_3 = ObjectId()
var order_id_4 = ObjectId()
var order_id_5 = ObjectId()
var order_id_6 = ObjectId()
try {
  db.orders.insertMany([
    {
      "_id": order_id_1,
      "employee_id": employee_id_1,
      "customer_id": customer_id_1,
      "shop_id": shop_id_1,
      "state": "finished",
      "order_items": [
        {
          "_id": product_id_1,
          "sku": "1001",
          "name": "Esspresso Roast",
          "quantity": 2,
          "pricing": {
            "retail": 5
          }
        }
      ],
      "total_sum": 10,
      "currency": "SEK",
      "entry_date": ISODate("2017-06-00T12:00:00Z")
    },
    {
      "_id": order_id_2,
      "employee_id": employee_id_1,
      "customer_id": customer_id_2,
      "shop_id": shop_id_1,
      "state": "finished",
      "order_items": [
        {
          "_id": product_id_1,
          "sku": "1001",
          "name": "Esspresso Roast",
          "quantity": 1,
          "pricing": {
            "retail": 5
          }
        },
        {
          "_id": product_id_2,
          "sku": "1002",
          "name": "Brewed Coffee",
          "quantity": 3,
          "pricing": {
            "retail": 3
          }
        },
        {
          "_id": product_id_4,
          "sku": "1004",
          "name": "Hot Chocolate",
          "quantity": 1,
          "pricing": {
            "retail": 7
          }
        }
      ],
      "total_sum": 21,
      "currency": "SEK",
      "entry_date": ISODate("2017-06-00T12:01:00Z")
    },
    {
      "_id": order_id_3,
      "employee_id": employee_id_2,
      "customer_id": "none",
      "shop_id": shop_id_1,
      "state": "finished",
      "order_items": [
        {
          "_id": product_id_5,
          "sku": "1005",
          "name": "Whole Bean French Roast",
          "quantity": 1,
          "pricing": {
            "retail": 7
          }
        }
      ],
      "total_sum": 7,
      "currency": "SEK",
      "entry_date": ISODate("2017-06-00T12:02:00Z")
    },
    {
      "_id": order_id_4,
      "employee_id": employee_id_1,
      "customer_id": "none",
      "shop_id": shop_id_1,
      "state": "finished",
      "order_items": [
        {
          "_id": product_id_2,
          "sku": "1002",
          "name": "Brewed Coffee",
          "quantity": 3,
          "pricing": {
            "retail": 3
          }
        }
      ],
      "total_sum": 9,
      "currency": "SEK",
      "entry_date": ISODate("2017-06-00T12:03:00Z")
    },
    {
      "_id": order_id_5,
      "employee_id": employee_id_1,
      "customer_id": customer_id_4,
      "shop_id": shop_id_1,
      "state": "finished",
      "order_items": [
        {
          "_id": product_id_2,
          "sku": "1002",
          "name": "Brewed Coffee",
          "quantity": 3,
          "pricing": {
            "retail": 3
          }
        }
      ],
      "total_sum": 9,
      "currency": "SEK",
      "entry_date": ISODate("2017-06-00T12:04:00Z")
    },
    {
      "_id": order_id_6,
      "employee_id": employee_id_1,
      "customer_id": customer_id_5,
      "shop_id": shop_id_1,
      "state": "finished",
      "order_items": [
        {
          "_id": product_id_2,
          "sku": "1002",
          "name": "Brewed Coffee",
          "quantity": 10,
          "pricing": {
            "retail": 3
          }
        }
      ],
      "total_sum": 30,
      "currency": "SEK",
      "entry_date": ISODate("2017-06-00T12:05:00Z")
    }
  ])
} catch (e) {
  print (e)
}

//stock_history
var stock_history_id_1 = ObjectId()
try {
  db.stock_history.insertOne({
    "_id": stock_history_id_1,
    "date": init_date,
    "shop_id": shop_id_1,
    "stock_quantities": {
      "1001": 4997,
      "1002": 4994,
      "1003": 5000,
      "1004": 4999,
      "1005": 4999
    }
  })
} catch (e) {
  print (e)
}
