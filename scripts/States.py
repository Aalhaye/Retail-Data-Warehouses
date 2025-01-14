import pandas as pd
from sqlalchemy import create_engine, text  # Import text for executing raw SQL

# Configure connection to PostgreSQL database
engine = create_engine('postgresql://postgres:123@localhost:5432/project_DB')

# Use the connection to set the search_path
with engine.connect() as connection:
    # Use text() to execute raw SQL commands
    connection.execute(text("SET search_path TO dw"))
    
# Function to fetch product sales statistics
def product_sales():
    query = """
    SELECT p.product_name, SUM(i.quantity) AS total_sales
    FROM invoices_fact i
    JOIN products_dim p ON i.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_sales DESC;
    """
    # Fetch data into a DataFrame
    sales_data = pd.read_sql(query, engine)
    return sales_data

# Function to fetch branch sales statistics
def branch_sales():
    query = """
    SELECT b.branch_id, b.shopping_mall, SUM(i.quantity * i.price) AS total_sales_value
    FROM invoices_fact i
    JOIN branches_dim b ON i.branch_id = b.branch_id
    GROUP BY b.branch_id, b.shopping_mall
    ORDER BY total_sales_value DESC;
    """
    # Fetch data into a DataFrame
    branch_data = pd.read_sql(query, engine)
    return branch_data

# Function to fetch sales statistics by payment method
def payment_method_sales():
    query = """
    SELECT i.payment_method, SUM(i.quantity * i.price) AS total_sales_value
    FROM invoices_fact i
    GROUP BY i.payment_method
    ORDER BY total_sales_value DESC;
    """
    # Fetch data into a DataFrame
    payment_data = pd.read_sql(query, engine)
    return payment_data

# Display statistics to the user
if __name__ == "__main__":
    print("1. Total Product Sales:")
    print(product_sales())  # Print product sales statistics
    
    print("\n2. Total Sales by Branch:")
    print(branch_sales())  # Print branch sales statistics
    
    print("\n3. Total Sales by Payment Method:")
    print(payment_method_sales())  # Print payment method statistics
