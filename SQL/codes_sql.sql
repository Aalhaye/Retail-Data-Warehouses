-- إنشاء جدول branches_clean
CREATE TABLE IF NOT EXISTS raw_tables.branches_clean (
    branch_id VARCHAR(255) PRIMARY KEY,  -- تعديل إلى VARCHAR بدلاً من INTEGER
    shopping_mall VARCHAR(255),
    location VARCHAR(255),
    manager_name VARCHAR(255)
);

-- إنشاء جدول categories_clean
CREATE TABLE IF NOT EXISTS raw_tables.categories_clean (
    category_id VARCHAR(255) PRIMARY KEY,  -- تعديل إلى VARCHAR بدلاً من INTEGER
    category VARCHAR(255),
    description TEXT
);

-- إنشاء جدول customers_clean
CREATE TABLE IF NOT EXISTS raw_tables.customers_clean (
    customer_id VARCHAR(255) PRIMARY KEY,  -- تعديل إلى VARCHAR بدلاً من INTEGER
    gender VARCHAR(10),
    age INT,
    payment_method VARCHAR(100)
);

-- إنشاء جدول invoices_clean
CREATE TABLE IF NOT EXISTS raw_tables.invoices_clean (
    invoice_no VARCHAR(255) PRIMARY KEY,  -- تعديل إلى VARCHAR بدلاً من INTEGER
    customer_id VARCHAR(255),  -- تعديل إلى VARCHAR بدلاً من INTEGER
    product_id VARCHAR(255),  -- تعديل إلى VARCHAR بدلاً من INTEGER
    branch_id VARCHAR(255),  -- تعديل إلى VARCHAR بدلاً من INTEGER
    category_id VARCHAR(255),  -- تعديل إلى VARCHAR بدلاً من INTEGER
    category VARCHAR(255),
    quantity INT,
    price DECIMAL(10, 2),
    invoice_date DATE,
    shopping_mall VARCHAR(255)
);

-- إنشاء جدول products_clean
CREATE TABLE IF NOT EXISTS raw_tables.products_clean (
    product_id VARCHAR(255) PRIMARY KEY,  -- تعديل إلى VARCHAR بدلاً من INTEGER
    category VARCHAR(255),
    product_name VARCHAR(255),
    price DECIMAL(10, 2)
);





-- إنشاء جدول الأبعاد Branches في الـ dw
CREATE TABLE IF NOT EXISTS dw.branches_dimension (
    branch_id VARCHAR(255) PRIMARY KEY,
    shopping_mall VARCHAR(255),
    location VARCHAR(255),
    manager_name VARCHAR(255)
);

-- إنشاء جدول الأبعاد Categories في الـ dw
CREATE TABLE IF NOT EXISTS dw.categories_dimension (
    category_id VARCHAR(255) PRIMARY KEY,
    category VARCHAR(255),
    description TEXT
);

-- إنشاء جدول الأبعاد Customers في الـ dw
CREATE TABLE IF NOT EXISTS dw.customers_dimension (
    customer_id VARCHAR(255) PRIMARY KEY,
    gender VARCHAR(50),
    age INT,
    payment_method VARCHAR(100)
);

-- إنشاء جدول الأبعاد Products في الـ dw
CREATE TABLE IF NOT EXISTS dw.products_dimension (
    product_id VARCHAR(255) PRIMARY KEY,
    category VARCHAR(255),
    product_name VARCHAR(255),
    price DECIMAL(10, 2)
);



-- إنشاء جدول الحقائق Invoices في الـ dw
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



-- إضافة البيانات من branches_clean إلى dw.branches_dimension
INSERT INTO dw.branches_dimension (branch_id, shopping_mall, location, manager_name)
SELECT branch_id, shopping_mall, location, manager_name
FROM raw_tables.branches_clean;

-- إضافة البيانات من categories_clean إلى dw.categories_dimension
INSERT INTO dw.categories_dimension (category_id, category, description)
SELECT category_id, category, description
FROM raw_tables.categories_clean;

-- إضافة البيانات من customers_clean إلى dw.customers_dimension
INSERT INTO dw.customers_dimension (customer_id, gender, age, payment_method)
SELECT customer_id, gender, age, payment_method
FROM raw_tables.customers_clean;

-- إضافة البيانات من products_clean إلى dw.products_dimension
INSERT INTO dw.products_dimension (product_id, category, product_name, price)
SELECT product_id, category, product_name, price
FROM raw_tables.products_clean;

-- إضافة البيانات من invoices_clean إلى dw.invoices_fact
INSERT INTO dw.invoices_fact (invoice_no, customer_id, product_id, branch_id, category_id, category, quantity, price, invoice_date, shopping_mall)
SELECT invoice_no, customer_id, product_id, branch_id, category_id, category, quantity, price, invoice_date, shopping_mall
FROM raw_tables.invoices_clean;






-- التحقق من البيانات في dw.branches_dimension
SELECT * FROM dw.branches_dimension LIMIT 10;

-- التحقق من البيانات في dw.categories_dimension
SELECT * FROM dw.categories_dimension LIMIT 10;

-- التحقق من البيانات في dw.customers_dimension
SELECT * FROM dw.customers_dimension LIMIT 10;

-- التحقق من البيانات في dw.products_dimension
SELECT * FROM dw.products_dimension LIMIT 10;

-- التحقق من البيانات في dw.invoices_fact
SELECT * FROM dw.invoices_fact LIMIT 10;








