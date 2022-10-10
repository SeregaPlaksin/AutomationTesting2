import time


def test_successful_login(auth_page):
    auth_page.enter_correct_username()
    auth_page.enter_correct_password()
    auth_page.click_login_button()
    auth_page.successful_login()


def test_unsuccessful_login(auth_page):
    auth_page.enter_uncorrect_username()
    auth_page.enter_correct_password()
    auth_page.click_login_button()
    auth_page.unsuccessful_login()


def test_logout(auth_page_input_data, main_page):
    main_page.click_main_button()
    time.sleep(3)
    auth_page_input_data.click_logout_button()
    time.sleep(3)
    auth_page_input_data.visible_login_button()
