import requests
import unittest
import json


class BaseRequest():
    def send_post(self, url, data):
        '''
        ��װpost����ʽ
        '''
        res = requests.post(url=url, data=data).text
        return res

    def send_get(self, url, data):
        '''
        ��װget����ʽ
        '''
        res = requests.get(url=url, parames=data).text
        return res

    def run_main(self, method, url, data):
        '''
        ͨ��methodֵ�жϷ�����һ�����͵�����
        '''
        if method == 'post':
            res = self.send_post(url, data)
            return res
        else:
            res = self.send_get(url, data)
            return res
        try:
            res = json.load(res)
            print(type(res))
        except:
            print("��������һ��text")

        return res

    def login_by_phone(self):
        url = 'http://101.37.27.140:8083/login-register/login-by-phone'
        data = {
            "phone": "10000000017",
            "password": "111111"
        }
        method = 'post'
        res = self.run_main(method, url, data)
        res = json.loads(res)
        return res['userKey']


baserequest = BaseRequest()

if __name__ == '__main__':
    print(baserequest.login_by_phone())



