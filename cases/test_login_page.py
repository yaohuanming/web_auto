import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class TestLoginPage:

    def test_login_success(self, get_webdriver):
        driver = get_webdriver

        lp = LoginPage(driver)
        lp.login()
        # 断言
        assert driver.find_element(By.CSS_SELECTOR, '.sidebar-menu > li:nth-child(2)').text == '客户'
        assert driver.find_element(By.CSS_SELECTOR, '.sidebar-menu > li:nth-child(3)').text == '药品'
        assert driver.find_element(By.CSS_SELECTOR, '.sidebar-menu > li:nth-child(4)').text == '订单'

    @pytest.mark.parametrize('login_info',
                             [('', '88888888', '请输入用户名'),
                              ('byhy', '', '请输入密码'),
                              ('byh', '88888888', '登录失败 : 用户名或者密码错误'),
                              ('byhy', '8888888', '登录失败 : 用户名或者密码错误'),
                              ('byhy', '888888888', '登录失败 : 用户名或者密码错误')])
    def test_login_failure(self, get_webdriver, login_info):
        driver = get_webdriver
        username, password, expected = login_info

        lp = LoginPage(driver)
        alert_text = lp.login_failure(username, password)
        assert expected == alert_text
