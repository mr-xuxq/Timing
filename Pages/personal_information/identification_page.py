#——————Timing认证页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Identification(BaseAction):
    # 学历认证
    educationalBtn = By.XPATH, '//*[@text="学历认证"]'
    #学历认证_认证专业栏
    professionBtn = By.ID,'com.huiian.timing:id/tv_profession'
    #学历认证_学校全称
    schoolFullNameBtn = By.ID,'com.huiian.timing:id/et_identification_full_name'
    #学历认证_认证信息
    identificationInfoBtn = By.ID,'com.huiian.timing:id/et_identification_info'
    #学历认证_上传学历证明材料
    identificationAddBtn = By.ID,'com.huiian.timing:id/tv_add'
    #学历认证_手持证件照
    photoHandAdd = By.ID,'com.huiian.timing:id/iv_hand'
    #学历认证_手持证件照
    photoFrontAdd = By.ID,'com.huiian.timing:id/iv_front'
    #学历认证_手持证件照
    photobackAdd = By.ID,'com.huiian.timing:id/iv_back'
    #学历认证_提交按钮
    submitBtn = By.ID,'com.huiian.timing:id/btn_submit'

    def click_educational(self):
        self.driver.click(self.educationalBtn)
    def click_profession(self):
        self.driver.click(self.professionBtn)
    def click_schoolFullName(self):
        self.driver.click(self.schoolFullNameBtn)
    def click_identificationInfo(self):
        self.driver.click(self.identificationInfoBtn)
    def click_identificationAdd(self):
        self.driver.click(self.identificationAddBtn)
    def click_photoHand(self):
        self.driver.click(self.photoHandAdd)
    def click_photoFront(self):
        self.driver.click(self.photoFrontAdd)
    def click_photoback(self):
        self.driver.click(self.photobackAdd)
    def click_submit(self):
        self.driver.click(self.submitBtn)
