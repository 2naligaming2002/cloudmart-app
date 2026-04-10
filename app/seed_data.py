from app.database import products_container

products = [
    {"id": "1", "name": "Laptop", "category": "Electronics", "price": 1200},
    {"id": "2", "name": "Phone", "category": "Electronics", "price": 800},
    {"id": "3", "name": "Headphones", "category": "Electronics", "price": 150},
    {"id": "4", "name": "T-Shirt", "category": "Clothing", "price": 25},
    {"id": "5", "name": "Jeans", "category": "Clothing", "price": 50},
    {"id": "6", "name": "Jacket", "category": "Clothing", "price": 100},
    {"id": "7", "name": "Book", "category": "Books", "price": 15},
    {"id": "8", "name": "Notebook", "category": "Books", "price": 10}
]

for product in products:
    products_container.upsert_item(product)

print("Data inserted successfully!")
