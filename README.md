# Retail-Data-Warehouses
A repository that answers sales questions and helps business owners keep up with changes 

# Project Name
Smart Shopping World Project - Data Warehouse

### Description
This project is designed to work with retail data, focusing on marketing products using Python and SQL. It provides company managers with the tools to analyze sales data, track performance, and make informed decisions. The project aims to help businesses answer important questions, such as identifying best-selling products and predicting future demand trends.

This project uses a Data Warehouse architecture to organize and process the data efficiently, allowing managers to generate insights from the data easily.

Project Structure
Data: Contains raw data tables with information about branches, categories, customers, products, and invoices.
ETL (Extract, Transform, Load): Scripts that clean, transform, and load data into the Data Warehouse.
Data Warehouse (DW): The final destination of processed data, consisting of fact and dimension tables for reporting and analysis.
Features
Data extraction from raw sources.
Data transformation and cleaning processes using Python.
Data loading into a PostgreSQL Data Warehouse.
Ability to analyze and visualize retail sales, customer behaviors, and product performance.
Installation

## 1. Clone the repository:
git clone https://github.com/Aalhaye/Data-Warehouse.git

## 2.Install dependencies:
This project requires the following Python libraries:
```bash
pip install psycopg2
pip install pandas
pip install sqlalchemy
pip install matplotlib
pip install scikit-learn
```
## 3. Requirements:
You also need to have the following programs installed:

PostgreSQL: To store and manage data in SQL format.
Jupyter: To clean, process, and analyze the data.
To install PostgreSQL, visit: PostgreSQL Installation Guide To install Jupyter, run:
```bash
pip install notebook
```
4. Setup Database:
   
Install PostgreSQL and start the server.
Create a database named dw (or any name you prefer) in PostgreSQL.
Create the necessary tables (fact and dimension tables) as per the project's schema.
6. Run the application:
After installing the dependencies and setting up the database, run the main Python script:


python final.py
This script will extract data from the raw tables, clean and process it, and then load it into the Data Warehouse for analysis.

### Usage
1. After downloading the programs and libraries:
Activate PostgreSQL and ensure it’s running.
Connect to the database via the Python code provided in the project.

3. Data Pipeline:
Download or load data into the raw tables.
Run the Python script (final.py) to clean, transform, and load the data into the Data Warehouse.
4. Data Analysis and Reporting:
Once the data is loaded into the Data Warehouse, you can use SQL queries or Python code to generate reports, perform analysis, and visualize data (e.g., sales trends, top-selling products, customer insights).

## 4. Example Query:
```bash

  SELECT product_id, SUM(quantity) AS total_sales
  
  FROM dw.invoices_fact
  
  GROUP BY product_id
  
  ORDER BY total_sales DESC;
```  
This query gives you the total sales per product from the Data Warehouse.

## Communication and Support
If you have any questions or need assistance, feel free to contact me:

Email: alhayekahmed045@gmail.com
Phone: +20 597967157
License
This project is open-source and available under the MIT License.
