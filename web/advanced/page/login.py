"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.main import Main


class Login(BasePage):
    _BASE_URL = "http://litemall.hogwarts.ceshiren.com/vue/index.html#/login?redirect=user"
    _ELEMENTS_USER_NAME= (By.CSS_SELECTOR, "input[name='user']")
    _ELEMENTS_USER_PASSWORD=(By.CSS_SELECTOR, "input[name='password']")

    def login(self):
        self.find(self._ELEMENTS_USER_NAME).send_keys("user123")
        self.find(self._ELEMENTS_USER_PASSWORD).send_keys("user123")
        self.find(By.CSS_SELECTOR, ".van-button").click()
        return Main(self.driver)