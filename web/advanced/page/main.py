"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.featured import Featured


class Main(BasePage):
    def goto_featured(self):
        self.find(By.CSS_SELECTOR, ".van-tabbar-item").click()
        return Featured(self.driver)