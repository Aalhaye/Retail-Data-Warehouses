-- Creating Branches Dimension Table in DW
CREATE TABLE IF NOT EXISTS dw.branches_dimension (
    branch_id VARCHAR(255) PRIMARY KEY,  -- Unique ID for each branch
    shopping_mall VARCHAR(255),          -- Shopping mall where the branch is located
    location VARCHAR(255),               -- Branch's location
    manager_name VARCHAR(255)            -- Manager of the branch
);

-- Creating Categories Dimension Table in DW
CREATE TABLE IF NOT EXISTS dw.categories_dimension (
    category_id VARCHAR(255) PRIMARY KEY,  -- Unique ID for each category
    category VARCHAR(255),                 -- Name of the category
    description TEXT                       -- Description of the category
);

-- Creating Customers Dimension Table in DW
CREATE TABLE IF NOT EXISTS dw.customers_dimension (
    customer_id VARCHAR(255) PRIMARY KEY,  -- Unique ID for each customer
    gender VARCHAR(50),                    -- Gender of the customer
    age INT,                               -- Age of the customer
    payment_method VARCHAR(100)            -- Method of payment used by the customer
);

-- Creating Products Dimension Table in DW
CREATE TABLE IF NOT EXISTS dw.products_dimension (
    product_id VARCHAR(255) PRIMARY KEY,   -- Unique ID for each product
    category VARCHAR(255),                 -- Product's category
    product_name VARCHAR(255),             -- Name of the product
    price DECIMAL(10, 2)                   -- Price of the product
);

-- Creating Invoices Fact Table in DW
CREATE TABLE IF NOT EXISTS dw.invoices_fact (
    invoice_no VARCHAR(255) PRIMARY KEY,   -- Invoice number
    customer_id VARCHAR(255),              -- Customer ID (foreign key to customers_dimension)
    product_id VARCHAR(255),               -- Product ID (foreign key to products_dimension)
    branch_id VARCHAR(255),                -- Branch ID (foreign key to branches_dimension)
    category_id VARCHAR(255),              -- Category ID (foreign key to categories_dimension)
    category VARCHAR(255),                 -- Product's category
    quantity INT,                          -- Quantity of product sold
    price DECIMAL(10, 2),                  -- Price of the product
    invoice_date DATE,                     -- Date of the invoice
    shopping_mall VARCHAR(255)            -- Shopping mall where the sale occurred
);
