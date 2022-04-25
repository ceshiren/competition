"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from protocol.http_protocol import HttpProtocol


class LitemallApi:

    def __init__(self):

        self.base_url = "http://litemall.hogwarts.ceshiren.com"

    def lite_mall_req(self, method, url , **kwargs):
        """
        一些与litemall产品强相关，但是和具体业务逻辑无关的封装
        :return:
        """
        # **kwargs 代表接口的不定长参数，比如headers
        if kwargs.get("headers"):
        # 如果传递过来的请求有头信息，那么我们就在头信息中做追加
            kwargs["headers"]["X-Litemall-Token"] = f"{self.get_token()}"
        else:
            # 如果传递过来的请求没有header
            kwargs["headers"] = {"X-Litemall-Token": f"{self.get_token()}"}
        # 传递塞入headers 的请求信息， 在发起请求的时候将基地址和传入的url的path进行拼接
        r = HttpProtocol.request(method, self.base_url+url, **kwargs)
        return r


    def get_token(self):
        url = self.base_url+"/wx/auth/login"
        body_data = {
            "username": "user123",
            "password": "user123"
        }
        r = HttpProtocol.request("post", url, json=body_data)
        token = r.get("data").get("token")
        return token
