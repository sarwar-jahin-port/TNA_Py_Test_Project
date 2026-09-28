from db import catalog_db

def get_product(catalog, product_id):
    for product in catalog:
        if product["id"] == product_id:
            return product
    return None

def get_available_products(catalog_db):
    """Filters and returns items where stock > 0."""
    return [product for product in catalog_db if product["stock"] > 0]
#print(get_available_products(catalog_db))

def search_products(catalog_db, keyword):
    """Performs a case-insensitive search matching keyword.lower() against product names."""
    return [product for product in catalog_db if keyword.lower() in product["name"].lower()]
# print(search_products(catalog_db, "keyboard"))

def update_stock(catalog_db, product_id, quantity):
    """Decrements stock by quantity for the given product ID upon checkout."""
    for product in catalog_db:
        if product["id"] == product_id:
            if product["stock"] >= quantity:
                product["stock"] -= quantity
                return True
            else:
                return False  # Not enough stock
    return False  # Product ID not found

def restock(catalog_db, product_id, quantity):
    for product in catalog_db:
        if product["id"] == product_id:
            product["stock"] += quantity
            return True
    return False  # Product ID not found

#print(update_stock(catalog, 103, 2))
#print(update_stock(catalog_db, 104, 2))