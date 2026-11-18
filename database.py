import sqlite3
from product import products


connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0
)
""")
for p in products:
    cursor.execute(
        "INSERT OR IGNORE INTO products(name, price, quantity) VALUES (?,?,?)",
        (p.name, p.price, p.quantity)
)
    
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)


connection.commit()
connection.close()