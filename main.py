from selenium import webdriver
from time import sleep

service = webdriver.ChromeService(executable_path='C:/selenium_driver/chromedriver.exe')
wd = webdriver.Chrome(service=service)

wd.maximize_window()
wd.get('https://www.baidu.com')
sleep(5)
