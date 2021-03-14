#——————更多页02——————#
#coding:utf-8
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Small_more(BaseAction):
    # 【学习Live】
    studyLive = By.XPATH, '//*[@text="学习Live"]'
    # 【学习记录】
    studyRecord = By.XPATH, '//*[@text="学习记录"]'
    # 【发布/投稿】
    postDiary = By.XPATH, '//*[@text="发布/投稿"]'
    # 【我的网盘】
    myDisk = By.XPATH, '//*[@text="我的网盘"]'
    # 【我的账户】
    myAccount = By.XPATH, '//*[@text="我的账户"]'
    # 【我的课程】
    myCourse = By.XPATH, '//*[@text="我的课程"]'

    def click_studyLive(self):
        self.click(self.studyLive)
    def click_studyRecord(self):
        self.click(self.studyRecord)
    def click_postDiary(self):
        self.click(self.postDiary)
    def click_myDisk(self):
        self.click(self.myDisk)
    def click_myAccount(self):
        self.click(self.myAccount)
    def click_myCourse(self):
        self.click(self.myCourse)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)