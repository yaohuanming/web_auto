from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.index_page import IndexPage


class LoginPage(BasePage):
    url = 'http://127.0.0.1/mgr/sign.html'

    name_input = (By.CSS_SELECTOR, '#username')
    pwd_input = (By.CSS_SELECTOR, '#password')
    submit = (By.CSS_SELECTOR, 'button[type="submit"]')

    # 打开网址
    def open_url(self):
        self.driver.get(self.url)

    # 登录
    def login(self, username='byhy', password='88888888'):
        self.open_url()
        self.type_text(self.name_input, username)
        self.type_text(self.pwd_input, password)
        self.click_element(self.submit)
        return IndexPage(self.driver)

    def login_failure(self, username, password):
        self.open_url()
        self.type_text(self.name_input, username)
        self.type_text(self.pwd_input, password)
        self.click_element(self.submit)
        # 获取alert对象
        alert = self.driver.switch_to.alert
        # 获取提示信息
        alert_text = alert.text
        # 关闭提示框
        alert.accept()
        # 返回提示信息
        return alert_text
