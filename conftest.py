import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def get_webdriver():
    # setUp
    service = webdriver.ChromeService(executable_path='C:/selenium_driver/chromedriver.exe')
    wd = webdriver.Chrome(service=service)
    wd.maximize_window()  # 窗口最大化
    wd.implicitly_wait(5)  # 隐式等待
    yield wd  # 返回WebDriver对象

    # tearDown
    wd.quit()  # 关闭浏览器
