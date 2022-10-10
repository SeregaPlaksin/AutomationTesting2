
class Locators:
    # Auth
    LOGIN = '.input_error[name="user-name"]'
    PASS = 'form>div:nth-child(2) .input_error'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MESSAGE = '.error-message-container'
    LOGOUT = '#logout_sidebar_link'

    # MAIN
    TITLE = '.header_secondary_container span.title'
    BASKET = '.shopping_cart_link'
    BASKET_CHECKOUT = '.cart_footer .btn.btn_action'
    CHECKOUT = '#checkout'


    BUTTON_MENU = 'div>.bm-burger-button >button'
    BUTTON_MENU_ALL_ITEMS = '#inventory_sidebar_link'
    SORT_CONTAINER = '.product_sort_container'
    INVENTORY_PRICE = '.inventory_item_price'
    PRICE_SORT_LTH = 'Price (low to high)'
