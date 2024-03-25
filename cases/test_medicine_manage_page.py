from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class TestMedicineManagePage:
    def test_add_medicine_success(self, get_webdriver):
        driver = get_webdriver
        medicine_name = '药品名称'
        medicine_id = 'ID12312313213'
        description = '药品描述'

        lp = LoginPage(driver)
        # 登录并进入药品管理页面
        mmp = lp.login().to_medicine_menu()
        # 新增一个药品
        mmp.add_medicine(medicine_name, medicine_id, description)

        # 断言：药品列表第一项结果中药品名、编号、描述信息都是正确的
        assert driver.find_element(By.XPATH, '//span[text()="药品："]/following-sibling::span').text == medicine_name
        assert driver.find_element(By.XPATH, '//span[text()="编号："]/following-sibling::span').text == medicine_id
        assert driver.find_element(By.XPATH, '//span[text()="描述："]/following-sibling::span').text == description
