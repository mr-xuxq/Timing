#——————修改个人资料页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Edit_personal_info(BaseAction):
    #头像按钮
    myimgBtn = By.ID,'com.huiian.timing:id/avatar_img'
    #姓名按钮
    nameBtn = By.XPATH,'//*[@text="姓名"]'
    #性别按钮
    genderBtn = By.XPATH,'//*[@text="性别"]'
    #生日按钮
    birthdayBtn = By.XPATH,'//*[@text="生日"]'
    #学习标签按钮
    identityBtn = By.XPATH,'//*[@text="学习标签"]'
    #个人描述按钮
    miaoshuBtn = By.XPATH,'//*[@text="个人描述"]'
    #定义修改后的昵称
    nameNew = By.XPATH,'//*[@text="new name"]'
    #滑动选择性别弹窗右上角的【完成】按钮
    genderSubmit = By.XPATH,'//*[@text="完成"]'
    #右上角的【保存】按钮
    infoSubmit = By.XPATH,'//*[@text="保存"]'

    def click_myimg(self):
        self.click(self.myimgBtn)
    def click_name(self):
        self.click(self.nameBtn)
    def click_gender(self):
        self.click(self.genderBtn)
    def click_birthday(self):
        self.click(self.birthdayBtn)
    def click_genderSubmit(self):
        self.click(self.genderSubmit)
    def click_infoSubmit(self):
        self.click(self.infoSubmit)
    def swipeByGender(self):
        self.swipeOperat(0.5, 0.93, 0.5, 0.79, 150)