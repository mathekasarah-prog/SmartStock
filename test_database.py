
from database import (
    initialize_db,
    add_product,
    get_products,
    search_products,
    update_product,
    delete_product
)

initialize_db()

# Add a product
add_product("Test Oil", 1200, 10)

# Display products
print("ALL PRODUCTS:")
print(get_products())

# Search
print("SEARCH RESULTS:")
print(search_products("Test"))

# Update
print("UPDATED ROWS:")
print(update_product(1, "Test Oil", 1200, 15))

# Delete
print("DELETED ROWS:")
print(delete_product(1))
