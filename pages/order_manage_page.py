from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderManagePage(BasePage):
    # 新增
    add_btn = (By.CSS_SELECTOR, 'button[type="button"]')
    order_name_input = (By.XPATH, '//div[text()="订单名称"]/input')  # 新增、修改共用
    customer_select = (By.XPATH, '//div[text()="客户"]/select')  # 新增、修改共用
    medicine_name_select = (By.XPATH, '//div[text()="药品（数量）："]/select')  # 新增、修改共用
    medicine_number_input = (By.CSS_SELECTOR, '[type="number"]')
    confirm_add_btn = (By.XPATH, '//button[text()="创建"]')
    cancel_add_bth = (By.XPATH, '//button[text()="取消"]')

    # 删除
    delete_btn = (By.XPATH, '//label[text()="删除"]')

    def add_order(self, order_name, customer, medicine_name, medicine_number):
        self.click_element(self.add_btn)
        self.type_text(self.order_name_input, order_name)
        self.select_item(self.customer_select, customer)

        self.select_item(self.medicine_name_select, medicine_name)
        self.type_text(self.medicine_number_input, medicine_number)

        self.click_element(self.confirm_add_btn)
        # 手动关闭页面
        self.click_element(self.cancel_add_bth)

    def delete_order(self):
        self.click_element(self.delete_btn)
        # 确认删除
        self.driver.switch_to.alert.accept()
