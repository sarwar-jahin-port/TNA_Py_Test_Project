#simulation for cart 
cart = [
    {"price": 100, "qty": 2},
    {"price": 50, "qty": 3}
]

def calculate_cart_total(cart) ->float :
    total = 0
    for item in cart:
        # print(item)
        item_price = item['price'] * item['qty']
        total += item_price
    return total


def apply_discount(total,rate=0.20) -> float: 
    return total - (total * rate)

def create_order(user,cart):

    total = calculate_cart_total(cart)


    return {"User_name": user.username,
             "Cart":cart , 
             "total" : apply_discount(total)
             }
            



