import sqlite3

def database_connection():
    connection = sqlite3.connect('database/inventory.db')
    cursor = connection.cursor()
    return cursor, connection