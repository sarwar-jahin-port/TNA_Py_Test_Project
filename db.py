ALLOWED_ROLES = {"admin", "customer"}

users_db = [
    {
        "id": 1,
        "username": "admin",
        "password": "123",
        "role": "admin"
    },
    {
        "id": 2,
        "username": "customer1",
        "password": "1234",
        "role": "customer"
    },
    {
        "id": 3,
        "username": "customer2",
        "password": "1234",
        "role": "customer"
    }
]

catalog_db = [
    {
        "id": 101,
        "name": "Mechanical Keyboard",
        "price": 2000.0,
        "stock": 10
    },
    {
        "id": 102,
        "name": "Ergonomic Wireless Mouse",
        "price": 800.0,
        "stock": 25
    },
    {
        "id": 103,
        "name": "4K Ultra HD Monitor",
        "price": 15000.0,
        "stock": 5
    },
    {
        "id": 104,
        "name": "USB-C Multiport Adapter",
        "price": 1200.0,
        "stock": 0  # Out of stock item for testing get_available_products()
    }
]

current_cart = []

#simulation for cart 
cart = [
    {"price": 100.5282, "qty": 2},
    {"price": 100.224424, "qty": 3}
]

orders_db = []