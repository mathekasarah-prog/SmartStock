import streamlit as st
import sqlite3
import csv
import io


def prepare_inventory_data(products):
    return [
        {
            "ID": product[0],
            "Name": product[1],
            "Price": product[2],
            "Quantity": product[3]
        }
        for product in products
    ]
from database import (
    initialize_db,
    load_sample_products,
    add_product,
    get_products,
    search_products,
    update_product,
    delete_product
)

from product import Product


# PAGE CONFIGURATION
st.set_page_config(
    page_title="SmartStock",
    page_icon="📦",
    layout="wide"
)


# INITIALIZE DATABASE
initialize_db()
load_sample_products()


# APPLICATION TITLE
st.title("📦 SmartStock")
st.caption("Small Business Inventory Management System")


# NAVIGATION
page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "View Inventory",
        "Add Product",
        "Update Product",
        "Delete Product",
        "Export CSV"
    ]
)


# DASHBOARD
if page == "Dashboard":

    products = get_products()

    total_products = len(products)

    inventory_value = sum(
        product[2] * product[3] for product in products
    )

    low_stock = sum(
        1 for product in products if product[3] <= 5
    )

    out_of_stock = sum(
        1 for product in products if product[3] == 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Products", total_products)

    col2.metric(
        "Inventory Value",
        f"KSh {inventory_value:,.2f}"
    )

    col3.metric("Low Stock", low_stock)

    col4.metric("Out of Stock", out_of_stock)

    st.subheader("Recent Inventory")

    st.dataframe(
        prepare_inventory_data(products),
        use_container_width=True,
        hide_index=True
    )


# VIEW INVENTORY
elif page == "View Inventory":

    st.subheader("Inventory")

    search_term = st.text_input("Search products by name")

    if search_term:
        products = search_products(search_term)
    else:
        products = get_products()

    st.dataframe(
        prepare_inventory_data(products),
        use_container_width=True,
        hide_index=True
    )


# ADD PRODUCT
elif page == "Add Product":

    st.subheader("Register New Product")

    with st.form("add_product_form"):

        name = st.text_input("Product Name")

        price = st.number_input(
            "Price (KSh)",
            min_value=0.0,
            step=50.0
        )

        quantity = st.number_input(
            "Quantity",
            min_value=0,
            step=1
        )

        submitted = st.form_submit_button("Add Product")

        if submitted:

            product = Product(name, price, quantity)

            if product.is_valid():

                try:
                    add_product(
                        product.name.strip(),
                        product.price,
                        product.quantity
                    )

                    st.success("Product added successfully!")

                except sqlite3.IntegrityError:
                    st.error("A product with this name already exists.")

            else:
                st.error("Please enter valid product information.")


# UPDATE PRODUCT
elif page == "Update Product":

    st.subheader("Update Product")

    products = get_products()

    if products:

        product_ids = [product[0] for product in products]

        selected_id = st.selectbox(
            "Select product ID",
            product_ids
        )

        selected_product = next(
            product for product in products
            if product[0] == selected_id
        )

        with st.form("update_product_form"):

            name = st.text_input(
                "Product Name",
                value=selected_product[1]
            )

            price = st.number_input(
                "Price (KSh)",
                min_value=0.0,
                value=float(selected_product[2])
            )

            quantity = st.number_input(
                "Quantity",
                min_value=0,
                value=int(selected_product[3])
            )

            submitted = st.form_submit_button("Save Changes")

            if submitted:

                product = Product(name, price, quantity)

                if product.is_valid():

                    try:
                        updated = update_product(
                            selected_id,
                            product.name.strip(),
                            product.price,
                            product.quantity
                        )

                        if updated:
                            st.success("Product updated successfully!")
                        else:
                            st.warning("No changes were made.")

                    except sqlite3.IntegrityError:
                        st.error("Another product already uses that name.")

                else:
                    st.error("Please enter valid product information.")

    else:
        st.info("No products available.")


# DELETE PRODUCT
elif page == "Delete Product":

    st.subheader("Delete Product")

    products = get_products()

    if products:

        product_ids = [product[0] for product in products]

        selected_id = st.selectbox(
            "Select product ID to delete",
            product_ids
        )

        selected_product = next(
            product for product in products
            if product[0] == selected_id
        )

        st.write(f"Product: {selected_product[1]}")

        confirm = st.checkbox("I confirm that I want to delete this product.")

        if st.button("Delete Product", disabled=not confirm):

            deleted = delete_product(selected_id)

            if deleted:
                st.success("Product deleted successfully!")
                st.rerun()

    else:
        st.info("No products available.")


# EXPORT CSV
elif page == "Export CSV":

    st.subheader("Export Inventory")

    products = get_products()

    if products:

        output = io.StringIO()

        fieldnames = ["ID", "Name", "Price", "Quantity"]

        writer = csv.DictWriter(
            output,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(prepare_inventory_data(products))

        st.download_button(
            label="Download Inventory CSV",
            data=output.getvalue(),
            file_name="smartstock_inventory.csv",
            mime="text/csv"
        )

    else:
        st.info("There are no products to export.")