import sqlite3
from product import Product

product1 = Product("Shea Glow Body Butter", 950, 25)
product2 = Product("African Black Soap", 650, 25)
product3 = Product("Rosemary Hair Oil", 1100, 25)
product4 = Product("Sandalwood Scented Candle", 1500, 25)
product5 = Product("Lavender Bath Set", 1800, 25)
product6 = Product("Chebe & Hibiscus Hair Butter", 1250, 25)
product7 = Product("Aloe & Honey Leave-In Conditioner", 1100, 25)
product8 = Product("Moringa Wellness Capsules", 1500, 25)
product9 = Product("Purify Bath Salts", 950, 25)
product10 = Product("Niacinamide Face Cream", 1350, 25)
product11 = Product("Mango Body Butter", 1200, 32)
product12 = Product("Turmeric & Honey Natural Soap", 650, 18)
product13 = Product("Rose & Aloe Face Mist", 850, 20)
product14 = Product("Moringa Body Scrub", 1100, 33)
product15 = Product("Rosehip Seed Oil", 1350, 30)
product16 = Product("Lavender & Frankincense Candle", 1500, 33)

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
for p in [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12, product13, product14, product15, product16]:
    cursor.execute(
        "INSERT OR IGNORE INTO products(name, price, quantity) VALUES (?,?,?)",
        (p.name, p.price, p.quantity)
)
    
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)


connection.commit()
connection.close()