import sqlite3


connection = sqlite3.connect("inventory.db")

cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")


connection.commit()
connection.close()