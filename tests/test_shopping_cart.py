def test_shopping_cart_badge(shopping_cart):
    shopping_cart.click_random_inventory_element()
    shopping_cart.click_add_to_cart()
    shopping_cart.checkout_shopping_cart_badge()


def test_add_object_shopping_cart(shopping_cart):
    shopping_cart.click_random_inventory_element()
    shopping_cart.click_add_to_cart()
    shopping_cart.click_shopping_cart()
    shopping_cart.checkout_shopping_cart_inventory()
