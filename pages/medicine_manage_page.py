from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MedicineManagePage(BasePage):
    # 新增
    add_btn = (By.CSS_SELECTOR, 'button[type="button"]')
    medicine_name_input = (By.XPATH, '//div[text()="药品名称"]/input')  # 新增、修改共用
    medicine_id_input = (By.XPATH, '//div[text()="编号"]/input')  # 新增、修改共用
    description_input = (By.XPATH, '//div[text()="描述"]/textarea')  # 新增、修改共用
    confirm_add_btn = (By.XPATH, '//button[text()="创建"]')
    cancel_add_bth = (By.XPATH, '//button[text()="取消"]')

    # 修改
    modify_btn = (By.XPATH, '//label[text()="编辑"]')
    confirm_modify_btn = (By.XPATH, '//label[text()="确定"]')
    cancel_modify_btn = (By.XPATH, '//label[text()="取消"]')

    # 删除
    delete_btn = (By.XPATH, '//label[text()="删除"]')

    def add_medicine(self, medicine_name, medicine_id, description):
        self.click_element(self.add_btn)
        self.type_text(self.medicine_name_input, medicine_name)
        self.type_text(self.medicine_id_input, medicine_id)
        self.type_text(self.description_input, description)
        self.click_element(self.confirm_add_btn)
        # 手动关闭页面
        self.click_element(self.cancel_add_bth)

    def delete_medicine(self):
        self.click_element(self.delete_btn)
        # 确认删除
        self.driver.switch_to.alert.accept()
