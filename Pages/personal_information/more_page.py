#——————更多页01——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class More(BaseAction):
    # 【个人信息按钮】
    personalInformation = By.ID, 'com.huiian.timing:id/tv_nickname'
    # 【timingID】
    timingID = By.ID, 'com.huiian.timing:id/tv_timing_id'
    # 【二维码】
    QRcode = By.ID, 'com.huiian.timing:id/iv_qr_code'
    # 图书馆按钮
    libraryBtn = By.XPATH, '//*[@text="图书馆"]'
    # 创建学习群按钮
    creatGroup = By.XPATH, '//*[@text="创建学习群"]'
    # 起床/睡觉打卡按钮
    getupAndSleepBtn = By.XPATH, '//*[@text="起床/睡觉打卡"]'
    # 自律工具
    studyToolBtn = By.XPATH, '//*[@text="自律工具"]'
    # 树洞对讲机
    treeHole = By.XPATH, '//*[@text="树洞对讲机"]'
    # 更多小按钮
    smallMore = By.XPATH, '//*[@text="更多"]'
    # 【设置按钮】
    settingBtn = By.ID, 'com.huiian.timing:id/tv_setting'
    # 【扫一扫】
    scanQRcode = By.ID, 'com.huiian.timing:id/tv_scan'

    def click_personalInformation(self):
        self.click(self.personalInformation)
    def click_timingID(self):
        self.click(self.timingID)
    def click_QRcode(self):
        self.click(self.QRcode)
    def click_libraryBtn(self):
        self.click(self.libraryBtn)
    def click_creatGroup(self):
        self.click(self.creatGroup)
    def click_getupAndSleepBtn(self):
        self.click(self.getupAndSleepBtn)
    def click_studyToolBtn(self):
        self.click(self.studyToolBtn)
    def click_treeHole(self):
        self.click(self.treeHole)
    def click_smallMore(self):
        self.click(self.smallMore)
    def click_settingBtn(self):
        self.click(self.settingBtn)
    def click_scanQRcode(self):
        self.click(self.scanQRcode)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)
    def swipeUp(self):
        self.swipeOperat(0.5,0.8,0.5,0.2,500)
    def swipeByTime(self):
        self.swipeOperat(0.6, 0.8, 0.6, 0.74, 500)