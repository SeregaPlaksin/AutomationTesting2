class LocatorsAuth:
    LOGIN = '.input_error[name="user-name"]'
    PASS = 'form>div:nth-child(2) .input_error'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MESSAGE = '.error-message-container'
    LOGOUT = '#logout_sidebar_link'


class LocatorsMain:
    TITLE = '.header_secondary_container span.title'
    INVENTORY_LIST = '.pricebar>button'
    BUTTON_MENU = 'div>.bm-burger-button >button'
    BUTTON_MENU_ALL_ITEMS = '#inventory_sidebar_link'


class LocatorsCart:
    ADD_TO_CARD = '.btn.btn_primary'
    SHOPPING_CART = '.shopping_cart_link'
    SHOPPING_CART_BADGE = '.shopping_cart_badge'
    SHOPPING_CART_INVENTORY = '.inventory_item_name'
    SHOPPING_CART_INVENTORY2 = '.inventory_item_name'
    ADD_TO_CART_INVENTORY = '#add-to-cart-sauce-labs-backpack'
    CHECKOUT = '#checkout'


class LocatorsSort:
    SORT_CONTAINER = '.product_sort_container'
    INVENTORY_PRICE = '.inventory_item_price'
    INVENTORY_NAME = '.inventory_item_name'
    PRICE_SORT_LTH = 'Price (low to high)'
    PRICE_SORT_HTL = 'Price (high to low)'


