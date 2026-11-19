
from database import (
    add_product,
    get_products,
    search_products,
    update_product,
    delete_product
)
# 1. ADD
add_product("SmartStock Test Item", 500, 10)
print("Product added!")

# 2. READ
print("\nALL PRODUCTS:")
print(get_products())



# 3. SEARCH
results = search_products("SmartStock Test Item")
print("\nSEARCH RESULTS:")
print(results)



# 4. GET PRODUCT ID
if results:
    product_id = results[0][0]
    print("\nProduct ID:", product_id)






    # 5. UPDATE
    updated = update_product(
        product_id,
        "SmartStock Test Item",
        600,
        15
    )
    print("Rows updated:", updated)

    # 6. DELETE
    deleted = delete_product(product_id)
    print("Rows deleted:", deleted)

    # 7. CONFIRM DELETION
    print("\nFINAL SEARCH:")
    print(search_products("SmartStock Test Item"))

else:
    print("Product was not found.")
