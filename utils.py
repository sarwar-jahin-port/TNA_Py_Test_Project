def read_int(prompt):
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Please enter a valid number.")
        return None

def print_products(products):
    if not products:
        print("No matching products found.")
        return

    print("\nID    PRODUCT                         PRICE       STOCK")
    print("-" * 58)
    for product in products:
        print(
            f'{product["id"]:<5} '
            f'{product["name"]:<32} '
            f'${product["price"]:>8.2f}   '
            f'{product["stock"]:>5}'
        )