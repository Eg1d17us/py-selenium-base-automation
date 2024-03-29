class LoginPageLocators:
    logo = "//div[@class='login_logo']"
    user_name_input = "//input[@id='user-name']"
    pass_input = "//input[@id='password']"
    login_btn = "//input[@id='login-button']"


class HomePageLocators:
    products_page_title = "//*[contains(text(),'Products')]"
    product_tile = "//*[@class='inventory_item']"
    side_menu_items = "//a[@class='bm-item menu-item']"
    random_add_to_cart_btn = "(//button[contains(.,'Add to cart')])[{}]"
    add_to_cart_btn = "//button[contains(.,'Add to cart')]"
    random_remove_from_cart_btn = "(//button[contains(.,'Remove')])[{}]"
    remove_from_cart_btn = "//button[contains(.,'Remove')]"
    cart_btn = "//a[@class='shopping_cart_link']"
    hamburger_btn = "//button[@id='react-burger-menu-btn']"
    logout_btn = "//a[@id='logout_sidebar_link']"
    close_side_menu_btn = "//button[@id='react-burger-cross-btn']"
    about_btn = "//a[text()='About']"
    twitter_btn = "//a[contains(text(),'Twitter')]"
    facebook_btn = "//a[contains(text(),'Facebook')]"
    linkedin_btn = "//a[contains(text(),'LinkedIn')]"
    product_sort_btn = "//select[@class='product_sort_container']"
    copyright_txt = "//div[@class='footer_copy']"
    cart_badge = "//span[@class='shopping_cart_badge']"
    product_names = "//a/div[@class='inventory_item_name ']"
    product_prices = "//div[@class='inventory_item_price']"


class CartPageLocators:
    cart_page_title = "//*[contains(text(),'Your Cart')]"
    first_name_input = "//input[@id='first-name']"
    last_name_input = "//input[@id='last-name']"
    zip_postal_input = "//input[@id='postal-code']"
    checkout_btn = "//button[@id='checkout']"
    continue_btn = "//input[@id='continue']"
    checkout_overview_page_title = "//*[contains(text(),'Checkout: Overview')]"
    finish_btn = "//button[@id='finish']"


class CheckoutCompleteLocators:
    checkout_complete_page_title = "//*[contains(text(),'Checkout: Complete!')]"
    checkmark_img = "//img[@alt='Pony Express']"
    thanks_header = "//h2[contains(text(), 'Thank you')]"
    description_text = "//div[contains(text(), 'Your order has been dispatched')]"
