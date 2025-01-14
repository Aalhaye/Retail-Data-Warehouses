from sqlalchemy import create_engine, text

# Establish connection to the Data Warehouse (DW) database
engine = create_engine('postgresql://postgres:123@localhost:5432/dw')

# Creating dimension and fact tables in the Data Warehouse (DW)
with engine.connect() as conn:
    # Create the branches_dimension table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS dw.branches_dimension (
        branch_id VARCHAR(255) PRIMARY KEY,
        shopping_mall VARCHAR(255),
        location VARCHAR(255),
        manager_name VARCHAR(255)
    );
    """)

    # Create the categories_dimension table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS dw.categories_dimension (
        category_id VARCHAR(255) PRIMARY KEY,
        category VARCHAR(255),
        description TEXT
    );
    """)

    # Create the customers_dimension table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS dw.customers_dimension (
        customer_id VARCHAR(255) PRIMARY KEY,
        gender VARCHAR(50),
        age INT,
        payment_method VARCHAR(100)
    );
    """)

    # Create the products_dimension table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS dw.products_dimension (
        product_id VARCHAR(255) PRIMARY KEY,
        category VARCHAR(255),
        product_name VARCHAR(255),
        price DECIMAL(10, 2)
    );
    """)

    # Create the invoices_fact table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS dw.invoices_fact (
        invoice_no VARCHAR(255) PRIMARY KEY,
        customer_id VARCHAR(255),
        product_id VARCHAR(255),
        branch_id VARCHAR(255),
        category_id VARCHAR(255),
        category VARCHAR(255),
        quantity INT,
        price DECIMAL(10, 2),
        invoice_date DATE,
        shopping_mall VARCHAR(255)
    );
    """)

    # Inserting data into the branches_dimension table from the branches_clean table
    conn.execute("""
    INSERT INTO dw.branches_dimension (branch_id, shopping_mall, location, manager_name)
    SELECT branch_id, shopping_mall, location, manager_name
    FROM raw_tables.branches_clean;
    """)

    # Inserting data into the categories_dimension table from the categories_clean table
    conn.execute("""
    INSERT INTO dw.categories_dimension (category_id, category, description)
    SELECT category_id, category, description
    FROM raw_tables.categories_clean;
    """)

    # Inserting data into the customers_dimension table from the customers_clean table
    conn.execute("""
    INSERT INTO dw.customers_dimension (customer_id, gender, age, payment_method)
    SELECT customer_id, gender, age, payment_method
    FROM raw_tables.customers_clean;
    """)

    # Inserting data into the products_dimension table from the products_clean table
    conn.execute("""
    INSERT INTO dw.products_dimension (product_id, category, product_name, price)
    SELECT product_id, category, product_name, price
    FROM raw_tables.products_clean;
    """)

    # Inserting data into the invoices_fact table from the invoices_clean table
    conn.execute("""
    INSERT INTO dw.invoices_fact (invoice_no, customer_id, product_id, branch_id, category_id, category, quantity, price, invoice_date, shopping_mall)
    SELECT invoice_no, customer_id, product_id, branch_id, category_id, category, quantity, price, invoice_date, shopping_mall
    FROM raw_tables.invoices_clean;
    """)

    # Checking data in the branches_dimension table
    print("\nChecking data in dw.branches_dimension")
    result = conn.execute("SELECT * FROM dw.branches_dimension LIMIT 10;")
    for row in result:
        print(row)

    # Checking data in the categories_dimension table
    print("\nChecking data in dw.categories_dimension")
    result = conn.execute("SELECT * FROM dw.categories_dimension LIMIT 10;")
    for row in result:
        print(row)

    # Checking data in the customers_dimension table
    print("\nChecking data in dw.customers_dimension")
    result = conn.execute("SELECT * FROM dw.customers_dimension LIMIT 10;")
    for row in result:
        print(row)

    # Checking data in the products_dimension table
    print("\nChecking data in dw.products_dimension")
    result = conn.execute("SELECT * FROM dw.products_dimension LIMIT 10;")
    for row in result:
        print(row)

    # Checking data in the invoices_fact table
    print("\nChecking data in dw.invoices_fact")
    result = conn.execute("SELECT * FROM dw.invoices_fact LIMIT 10;")
    for row in result:
        print(row)

print("DW schema has been created and data has been loaded successfully!")
