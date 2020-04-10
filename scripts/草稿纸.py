#——————手机号/qq/微信登录页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
phoneBtn =By.ID,'com.huiian.timing:id/ll_lbp'

print(phoneBtn[1])
    #
    # def check_phone(self):
    #     try:
    #         self.driver.find_element_by_id('')
    #     except Exception as e:
    #         return False
    #     else:
    #         return True
    #     # self.is_feature_exist(self.phoneBtn)
    #     # return  self.find_element(self.phoneBtn,timeout=2, poll=1)
