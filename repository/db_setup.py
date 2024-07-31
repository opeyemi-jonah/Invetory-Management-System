import sqlite3

def create_tables():
    connection = sqlite3.connect('database/inventory.db')
    cursor = connection.cursor()

    # Create Products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id TEXT PRIMARY KEY,
        name TEXT,
        category TEXT,
        price REAL,
        quantity INTEGER
    )
    ''')

    # Create Customers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id TEXT PRIMARY KEY,
        name TEXT,
        contact TEXT
    )
    ''')

    # Create Orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        customer_id TEXT,
        total_price FLOAT,
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    )
    ''')

    # Create OrderItems table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
        order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id TEXT,
        product_id TEXT,
        quantity INTEGER,
        FOREIGN KEY (order_id) REFERENCES orders (order_id),
        FOREIGN KEY (product_id) REFERENCES products (product_id)
    )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_tables()
