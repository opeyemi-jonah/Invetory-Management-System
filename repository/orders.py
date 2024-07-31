from models.Order import Order
from repository import database_connection as dbconn

def add_order(order):
    cursor, connection = dbconn()
    try:
        # Insert order details
        cursor.execute('''
        INSERT INTO orders (order_id, customer_name, total_price, order_date)
        VALUES (?, ?, ?, ?)
        ''', (order._Order__order_id, order._Order__customer_name, order._Order__total_price, order._Order__order_date))
        
        # Insert each product in order
        for product in order._Order__products:
            cursor.execute('''
            INSERT INTO order_items (order_id, product_id, quantity)
            VALUES (?, ?, ?)
            ''', (order._Order__order_id, product['product_id'], product['quantity']))
        
        connection.commit()
    finally:
        connection.close()


def get_order(order_id):
    cursor, connection = dbconn()
    try:
        # Get order details
        cursor.execute('SELECT * FROM orders WHERE order_id = ?', (order_id,))
        order_row = cursor.fetchone()
        if order_row:
            order_id, customer_name, total_price, order_date = order_row
            
            # Get products in the order
            cursor.execute('SELECT product_id, quantity FROM order_items WHERE order_id = ?', (order_id,))
            products = [{'product_id': row[0], 'quantity': row[1]} for row in cursor.fetchall()]
            
            return Order(order_id, customer_name, products, total_price, order_date)
    finally:
        connection.close()
    return None

def update_order(order):
    cursor, connection = dbconn()
    try:
        # Update order details
        cursor.execute('''
        UPDATE orders
        SET customer_name = ?, total_price = ?, order_date = ?
        WHERE order_id = ?
        ''', (order._Order__customer_name, order._Order__total_price, order._Order__order_date, order._Order__order_id))
        
        # Delete existing products and insert updated ones
        cursor.execute('DELETE FROM order_items WHERE order_id = ?', (order._Order__order_id,))
        for product in order._Order__products:
            cursor.execute('''
            INSERT INTO order_items (order_id, product_id, quantity)
            VALUES (?, ?, ?)
            ''', (order._Order__order_id, product['product_id'], product['quantity']))
        
        connection.commit()
    finally:
        connection.close()

def delete_order(order_id):
    cursor, connection = dbconn()
    try:
        # Delete products in the order
        cursor.execute('DELETE FROM order_items WHERE order_id = ?', (order_id,))
        
        # Delete order
        cursor.execute('DELETE FROM orders WHERE order_id = ?', (order_id,))
        
        connection.commit()
    finally:
        connection.close()
