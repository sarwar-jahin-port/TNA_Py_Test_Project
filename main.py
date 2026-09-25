from utils import print_products
from utils import read_int
import db
import auth
import catalog_shovon as catalog
from orders import checkout, show_cart, add_to_cart


def print_banner():
    print(r"""
============================================================
                 E-COMMERCE CLI SYSTEM v1.0
============================================================
A simple terminal e-commerce demo with:
  [1] Customer shopping flow
  [2] Admin management flow
  [3] Product search and inventory
  [4] Cart, discounts, checkout, and sales report
============================================================
""")


def print_test_accounts():
    print("\nQUICK TEST ACCOUNTS")
    print("  Admin    -> username: admin      password: 123")
    print("  Customer -> username: customer1  password: 1234")
    print("  Customer -> username: customer2  password: 1234")
    print("")

def login_flow():
    print("\nLOGIN")
    print_test_accounts()
    username = input("Username (or 'back'): ").strip()
    if username.lower() == "back":
        return None

    password = input("Password: ").strip()
    user = auth.login(db.users_db, username, password)

    if user is None:
        print("Login failed. Check the username/password and try again.")
        return None

    print(f'\nLogged in as {user["username"]} ({user["role"]}).')
    return user

def customer_menu(user):
    cart = []

    while True:
        print(f"""
---------------- CUSTOMER MENU ({user["username"]}) ----------------
1. View available products
2. Search products
3. Add product to cart
4. View cart
5. Checkout
6. Logout
--------------------------------------------------------------
""")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print_products(catalog.get_available_products(db.catalog_db))
        elif choice == "2":
            keyword = input("Search keyword: ")
            print_products(catalog.search_products(db.catalog_db, keyword))
        elif choice == "3":
            add_to_cart(cart)
        elif choice == "4":
            show_cart(cart)
        elif choice == "5":
            checkout(user, cart)
        elif choice == "6":
            print("Logged out.")
            return
        else:
            print("Invalid option. Please choose 1-6.")

def admin_menu(user):
    allowed = {"admin"}
    if not auth.check_permission(user["role"], allowed):
        print("Access denied.")
        return

    while True:
        print(f"""
---------------- ADMIN MENU ({user["username"]}) ----------------
1. View all products
2. Search products
3. Restock product
4. View order history
5. Logout
-----------------------------------------------------------
""")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print_products(db.catalog_db)
        elif choice == "2":
            keyword = input("Search keyword: ")
            print_products(catalog.search_products(db.catalog_db, keyword))
        elif choice == "3":
            print_products(db.catalog_db)
            product_id = read_int("Product ID (0 = back): ")
            if product_id in (None, 0):
                continue
            quantity = read_int("Quantity to add: ")
            if quantity is None:
                continue
            if catalog.restock(db.catalog_db, product_id, quantity):
                print("Stock updated successfully.")
            else:
                print("Could not restock. Check the product ID and quantity.")
        elif choice == "4":
            if not db.orders_db:
                print("No orders have been completed yet.")
            else:
                for order in db.orders_db:
                    print(
                        f'Order #{order["order_id"]} | '
                        f'{order["User_name"]} | '
                        f'${order["total"]:.2f}'
                    )
        elif choice == "5":
            print("Logged out.")
            return
        else:
            print("Invalid option. Please choose 1-6.")


def main_menu():
    print_banner()
    print_test_accounts()

    while True:
        print("""
==================== START MENU ====================
1. Login as customer
2. Login as admin
3. Show test accounts
4. Exit
======================================================
""")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            user = login_flow()
            if user:
                if user["role"] == "customer":
                    customer_menu(user)
                else:
                    print("That account is not a customer account.")
        elif choice == "2":
            user = login_flow()
            if user:
                if user["role"] == "admin":
                    admin_menu(user)
                else:
                    print("That account is not an admin account.")
        elif choice == "3":
            print_test_accounts()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main_menu()