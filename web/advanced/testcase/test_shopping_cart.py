"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from web.advanced.page.login import Login


class TestShoppingCart:
    def setup_class(self):
        self.login = Login()


    def test_add_shopping_cart(self):
        res = self.login.login().\
            goto_featured().\
            goto_search().\
            search("火焰杯测试商品").\
            goto_shopping_cart().\
            get_product_list()
        assert "火焰杯测试商品" in res

    def teardown_class(self):
        self.login.quit()

