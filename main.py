import db 
import orders
from orders import cart


users = db.users_db

print(users)

#printing orders
print("Printing cart total------")
print(orders.calculate_cart_total(cart))

#testing 
print("testing area")
total = orders.calculate_cart_total(cart)
discount = orders.apply_discount(total)
print(total,discount)

#-----------