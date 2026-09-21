"""Core Responsibilities:
1. Inventory availability filtering, 
2. Product search, 
3. Stock updates.

Functions to Build:
get_available_products(catalog) -> list: Filters and returns items where stock > 0.
search_products(catalog, keyword) -> list: Performs a case-insensitive search matching keyword.lower() against product names.
update_stock(catalog, product_id, quantity) -> bool: Decrements stock by quantity for the given product ID upon checkout.

catalog_db = [
    { "id": 101, "name": "Mechanical Keyboard",      "price": 2000.0,     "stock": 10 },
    { "id": 102, "name": "Ergonomic Wireless Mouse", "price": 800.0,      "stock": 25 }
    { "id": 103, "name": "4K Ultra HD Monitor",      "price": 15000.0,    "stock": 5  },
    { "id": 104, "name": "USB-C Multiport Adapter",  "price": 1200.0,     "stock": 0  } 
    # Out of stock item for testing get_available_products()
]"""
catalog = [
    { "id": 101, "name": "Mechanical Keyboard",      "price": 2000.0,     "stock": 10 },
    { "id": 102, "name": "Ergonomic Wireless Mouse", "price": 800.0,      "stock": 25 },
    { "id": 103, "name": "4K Ultra HD Monitor",      "price": 15000.0,    "stock": 5  },
    { "id": 104, "name": "USB-C Multiport Adapter",  "price": 1200.0,     "stock": 0  } 
    ]

#print(catalog)

def get_available_products(catalog):
    """Filters and returns items where stock > 0."""
    return [product for product in catalog if product["stock"] > 0]
#print(get_available_products(catalog))

def search_products(catalog, keyword):
    """Performs a case-insensitive search matching keyword.lower() against product names."""
    return [product for product in catalog if keyword.lower() in product["name"].lower()]
#print(search_products(catalog, "keyboard"))

def update_stock(catalog, product_id, quantity):
    """Decrements stock by quantity for the given product ID upon checkout."""
    for product in catalog:
        if product["id"] == product_id:
            if product["stock"] >= quantity:
                product["stock"] -= quantity
                return True
            else:
                return False  # Not enough stock
    return False  # Product ID not found

print(update_stock(catalog, 103, 2))