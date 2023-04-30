// Create a database for order table
CREATE TABLE orders(
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT 
    CURRENT_TIMESTAMP,
        total_amount DECIMAL(10,2)
);

// Create a database for order details
CREATE TABLE order_details (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quanity INT NOT NULL,
    price DECIMAL(10,2)
);

import my sql.connector

mydb = mysql.connector.connect(
    host="localhost" ,
    user="root" ,
    password="password" , 
    database="ecommerce"
)

// Define a function to retrieve the current user's shopping cart:

def get_shopping_cart(user_id): cursor = mydb.cursor()

# Retrieve the order details for the current user's shopping cart
query = """
SELECT od.id, p.name, od.quantity, od.price
FROM orders o
JOIN order_details od ON o.id = od.order_id
JOIN products p ON od.product_id = p.id
WHERE o.customers_id = %s AND o.order_date
IS NULL
"""

cursor.execute(query, (user_id,))
result = cursor.fetchall()

# Convert the result to a dictionary
shopping_cart = {}
for row in result:
    item_id, item_name, item_quantity, item_price = row
shopping_cart[item_id] = {
    "name": item_name,
    "quantity": item_quantity,
    "price": item_price
}

return shopping_cart
}

// Define a function to add a product to the shopping cart

def add_to_cart(user_id, product_id, quantity):
    cursor = mydb.cursor()

    # Check if the product is already in the shopping cart
    query = """
    SELECT od.id, od.quantity
    FROM orders o
    JOIN order_details od ON od.id = od.order_id
    WHERE o.customer_id= %s AND o.order_date
IS NULL AND od.product_id = %s
"""
cursor.execute(query, (user_id, product_id))
    result = cursor.fetchone()

    if result:
        # If the product is already in the shopping cart, update the quantity
        order_detail_id, current_quantity = result
        new_quantity = current_quantity + quantity
        query = """
        UPDATE order_details SET quantity = %s
        WHERE id = %s
        """

        cursor.executive(query, (new_quantity, order_detail_d))
        else:
            # If the product is not in the shopping cart, add it
            query = """
            INSERT INTO orders (customers_id, total_amount) VALUES (%s, 0)
            """

            cursor.execute(query, user_id,))
            order_id = cursor.lastrowid

            query = """
            INSERT INTO order_details (order_id, product_id, quantity, price)
            SELECT %s, id, %s, price FROM products 
            WHERE id = %s
            """
            cursor.execute(query, (order_id, quantity, product_id))

            mydb.commit