"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest

from page.login import Login


class TestShoppingCart:
    def setup_class(self):
        self.login = Login()
        self.main = self.login.login()


    def teardown(self):
        self.main.back_to()




    @pytest.mark.parametrize('product_name',  ["火焰杯测试商品", "查询测试"] )
    def test_add_shopping_cart(self, product_name):
        res = self.main.\
            goto_featured().\
            goto_search().\
            search(product_name).\
            goto_shopping_cart().\
            get_product_list()
        assert product_name in res

    def teardown_class(self):
        self.login.quit()

