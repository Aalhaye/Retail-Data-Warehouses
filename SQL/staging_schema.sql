-- Table for branch details
CREATE TABLE IF NOT EXISTS raw_tables.branches_clean (
    branch_id VARCHAR(255) PRIMARY KEY,  -- Branch identifier
    shopping_mall VARCHAR(255),          -- Mall name
    location VARCHAR(255),               -- Branch location
    manager_name VARCHAR(255)            -- Branch manager's name
);

-- Table for storing product categories
CREATE TABLE IF NOT EXISTS raw_tables.categories_clean (
    category_id VARCHAR(255) PRIMARY KEY,  -- Category identifier
    category VARCHAR(255),                 -- Category name
    description TEXT                       -- Category description
);

-- Table for customer information
CREATE TABLE IF NOT EXISTS raw_tables.customers_clean (
    customer_id VARCHAR(255) PRIMARY KEY,  -- Customer identifier
    gender VARCHAR(10),                    -- Customer's gender
    age INT,                               -- Customer's age
    payment_method VARCHAR(100)            -- Payment method
);

-- Table for invoice data
CREATE TABLE IF NOT EXISTS raw_tables.invoices_clean (
    invoice_no VARCHAR(255) PRIMARY KEY,   -- Invoice number
    customer_id VARCHAR(255),              -- Customer identifier
    product_id VARCHAR(255),               -- Product identifier
    branch_id VARCHAR(255),                -- Branch identifier
    category_id VARCHAR(255),              -- Category identifier
    category VARCHAR(255),                 -- Product category
    quantity INT,                          -- Quantity sold
    price DECIMAL(10, 2),                  -- Product price
    invoice_date DATE,                     -- Invoice date
    shopping_mall VARCHAR(255)            -- Shopping mall name
);

-- Table for product details
CREATE TABLE IF NOT EXISTS raw_tables.products_clean (
    product_id VARCHAR(255) PRIMARY KEY,   -- Product identifier
    category VARCHAR(255),                 -- Product category
    product_name VARCHAR(255),             -- Product name
    price DECIMAL(10, 2)                   -- Product price
);
