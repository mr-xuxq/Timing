#——————注册的填写个人信息页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Register_fillInformation(BaseAction):
    # 【选择照片按钮】
    selectPhotoBtn =By.ID,'com.huiian.timing:id/iv_avatar'
    # 【昵称填写框】
    nickNameBox =By.ID,'com.huiian.timing:id/et_name'
    # 【男性按钮】
    genderBtn =By.ID,'com.huiian.timing:id/tv_male'
    # 【出生年月按钮】
    brithdayBtn =By.ID,'com.huiian.timing:id/tv_birth'
    # 【确定按钮】
    okBtn =By.ID,'com.huiian.timing:id/tv_ok'
    # 【生成学习档案】
    generateBtn = By.ID, 'com.huiian.timing:id/tv_commit'
    # 【目标】
    target =By.ID, 'com.huiian.timing:id/message_img'


    def click_selectPhotoBtn(self):
        self.click(self.selectPhotoBtn)

    def input_nickNameBox(self,content):
        self.input(self.nickNameBox,content)

    def click_genderBtn(self):
        self.click(self.genderBtn)

    def set_brithday(self):
        self.click(self.brithdayBtn)
        for i in range(1,10):
            self.swipeOperat(0.35,0.93,0.35,0.78,500)
            self.swipeOperat(0.78, 0.93, 0.78, 0.78, 500)
        self.click(self.okBtn)

    def click_generateBtn(self):
        self.click(self.generateBtn)

    def waitAndFind(self):
        if  self.waitLoading(self.target,t=20) == True:
            return True
        else:
            return False
