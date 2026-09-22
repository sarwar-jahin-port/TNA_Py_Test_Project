import db 
import orders

cart = orders.cart
users = db.users_db

print(users)

#printing orders
print("Printing cart total------")
print(orders.calculate_cart_total(cart))
