import requests
import unittest
import json
from Api.base_api import BaseRequest
class Login(BaseRequest):
    def login_by_phone(self,phone):
        url = 'http://101.37.27.140:8083/login-register/login-by-phone'
        data = {
            "phone": phone,
            "password": "111111"
        }
        method = 'post'
        res = self.run_main(method, url, data)
        res = json.loads(res)
        return res#['userKey']
    def reset_password(self,phone,captcha,password):
        url = 'http://118.178.104.233:8080/timingServer/user/resetPasswordByPhone'
        data = {
            "phone": phone,
            "captcha": captcha,
            "password": password
        }
        method = 'post'
        res = self.run_main(method, url, data)
        res = json.loads(res)
        return res#['userKey']

# if __name__ == '__main__':
#     print(Login().reset_password(phone=10000000017,captcha=820701,password=111111))