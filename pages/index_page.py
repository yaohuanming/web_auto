from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cust_manage_page import CustManagePage
from pages.medicine_manage_page import MedicineManagePage
from pages.order_manage_page import OrderManagePage


class IndexPage(BasePage):
    customer_menu = (By.CSS_SELECTOR, '[href="#/customers"]')
    medicine_menu = (By.CSS_SELECTOR, '[href="#/medicines"]')
    order_menu = (By.CSS_SELECTOR, '[href="#/orders"]')

    def to_customer_menu(self):
        self.click_element(self.customer_menu)
        return CustManagePage(self.driver)

    def to_medicine_menu(self):
        self.click_element(self.medicine_menu)
        return MedicineManagePage(self.driver)

    def to_order_menu(self):
        self.click_element(self.order_menu)
        return OrderManagePage(self.driver)