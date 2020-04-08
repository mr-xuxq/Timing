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

    def click_personInfo(self,target):
        self.click(target)
    #上滑更多页面至计时区域
    def swipeByMy(self,x1, y1, x2, y2, t):
        self.swipeOperat(x1, y1, x2, y2, t)

    def waitAndfind(self, target, t):
        if self.waitLoading(target, t) == True:
            return True
        else:
            return False