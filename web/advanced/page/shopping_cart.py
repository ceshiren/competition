"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from web.advanced.page.base_page import BasePage
from web.advanced.utils.log_utils import logger


class ShoppingCart(BasePage):
    def get_product_list(self):
        res = self.finds(By.CSS_SELECTOR, ".van-card__title")
        res_text = [i.text for i in res]
        logger.info(f"购物车的商品有{res_text}")
        return res_text
