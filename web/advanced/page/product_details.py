"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from web.advanced.page.base_page import BasePage
from web.advanced.page.shopping_cart import ShoppingCart


class ProductDetails(BasePage):
    def goto_shopping_cart(self):
        self.wait_element_until_clickable(
            (By.CSS_SELECTOR, ".van-goods-action-button--first")).click()
        self.wait_element_until_clickable(
            (By.CSS_SELECTOR, ".van-button--warning")).click()
        self.wait_element_until_clickable(
            (By.CSS_SELECTOR, ".van-goods-action-icon")).click()
        return ShoppingCart(self.driver)