from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class TestCustManagePage:
    def test_add_cust_success(self, get_webdriver):
        driver = get_webdriver
        name = '南京中医院'
        tel = '15352222222'
        addr = '南京中医院的地址'

        lp = LoginPage(driver)
        # 登录并进入客户管理页面
        cmp = lp.login().to_customer_menu()
        # 新增一个客户
        cmp.add_customer(name, tel, addr)

        # 断言：客户列表第一项结果中客户名、电话、地址信息都是正确的
        assert driver.find_element(By.XPATH, '//span[text()="客户名："]/following-sibling::span').text == name
        assert driver.find_element(By.XPATH, '//span[text()="联系电话："]/following-sibling::span').text == tel
        assert driver.find_element(By.XPATH, '//span[text()="地址："]/following-sibling::span').text == addr

    def test_modify_cust_success(self, get_webdriver):
        driver = get_webdriver
        name = '南京中医院'
        tel = '15352222222'
        addr = '南京中医院的地址'
        new_name = '南京省中医院'

        lp = LoginPage(driver)
        # 登录并进入客户管理页面
        cmp = lp.login().to_customer_menu()
        # 新增一个客户
        cmp.add_customer(name, tel, addr)
        # 修改客户名
        cmp.modify_customer(new_name)

        # 断言：客户列表第一项结果中客户名、电话、地址信息都是正确的
        assert driver.find_element(By.XPATH, '//span[text()="客户名："]/following-sibling::span').text == new_name
        assert driver.find_element(By.XPATH, '//span[text()="联系电话："]/following-sibling::span').text == tel
        assert driver.find_element(By.XPATH, '//span[text()="地址："]/following-sibling::span').text == addr
