"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from bu.cart import Cart


class TestCart:
    def setup_class(self):
        self.cart = Cart()

    def test_create(self):
        r = self.cart.create()
        assert r["errmsg"] == "成功"
        assert r["errno"] == 0
