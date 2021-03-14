#——————编辑个人资料页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Edit_personalData(BaseAction):
    #姓名输入栏
    nameBox = By.ID,'com.huiian.timing:id/et_name'
    #性别栏
    gender = By.ID,'com.huiian.timing:id/gender_rl'
    #生日栏
    birthday = By.ID,'com.huiian.timing:id/birthday_rl'
    #学习标签栏
    studyLabel= By.ID,'com.huiian.timing:id/identity_rl'
    #个人描述输入框
    myDescriptionBox = By.ID,'com.huiian.timing:id/et_desc'
    #保存按钮
    saveBtn = By.ID,'com.huiian.timing:id/activity_banner_right_tv'
    #后退按钮
    backBtn = By.ID,'com.huiian.timing:id/activity_banner_back_ll'
    #修改性别完成按钮
    saveGenderBtn = By.ID,'com.huiian.timing:id/btnSubmit'
    def click_gender(self):
        self.click(self.gender)
    def click_birthday(self):
        self.click(self.birthday)
    def click_studyLabel(self):
        self.click(self.studyLabel)
    def click_saveBtn(self):
        self.click(self.saveBtn)
    def click_backBtn(self):
        self.click(self.backBtn)
    def click_saveGenderBtn(self):
        self.click(self.saveGenderBtn)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)
    def input_nameBox(self,context):
        self.input(self.nameBox,context)
    def input_myDescriptionBox(self,context):
        self.input(self.myDescriptionBox,context)
