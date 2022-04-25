"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from web.advanced.page.base_page import BasePage
from web.advanced.page.search import Search


class Featured(BasePage):
    def goto_search(self):
        self.wait_element_until_clickable(
            (By.CSS_SELECTOR, ".van-field__control")).click()
        return Search(self.driver)