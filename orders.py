from utils import print_products
from utils import read_int
import catalog_shovon as catalog
from db import users_db,cart,catalog_db, orders_db

def calculate_cart_total(cart) -> float :
    total = 0
    for item in cart:
        # print(item)
        item_price = item['price'] * item['qty']
        total += item_price
    return round(total,2)

#this the function which deals with applying discount 
def apply_discount(total,rate=0.01) -> float: 
    if total > 1000:
        rate = 0.3
    if total > 2000:
        rate = 0.4

    return round(total - (total * rate)) #returning the final discounted price
 
#this function aggregates all the user and cart  
def create_order(user,cart):
    total = calculate_cart_total(cart)
    try:
        if user not in users_db:
            raise ValueError("User doesn't exist")
        username = user['username']
    except (TypeError,  KeyError, ValueError):
        return {"error": "User doesn't exist"}
    
    return {"User_name": username,
             "Cart":cart, 
             "total" : apply_discount(total)
             }
            
def add_to_cart(cart):
    print_products(catalog.get_available_products(catalog_db))
    product_id = read_int("\nEnter product ID to add (0 = back): ")
    if product_id in (None, 0):
        return

    product = catalog.get_product(catalog_db, product_id)
    if product is None:
        print("Product ID not found.")
        return

    if product["stock"] <= 0:
        print("That product is out of stock.")
        return

    quantity = read_int("Quantity: ")
    if quantity is None or quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    existing = next((item for item in cart if item["id"] == product_id), None)
    already_in_cart = existing["qty"] if existing else 0

    if already_in_cart + quantity > product["stock"]:
        print(f'Only {product["stock"]} unit(s) are currently available.')
        return

    if existing:
        existing["qty"] += quantity
    else:
        cart.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "qty": quantity,
        })

    print(f'Added {quantity} x {product["name"]} to your cart.')

def show_cart(cart):
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\nYOUR CART")
    print("-" * 65)
    for item in cart:
        line_total = item["price"] * item["qty"]
        print(
            f'{item["name"]:<32} '
            f'x {item["qty"]:<3} '
            f'${line_total:>9.2f}'
        )

    subtotal = calculate_cart_total(cart)
    total = apply_discount(subtotal)
    print("-" * 65)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"After discount: ${total:.2f}")

def checkout(user, cart):
    if not cart:
        print("Your cart is empty. Add something before checkout.")
        return

    show_cart(cart)
    confirm = input("\nConfirm checkout? (y/n): ").strip().lower()
    if confirm != "y":
        print("Checkout cancelled.")
        return

    # Validate inventory before changing any stock.
    for item in cart:
        product = catalog.get_product(catalog_db, item["id"])
        if product is None or product["stock"] < item["qty"]:
            print(f'Checkout failed: insufficient stock for "{item["name"]}".')
            return

    order = create_order(user, cart)
    if "error" in order:
        print(order["error"])
        return

    for item in cart:
        catalog.update_stock(catalog_db, item["id"], item["qty"])

    order["order_id"] = 5001 + len(orders_db)
    orders_db.append(order)

    print("\nORDER COMPLETED")
    print(f'Order ID: {order["order_id"]}')
    print(f'Final total: ${order["total"]:.2f}')
    print("Thank you for shopping!")
    cart.clear()
