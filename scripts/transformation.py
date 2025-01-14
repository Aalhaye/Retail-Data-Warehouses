import pandas as pd
from faker import Faker

fake = Faker()

rows = 99457

products = pd.DataFrame({
    'product_id': [fake.uuid4()[:8] for _ in range(500)],  
    'category': [fake.word() for _ in range(500)],        
    'product_name': [fake.word() for _ in range(500)],   
    'price': [round(fake.random_number(digits=3, fix_len=False) + 10, 2) for _ in range(500)], 
})

branches = pd.DataFrame({
    'branch_id': [fake.uuid4()[:8] for _ in range(50)],        
    'shopping_mall': [fake.company() for _ in range(50)],     
    'location': [fake.city() for _ in range(50)],              
    'manager_name': [fake.name() for _ in range(50)],         
})

categories = pd.DataFrame({
    'category_id': [fake.uuid4()[:8] for _ in range(20)],  
    'category': [fake.word() for _ in range(20)],          
    'description': [fake.sentence() for _ in range(20)],   
})

customers = pd.DataFrame({
    'customer_id': [f'CUS-{i+1:05}' for i in range(rows)], 
    'gender': [fake.random_element(['Male', 'Female']) for _ in range(rows)],
    'age': [fake.random_int(min=18, max=70) for _ in range(rows)],
    'payment_method': [fake.random_element(['Cash', 'Card', 'Online']) for _ in range(rows)],
})

invoices = pd.DataFrame({
    'invoice_no': [f'INV-{i+1:07}' for i in range(rows)],        
    'customer_id': customers['customer_id'],                    
    'category': [fake.random_element(categories['category']) for _ in range(rows)], 
    'quantity': [fake.random_int(min=1, max=10) for _ in range(rows)],               
    'price': [fake.random_int(min=10, max=100) for _ in range(rows)],               
    'invoice_date': [fake.date_this_year() for _ in range(rows)],                    
    'shopping_mall': [fake.random_element(branches['shopping_mall']) for _ in range(rows)],  
})

print("Products Table:")
print(products.head())

print("\nBranches Table:")
print(branches.head())

print("\nCategories Table:")
print(categories.head())

print("\nCustomers Table:")
print(customers.head())

print("\nInvoices Table:")
print(invoices.head())


# products.to_csv("products.csv", index=False)
# branches.to_csv("branches.csv", index=False)
# categories.to_csv("categories.csv", index=False)
# customers.to_csv("customers.csv", index=False)
# invoices.to_csv("invoices.csv", index=False)
