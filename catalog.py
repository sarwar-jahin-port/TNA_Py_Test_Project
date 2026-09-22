catalog = [
    { "id": 101, "name": "Mechanical Keyboard",      "price": 2000.0,     "stock": 10 },
    { "id": 102, "name": "Ergonomic Wireless Mouse", "price": 800.0,      "stock": 25 },
    { "id": 103, "name": "4K Ultra HD Monitor",      "price": 15000.0,    "stock": 5  },
    { "id": 104, "name": "USB-C Multiport Adapter",  "price": 1200.0,     "stock": 0  } 
    ]


def get_available_products(catalog):
    """Filters and returns items where stock > 0."""
    list_of_available_products = []
    for product in catalog:
        if product["stock"] > 0:
            list_of_available_products.append(product)
    return list_of_available_products
