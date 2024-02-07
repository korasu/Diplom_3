from selenium.webdriver.common.by import By


class OrderFeedLocators:
    order_feed_header = By.XPATH, ".//h1[text()='Лента заказов']"
    first_order = By.XPATH, ".//a[@class='OrderHistory_link__1iNby']"
    popup_with_order_info = By.XPATH, (".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X "
                                       "p-10']")
    number_first_order = By.XPATH, ".//p[@class='text text_type_digits-default']"
    count_orders_for_all_time = By.XPATH, ".//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    count_orders_in_day = By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]"
    order_in_work = By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"
