def test_sort_price1(sort_page):
    sort_page.click_dropdown_price_lth()
    sort_page.save_list_by_price()
    sort_page.check_sort_by_price_lists_az()


def test_sort_price2(sort_page):
    sort_page.click_dropdown_price_htl()
    sort_page.save_list_by_price()
    sort_page.check_sort_by_price_lists_za()


def test_sort_name_az(sort_page):
    sort_page.click_dropdown_name_az()
    sort_page.save_list_by_name()
    sort_page.check_sort_by_name_lists_az()


def test_sort_name_za(sort_page):
    sort_page.click_dropdown_name_za()
    sort_page.save_list_by_name()
    sort_page.check_sort_by_name_lists_za()



