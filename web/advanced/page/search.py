"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.product_details import ProductDetails


class Search(BasePage):
    def search(self, search_name):
        self.find(By.CSS_SELECTOR, "form input").clear()
        self.find(By.CSS_SELECTOR, "form input").send_keys(search_name)
        self.find(By.CSS_SELECTOR, ".van-field__control").send_keys(Keys.ENTER)
        self.wait_element_until_clickable(
            (By.CSS_SELECTOR, ".van-card__title")).click()
        return ProductDetails(self.driver)

