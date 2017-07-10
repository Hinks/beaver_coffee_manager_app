from datetime import datetime
from toolz.dicttoolz import assoc


def read(db, shop_id):
    shop = fetch_shop(db, shop_id)
    if shop:
        return shop.get('stock_quantities')
    else:
        return 'error, no shop with that id exists.'


def update(db, shop_id):
    date_input_str = input('Enter the date of today, format: yyyy-mm-dd: ')
    date = convert_to_datetime(date_input_str)

    sku_input = input('Enter product sku to update: ')
    qty_input = input('Enter product qty to increment by(possitive or negative)')
    update_shopstock_and_stockhistory(db, shop_id, date, sku_input, int(qty_input))
    return f'Stock qty for {sku_input} has been updated by {qty_input} and logged on {date_input_str}.'


def update_shopstock_and_stockhistory(db, shop_id, date, sku, qty):
    """ Update stock quantities in shop and logg that change to the stock_history collection."""

    stock_history_at_date = fetch_historical_shop_stock(db, shop_id, date)

    # If the logg/history document(usually the document at the current/todays date)
    # for the specified date exist, then update both the stock quantity for the
    # product in the current shop inventory and in "todays" (history/logg date) document.
    if stock_history_at_date:
        update_shop_stock(db, shop_id, sku, qty)

        update_stock_history(db, shop_id, date, sku, qty)

    # If the requested stock history document(usually the document at the current/todays date)
    # for the shop doesn't exist, we update the current shops inventory
    # and insert todays logg ducument with the correct init-stock-quantities.
    # Example: if yesterdays stock qty for product with sku 1001 = 100 and
    # at todays very first puchase of that product is a quantity of 5,
    # the new insteted logg document's init-stock-quantity for that product has
    # to be 95.
    else:
        last_histoty_stock_date = fetch_latest_historical_shop_stock(db, shop_id)

        # If we find the latest logg document, the inventory in the shop is
        # directly updated, and we use the latest logg document to calculate
        # "today's stock quantities" and insert the logg document for today with the
        # correct stock-init values. As the example above.
        if last_histoty_stock_date:
            update_shop_stock(db, shop_id, sku, qty)

            old_stock = last_histoty_stock_date.get('stock_quantities')
            new_stock = update_stock(old_stock, sku, qty)
            insert_new_history_doc(db, shop_id, date, new_stock)

        # If no logg document for the shop exist in the stock_history-collection,
        # the init-stock-values for today logg document has to be fetched from
        # the current shop inventory instead of a previous logg ducument before
        # beeing inserted.
        else:
            update_shop_stock(db, shop_id, sku, qty)

            shop = fetch_shop(db, shop_id)
            insert_new_history_doc(db, shop_id, date, shop.get('stock_quantities'))


def fetch_shop(db, shop_id):
    """ Returns the specified shop as a dictionary."""
    return db.locations.find_one({'_id': shop_id})


def fetch_historical_shop_stock(db, shop_id, date):
    """ Returns the stock quantities for the shop at the specified date
    if the document exists.
    """
    return db.stock_history.find_one({'shop_id': shop_id, 'date': date})


def fetch_latest_historical_shop_stock(db, shop_id):
    """ Returns the latest stock quantities for the shop.
    If no historical stock quantities exists, None will be returned.
    """
    try:
        cursor = db.stock_history.find({'shop_id': shop_id}).sort('date', -1).limit(1)
        return cursor[0]
    except IndexError as e:
        print('No historical stock quantities exist for this shop.')
        return None


def update_shop_stock(db, shop_id, sku, qty):
    """ Updates the stock quantity for a product in the shop."""
    return db.locations.update({'_id': shop_id},
        {'$inc': {f'stock_quantities.{sku}': qty}}
    )


def update_stock_history(db, shop_id, date, sku, qty):
    """ Updates the stock quantity for a product in the shop at the specified date."""
    return db.stock_history.update({'shop_id': shop_id, 'date': date},
        {'$inc': {f'stock_quantities.{sku}': qty}}
    )


def insert_new_history_doc(db, shop_id, date, stock):
    """ Inserts a new stock_history document for the shop in the stock_history
    collection. A new history document for the shop will be inserted if it doesn't exist.
    This is performed at the very first buy or product stock change every day.
    """
    return db.stock_history.insert_one({
        'date': date,
        'shop_id': shop_id,
        'stock_quantities': stock
    })


def update_stock(stock, sku, qty):
    """ Returns an updated version of the stock, there the quantity for the specified
    sku is updated.

    >>> update_stock({'1001': 1000, '1002': 1250}, '1001', 50)
    {'1001': 1050, '1002': 1250}
    >>> update_stock({'1001': 1000, '1002': 1250}, '1001', -50)
    {'1001': 950, '1002': 1250}
    """
    old_sku_qty = stock.get(sku)
    return assoc(stock, sku, old_sku_qty + qty)

def convert_to_datetime(date_str):
    year, month, day = map(int, date_str.split('-'))
    return datetime(year, month, day)
