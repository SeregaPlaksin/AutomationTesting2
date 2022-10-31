
def test_sort_price(sort_page):
    sort_page.click_dropdown_price_lth()
    sort_page.sort_by_price_lth()
    sort_page.sort_by_price_lists()


def test_random_inventory(main_page):
    main_page.random_inventory_elements()
