"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from bu.litemall_api import LitemallApi


class Cart(LitemallApi):
    def create(self):
        url = "/wx/cart/add"
        r = self.lite_mall_req("post", url, json={"goodsId": 1181648, "number": 1, "productId": 892})
        return r
