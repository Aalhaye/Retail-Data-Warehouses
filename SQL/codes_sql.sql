-- Create the branches_clean table
CREATE TABLE IF NOT EXISTS raw_tables.branches_clean (
    branch_id VARCHAR(255) PRIMARY KEY,  -- Changed to VARCHAR instead of INTEGER
    shopping_mall VARCHAR(255),
    location VARCHAR(255),
    manager_name VARCHAR(255)
);

-- Create the categories_clean table
CREATE TABLE IF NOT EXISTS raw_tables.categories_clean (
    category_id VARCHAR(255) PRIMARY KEY,  -- Changed to VARCHAR instead of INTEGER
    category VARCHAR(255),
    description TEXT
);

-- Create the customers_clean table
CREATE TABLE IF NOT EXISTS raw_tables.customers_clean (
    customer_id VARCHAR(255) PRIMARY KEY,  -- Changed to VARCHAR instead of INTEGER
    gender VARCHAR(10),
    age INT,
    payment_method VARCHAR(100)
);

-- Create the invoices_clean table
CREATE TABLE IF NOT EXISTS raw_tables.invoices_clean (
    invoice_no VARCHAR(255) PRIMARY KEY,  -- Changed to VARCHAR instead of INTEGER
    customer_id VARCHAR(255),  -- Changed to VARCHAR instead of INTEGER
    product_id VARCHAR(255),  -- Changed to VARCHAR instead of INTEGER
    branch_id VARCHAR(255),  -- Changed to VARCHAR instead of INTEGER
    category_id VARCHAR(255),  -- Changed to VARCHAR instead of INTEGER
    category VARCHAR(255),
    quantity INT,
    price DECIMAL(10, 2),
    invoice_date DATE,
    shopping_mall VARCHAR(255)
);

-- Create the products_clean table
CREATE TABLE IF NOT EXISTS raw_tables.products_clean (
    product_id VARCHAR(255) PRIMARY KEY,  -- Changed to VARCHAR instead of INTEGER
    category VARCHAR(255),
    product_name VARCHAR(255),
    price DECIMAL(10, 2)
);

-- Create the branches_dimension table in the dw schema
CREATE TABLE IF NOT EXISTS dw.branches_dimension (
    branch_id VARCHAR(255) PRIMARY KEY,
    shopping_mall VARCHAR(255),
    location VARCHAR(255),
    manager_name VARCHAR(255)
);

-- Create the categories_dimension table in the dw schema
CREATE TABLE IF NOT EXISTS dw.categories_dimension (
    category_id VARCHAR(255) PRIMARY KEY,
    category VARCHAR(255),
    description TEXT
);

-- Create the customers_dimension table in the dw schema
CREATE TABLE IF NOT EXISTS dw.customers_dimension (
    customer_id VARCHAR(255) PRIMARY KEY,
    gender VARCHAR(50),
    age INT,
    payment_method VARCHAR(100)
);

-- Create the products_dimension table in the dw schema
CREATE TABLE IF NOT EXISTS dw.products_dimension (
    product_id VARCHAR(255) PRIMARY KEY,
    category VARCHAR(255),
    product_name VARCHAR(255),
    price DECIMAL(10, 2)
);

-- Create the invoices_fact table in the dw schema
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

-- Insert data from branches_clean into dw.branches_dimension
INSERT INTO dw.branches_dimension (branch_id, shopping_mall, location, manager_name)
SELECT branch_id, shopping_mall, location, manager_name
FROM raw_tables.branches_clean;

-- Insert data from categories_clean into dw.categories_dimension
INSERT INTO dw.categories_dimension (category_id, category, description)
SELECT category_id, category, description
FROM raw_tables.categories_clean;

-- Insert data from customers_clean into dw.customers_dimension
INSERT INTO dw.customers_dimension (customer_id, gender, age, payment_method)
SELECT customer_id, gender, age, payment_method
FROM raw_tables.customers_clean;

-- Insert data from products_clean into dw.products_dimension
INSERT INTO dw.products_dimension (product_id, category, product_name, price)
SELECT product_id, category, product_name, price
FROM raw_tables.products_clean;

-- Insert data from invoices_clean into dw.invoices_fact
INSERT INTO dw.invoices_fact (invoice_no, customer_id, product_id, branch_id, category_id, category, quantity, price, invoice_date, shopping_mall)
SELECT invoice_no, customer_id, product_id, branch_id, category_id, category, quantity, price, invoice_date, shopping_mall
FROM raw_tables.invoices_clean;

-- Verify data in dw.branches_dimension
SELECT * FROM dw.branches_dimension LIMIT 10;

-- Verify data in dw.categories_dimension
SELECT * FROM dw.categories_dimension LIMIT 10;

-- Verify data in dw.customers_dimension
SELECT * FROM dw.customers_dimension LIMIT 10;

-- Verify data in dw.products_dimension
SELECT * FROM dw.products_dimension LIMIT 10;

-- Verify data in dw.invoices_fact
SELECT * FROM dw.invoices_fact LIMIT 10;
