from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CustManagePage(BasePage):
    # 新增
    add_btn = (By.CSS_SELECTOR, 'button[type="button"]')
    cust_name_input = (By.XPATH, '//div[text()="客户名"]/input')  # 新增、修改共用
    tel_input = (By.XPATH, '//div[text()="联系电话"]/input')  # 新增、修改共用
    addr_input = (By.CSS_SELECTOR, 'textarea')  # 新增、修改共用
    confirm_add_btn = (By.XPATH, '//button[text()="创建"]')
    cancel_add_bth = (By.XPATH, '//button[text()="取消"]')

    # 修改
    modify_btn = (By.XPATH, '//label[text()="编辑"]')
    confirm_modify_btn = (By.XPATH, '//label[text()="确定"]')
    cancel_modify_btn = (By.XPATH, '//label[text()="取消"]')

    # 删除
    delete_btn = (By.XPATH, '//label[text()="删除"]')

    def add_customer(self, name, tel, addr):
        self.click_element(self.add_btn)
        self.type_text(self.cust_name_input, name)
        self.type_text(self.tel_input, tel)
        self.type_text(self.addr_input, addr)
        self.click_element(self.confirm_add_btn)
        # 手动关闭页面
        self.click_element(self.cancel_add_bth)

    def modify_customer(self, name):
        self.click_element(self.modify_btn)
        # 修改客户名称
        self.clear_text(self.cust_name_input)
        self.type_text(self.cust_name_input, name)

        self.click_element(self.confirm_modify_btn)

    def delete_customer(self):
        self.click_element(self.delete_btn)
        # 确认删除
        self.driver.switch_to.alert.accept()
