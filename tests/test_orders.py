from orders import calculate_cart_total, apply_discount


def test_calculate_cart_total():
    cart = [
        {"price": 10, "qty": 2},
        {"price": 5, "qty": 1}
    ]

    result = calculate_cart_total(cart)

    assert result == 25


def test_apply_discount():
    result = apply_discount(100)

    assert result == 99