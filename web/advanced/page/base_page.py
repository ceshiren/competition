"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _BASE_URL = ""
    def __init__(self, base_driver=None):
        if base_driver:
            self.driver = base_driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)

        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)

    def back_to(self):
        self.driver.get(self._BASE_URL)
        self.driver.refresh()


    def find(self, by, locator=None):
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def finds(self, by, locator=None):
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def wait_element_until_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        self.driver.quit()


