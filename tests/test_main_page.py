import time


def test_sort_price(sort_page):
    sort_page.click_dropdown_price_lth()
    sort_page.sort_by_price_lth()
    sort_page.sort_by_price_lists()


def test_random_inventory(main_page, shopping_cart):
    main_page.click_random_inventory_element()
    time.sleep(3)
    shopping_cart.checkout_shopping_cart_badge()
