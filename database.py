import sqlite3
from product import products

DB_NAME = "inventory.db"


def initialize_db():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL DEFAULT 0
            )
        """)
        connection.commit()
    finally:
        connection.close()
        
def load_sample_products():
    connection = sqlite3.connect(DB_NAME)

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM products")
        count = cursor.fetchone()[0]

        # Only load sample products when the table is empty
        if count == 0:
            for product in products:
                if product.is_valid():
                    cursor.execute(
                        """
                        INSERT INTO products (name, price, quantity)
                        VALUES (?, ?, ?)
                        """,
                        (product.name, product.price, product.quantity)
                    )

        connection.commit()

    finally:
        connection.close()
        
def add_product(name, price, quantity):
    connection = sqlite3.connect(DB_NAME)

    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
            (name, price, quantity)
        )
        connection.commit()
    finally:
        connection.close()
        

def update_product(product_id, name, price, quantity):
    connection = sqlite3.connect(DB_NAME)

    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE products
            SET name = ?, price = ?, quantity = ?
            WHERE id = ?
        """, (name, price, quantity, product_id))

        connection.commit()
        return cursor.rowcount
    finally:
        connection.close()
        
        
def delete_product(product_id):
    connection = sqlite3.connect(DB_NAME)

    try:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM products WHERE id = ?",
            (product_id,)
        )
        connection.commit()
        return cursor.rowcount
    finally:
        connection.close()
        
def search_products(search_term):
    connection = sqlite3.connect(DB_NAME)

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM products
            WHERE name LIKE ?
        """, (f"%{search_term}%",))

        return cursor.fetchall()
    finally:
        connection.close()
        
def get_products():
    connection = sqlite3.connect(DB_NAME)

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()

    finally:
        connection.close()


