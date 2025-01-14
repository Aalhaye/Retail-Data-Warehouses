import psycopg2
import pandas as pd
from psycopg2 import sql
from psycopg2 import OperationalError
from psycopg2 import sql,OperationalError
from sqlalchemy import create_engine


def check_table_exists(cursor, table_name):
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_schema = 'raw_tables' AND table_name = %s
        );
    """, (table_name,))
    return cursor.fetchone()[0]

def load_data_to_postgres(filepath, table_name):

    try:
        # Connecting to the database
        conn = psycopg2.connect(
            dbname="project_DB", 
            user="postgres", 
            password="123", 
            host="localhost", 
            port="5432"
        )


        # Creating a cursor object
        cursor = conn.cursor()

        # Checking that the table exists in the database
        if not check_table_exists(cursor, table_name):
            print(f"Error: The table '{table_name}' does not exist in 'raw_tables' schema.")
            return

        # Reading data from a CSV file
        data = pd.read_csv(filepath)
        columns = list(data.columns)

        # Building an INSERT query with placeholder
        insert_query = sql.SQL("INSERT INTO raw_tables.{} ({}) VALUES ({})").format(
            sql.Identifier(table_name),  # تخصيص اسم الجدول
            sql.SQL(', ').join(map(sql.Identifier, columns)),  # Customize columns
            sql.SQL(', ').join([sql.Placeholder()] * len(columns))  # Customize values
        )

        # Entering data into the database
        for row in data.itertuples(index=False, name=None):
            cursor.execute(insert_query, row)

        #  Confirming changes in the database
        conn.commit()

        print("Data loaded successfully!")

    except pd.errors.EmptyDataError:
        print(f"Error: The file '{filepath}' is empty")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found")

    except OperationalError as e:
        print(f"Operational error while loading data into table '{table_name}': {e}")
    
    except Exception as e:
        print(f"An error occurred while loading data into table '{table_name}': {e}")

if __name__ == "__main__":
    try:
        load_data_to_postgres(r"E:/مخازن بيانات/project2/processed/branches_clean.csv", "branches_clean")
        load_data_to_postgres(r"E:/مخازن بيانات/project2/processed/categories_clean.csv", "categories_clean")
        load_data_to_postgres(r"E:/مخازن بيانات/project2/processed/customers_clean.csv", "customers_clean")
        load_data_to_postgres(r"E:/مخازن بيانات/project2/processed/invoices_clean.csv", "invoices_clean")
        load_data_to_postgres(r"E:/مخازن بيانات/project2/processed/products_clean.csv", "products_clean")


        
    except Exception as e:
        print(f"A critical error occurred: {e}")
