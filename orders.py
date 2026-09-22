from db import cart
from db import users_db,cart

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
            



