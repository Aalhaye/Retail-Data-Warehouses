{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "ObjectNotExecutableError",
     "evalue": "Not an executable object: 'SET search_path TO dw'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "File \u001b[1;32mc:\\Users\\Ahmed\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\sqlalchemy\\engine\\base.py:1414\u001b[0m, in \u001b[0;36mConnection.execute\u001b[1;34m(self, statement, parameters, execution_options)\u001b[0m\n\u001b[0;32m   1413\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m-> 1414\u001b[0m     meth \u001b[38;5;241m=\u001b[39m \u001b[43mstatement\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_execute_on_connection\u001b[49m\n\u001b[0;32m   1415\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mAttributeError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'str' object has no attribute '_execute_on_connection'",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[1;31mObjectNotExecutableError\u001b[0m                  Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 8\u001b[0m\n\u001b[0;32m      5\u001b[0m engine \u001b[38;5;241m=\u001b[39m create_engine(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mpostgresql://postgres:123@localhost:5432/project_DB\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m      7\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m engine\u001b[38;5;241m.\u001b[39mconnect() \u001b[38;5;28;01mas\u001b[39;00m connection:\n\u001b[1;32m----> 8\u001b[0m     \u001b[43mconnection\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mexecute\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mSET search_path TO dw\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m      9\u001b[0m \u001b[38;5;66;03m# دالة لاسترجاع إحصائيات المبيعات لكل منتج\u001b[39;00m\n\u001b[0;32m     10\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mproduct_sales\u001b[39m():\n",
      "File \u001b[1;32mc:\\Users\\Ahmed\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\sqlalchemy\\engine\\base.py:1416\u001b[0m, in \u001b[0;36mConnection.execute\u001b[1;34m(self, statement, parameters, execution_options)\u001b[0m\n\u001b[0;32m   1414\u001b[0m     meth \u001b[38;5;241m=\u001b[39m statement\u001b[38;5;241m.\u001b[39m_execute_on_connection\n\u001b[0;32m   1415\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mAttributeError\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m err:\n\u001b[1;32m-> 1416\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m exc\u001b[38;5;241m.\u001b[39mObjectNotExecutableError(statement) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01merr\u001b[39;00m\n\u001b[0;32m   1417\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m   1418\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m meth(\n\u001b[0;32m   1419\u001b[0m         \u001b[38;5;28mself\u001b[39m,\n\u001b[0;32m   1420\u001b[0m         distilled_parameters,\n\u001b[0;32m   1421\u001b[0m         execution_options \u001b[38;5;129;01mor\u001b[39;00m NO_OPTIONS,\n\u001b[0;32m   1422\u001b[0m     )\n",
      "\u001b[1;31mObjectNotExecutableError\u001b[0m: Not an executable object: 'SET search_path TO dw'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "# إعداد الاتصال بقاعدة بيانات PostgreSQL باستخدام SQLAlchemy\n",
    "engine = create_engine('postgresql://postgres:123@localhost:5432/project_DB')\n",
    "\n",
    "with engine.connect() as connection:\n",
    "    connection.execute(\"SET search_path TO dw\")\n",
    "    \n",
    "# دالة لاسترجاع إحصائيات المبيعات لكل منتج\n",
    "def product_sales():\n",
    "    query = \"\"\"\n",
    "    SELECT p.product_name, SUM(i.quantity) AS total_sales\n",
    "    FROM invoices_fact i\n",
    "    JOIN products_dim p ON i.product_id = p.product_id\n",
    "    GROUP BY p.product_name\n",
    "    ORDER BY total_sales DESC;\n",
    "    \"\"\"\n",
    "    # استعلام SQL لاسترجاع البيانات وتحميلها في DataFrame\n",
    "    sales_data = pd.read_sql(query, engine)\n",
    "    return sales_data\n",
    "\n",
    "# دالة لاسترجاع إحصائيات المبيعات حسب الفروع\n",
    "def branch_sales():\n",
    "    query = \"\"\"\n",
    "    SELECT b.branch_id, b.shopping_mall, SUM(i.quantity * i.price) AS total_sales_value\n",
    "    FROM invoices_fact i\n",
    "    JOIN branches_dim b ON i.branch_id = b.branch_id\n",
    "    GROUP BY b.branch_id, b.shopping_mall\n",
    "    ORDER BY total_sales_value DESC;\n",
    "    \"\"\"\n",
    "    # استعلام SQL لاسترجاع البيانات وتحميلها في DataFrame\n",
    "    branch_data = pd.read_sql(query, engine)\n",
    "    return branch_data\n",
    "\n",
    "# دالة لاسترجاع إحصائيات العملاء حسب طريقة الدفع\n",
    "def payment_method_sales():\n",
    "    query = \"\"\"\n",
    "    SELECT i.payment_method, SUM(i.quantity * i.price) AS total_sales_value\n",
    "    FROM invoices_fact i\n",
    "    GROUP BY i.payment_method\n",
    "    ORDER BY total_sales_value DESC;\n",
    "    \"\"\"\n",
    "    # استعلام SQL لاسترجاع البيانات وتحميلها في DataFrame\n",
    "    payment_data = pd.read_sql(query, engine)\n",
    "    return payment_data\n",
    "\n",
    "# عرض الإحصائيات للمستخدم\n",
    "if __name__ == \"__main__\":\n",
    "    print(\"1. Total Product Sales:\")\n",
    "    print(product_sales())  # طباعة إحصائيات المبيعات لكل منتج\n",
    "    \n",
    "    print(\"\\n2. Total Sales by Branch:\")\n",
    "    print(branch_sales())  # طباعة إحصائيات المبيعات حسب الفروع\n",
    "    \n",
    "    print(\"\\n3. Total Sales by Payment Method:\")\n",
    "    print(payment_method_sales())  # طباعة إحصائيات المبيعات حسب طريقة الدفع\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
