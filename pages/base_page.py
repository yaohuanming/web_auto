from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def type_text(self, locator, *args):
        self.driver.find_element(*locator).send_keys(*args)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def clear_text(self, locator):
        self.driver.find_element(*locator).clear()

    def select_item(self, locator, item_name):
        Select(self.driver.find_element(*locator)).select_by_visible_text(item_name)
