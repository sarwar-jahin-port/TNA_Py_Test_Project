import db 
import orders
from orders import cart
from db import users_db

print(users_db)

#printing orders
print("Printing cart total------")
print(orders.calculate_cart_total(cart))

#testing 
print("testing area")
total = orders.calculate_cart_total(cart)
discount = orders.apply_discount(total)
print(total,discount)

print(orders.create_order(users_db[0],cart))


#-----------