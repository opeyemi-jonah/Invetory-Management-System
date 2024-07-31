from models.Product import Product
from repository import database_connection as dbconn

def add_product(product):
    cursor, connection = dbconn()
    try:
        cursor.execute('''
        INSERT INTO products (product_id, name, category, price, quantity)
        VALUES (?, ?, ?, ?, ?)
        ''', (product.product_id, product.name, product.category, product.price, product.quantity))
        connection.commit()
    finally:
        connection.close()

def get_product(product_id):
    cursor, connection = dbconn()
    try:
        cursor.execute('SELECT * FROM products WHERE product_id = ?', (product_id,))
        row = cursor.fetchone()
        if row:
            return Product(row[0], row[1], row[2], row[3], row[4])
    finally:
        connection.close()
    return None

def update_product(product):
    cursor, connection = dbconn()
    try:
        cursor.execute('''
        UPDATE products
        SET name = ?, category = ?, price = ?, quantity = ?
        WHERE product_id = ?
        ''', (product.name, product.category, product.price, product.quantity, product.product_id))
        connection.commit()
    finally:
        connection.close()

def delete_product(product_id):
    cursor, connection = dbconn()
    try:
        cursor.execute('DELETE FROM products WHERE product_id = ?', (product_id,))
        connection.commit()
    finally:
        connection.close()
