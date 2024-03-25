import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from time import sleep


@pytest.fixture()
def clear_data(get_webdriver):
    driver = get_webdriver
    # 登录
    index_page = LoginPage(driver).login()
    # 进入订单管理页面，删除所有订单
    omp = index_page.to_order_menu()
    while driver.find_elements(*omp.delete_btn):
        omp.delete_order()
        sleep(0.5)
    # 进入客户管理页面，删除所有客户
    cmp = index_page.to_customer_menu()
    while driver.find_elements(*cmp.delete_btn):
        cmp.delete_customer()
        sleep(0.5)
    # 进入药品管理页面，删除所有药品
    mmp = index_page.to_medicine_menu()
    while driver.find_elements(*mmp.delete_btn):
        mmp.delete_medicine()
        sleep(0.5)


class TestOrderManagePage:

    def test_add_order_success(self, get_webdriver, clear_data):
        driver = get_webdriver

        # 登录
        index_page = LoginPage(driver).login()
        # 进入客户管理页面，添加客户
        cmp = index_page.to_customer_menu()
        cmp.add_customer('南京中医院1', '2551867851', '江苏省-南京市-秦淮区-汉中路-501')
        cmp.add_customer('南京中医院2', '2551867852', '江苏省-南京市-秦淮区-汉中路-502')
        cmp.add_customer('南京中医院3', '2551867853', '江苏省-南京市-秦淮区-汉中路-503')
        # 进入药品管理页面，添加药品
        mmp = index_page.to_medicine_menu()
        mmp.add_medicine('青霉素盒装1', 'YP-32342341', '青霉素注射液，每支15ml，20支装')
        mmp.add_medicine('青霉素盒装2', 'YP-32342342', '青霉素注射液，每支15ml，30支装')
        mmp.add_medicine('青霉素盒装3', 'YP-32342343', '青霉素注射液，每支15ml，40支装')
        # 进入订单管理页面，添加订单
        omp = index_page.to_order_menu()
        omp.add_order('新订单', '南京中医院2', '青霉素盒装1', 100)
        # 断言
        assert driver.find_element(By.XPATH, '//span[text()="订单："]/following-sibling::span').text == '新订单'
