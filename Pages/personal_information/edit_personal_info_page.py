#——————修改个人资料页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Edit_personal_info(BaseAction):
    #头像按钮
    myimgBtn = By.ID,'com.huiian.timing:id/change_avatar_tv'
    #更换照片
    changephoto = By.ID,'com.huiian.timing:id/change_avatar_tv'
    #点击更换照片后返回
    return1 = By.ID,'com.huiian.timing:id/activity_banner_back_iv'
    #点击选择照片
    chosephoto = By.ID,'com.huiian.timing:id/avatar_img'
    #点击选取
    selection = By.ID,'com.huiian.timing:id/tv_crop_select'
    #删除输入框的姓名
    deletenamme = By.ID,'android:id/inputArea'
    #姓名输入框
    nameContentBox = By.ID,'com.huiian.timing:id/name_rl'


    #姓名按钮
    nameBtn = By.ID,'com.huiian.timing:id/name_tv'
    #性别按钮
    genderBtn = By.XPATH,'//*[@text="性别"]'

    #生日按钮
    birthdayBtn = By.XPATH,'//*[@text="生日"]'
    #学习标签按钮
    identityBtn = By.XPATH,'//*[@text="学习标签"]'
    #个人描述按钮
    miaoshuBtn = By.XPATH,'//*[@text="个人描述"]'
    #定义修改后的昵称
    name = By.XPATH,'//*[@text="new name"]'
    #滑动选择性别弹窗右上角的【完成】按钮
    genderSubmit = By.XPATH,'//*[@text="完成"]'
    #右上角的【保存】按钮
    infoSubmit = By.XPATH,'//*[@text="保存"]'
    #右上角的【后退】按钮
    backBtn = By.ID,'com.huiian.timing:id/activity_banner_back_iv'
    # 修改姓名后右上角【确定】按钮
    determine = By.ID,'com.huiian.timing:id/activity_banner_right_tv'
    # 点击姓名输入框
    namexiu = By.ID, 'com.huiian.timing:id/name_et'
    def click_myimg(self):
        self.click(self.myimgBtn)
    def click_changephoto(self):
        self.click(self.changephoto)
    def click_chosephoto(self):
        self.click(self.chosephoto)
    def click_selection(self):
        self.click(self.selection)
    def click_nameContentBox(self):
        self.click(self.nameContentBox)

    def click_deletename(self):
        self.click(self.deletenamme)

    def input_namexiu(self):
        self.input(self.namexiu)

    def click_determine(self):
        self.click(self.determine)
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
    def click_back(self):
        self.click(self.backBtn)
    def swipeByGender(self):
        self.swipeOperat(0.5, 0.93, 0.5, 0.79, 150)

    def input_name(self):
        self.input(self.nameContentBox)

    def tapScreen(self,x,y):
        L = self.getSize()
        self.driver.tap([(L[0]*x,L[1]*y)],1)
    def click_man(self):
        self.click(self.click_man())
    def click_return1(self):
        self.click(self.return1)