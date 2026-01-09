# List of product dictionaries
products = [
    {"name": "Eco-Friendly Bottle", "price": 25},
    {"name": "Bamboo Toothbrush", "price": 10},
    {"name": "Solar Charger", "price": 50},
    {"name": "Organic Tote Bag", "price": 15},
    {"name": "Recycled Notebook", "price": 30}
]

# Sort using a lambda function as the key
products.sort(key=lambda x: x['price'])

print("Products sorted by price (Low to High):")
for item in products:
    print(f"{item['name']}: ${item['price']}")
