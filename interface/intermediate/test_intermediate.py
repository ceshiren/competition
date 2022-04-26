"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests


class TestIntermediate:
    def setup_class(self):
        self.base_url = "http://litemall.hogwarts.ceshiren.com"

    def test_begginner(self):
        # 第一个请求
        r = requests.post(self.base_url+"/wx/auth/login",
                          json={"username": "user123", "password": "user123"})
        token = r.json()["data"]["token"]
        # 第二个请求
        r2 = requests.post(self.base_url+"/wx/cart/add",
                           headers={"X-Litemall-Token": token},
                           json={"goodsId": 1181648, "number": 1, "productId": 892})
        assert r2.json()["errmsg"] == "成功"
        assert r2.json()["errno"] == 0