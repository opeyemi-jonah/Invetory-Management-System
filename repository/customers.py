from models.Customer import Customer
from repository import database_connection as dbconn

def add_customer(customer):
    cursor, connection = dbconn()
    try:
        cursor.execute('''
        INSERT INTO customers (customer_id, name, contact)
        VALUES (?, ?, ?)
        ''', (customer.customer_id, customer.name, customer.contact))
        connection.commit()
    finally:
        connection.close()

def get_customer(customer_id):
    cursor, connection = dbconn()
    try:
        cursor.execute('SELECT * FROM customers WHERE customer_id = ?', (customer_id,))
        row = cursor.fetchone()
        if row:
            return Customer(row[0], row[1], row[2])
    finally:
        connection.close()
    return None

def update_customer(customer):
    cursor, connection = dbconn()
    try:
        cursor.execute('''
        UPDATE customers
        SET name = ?, contact = ?
        WHERE customer_id = ?
        ''', (customer.name, customer.contact, customer.customer_id))
        connection.commit()
    finally:
        connection.close()

def delete_customer(customer_id):
    cursor, connection = dbconn()
    try:
        cursor.execute('DELETE FROM customers WHERE customer_id = ?', (customer_id,))
        connection.commit()
    finally:
        connection.close()
