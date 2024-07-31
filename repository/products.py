import sqlite3
from models.Product import Product

def add_product(product):
    connection = sqlite3.connect('database/inventory.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO products (product_id, name, category, price, quantity)
    VALUES (?, ?, ?, ?, ?)
    ''', (product.product_id, product.name, product.category, product.price, product.quantity))
    connection.commit()
    connection.close()

def get_product(product_id):
    connection = sqlite3.connect('database/inventory.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products WHERE product_id = ?', (product_id,))
    row = cursor.fetchone()
    connection.close()
    if row:
        return Product(row[0], row[1], row[2], row[3], row[4])
    return None

def update_product(product):
    connection = sqlite3.connect('database/inventory.db')
    cursor = connection.cursor()
    cursor.execute('''
    UPDATE products
    SET name = ?, category = ?, price = ?, quantity = ?
    WHERE product_id = ?
    ''', (product.name, product.category, product.price, product.quantity, product.product_id))
    connection.commit()
    connection.close()

def delete_product(product_id):
    connection = sqlite3.connect('database/inventory.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM products WHERE product_id = ?', (product_id,))
    connection.commit()
    connection.close()
