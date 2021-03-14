#——————编辑学习标签页——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Study_label(BaseAction):
    # 后退按钮
    backBtn = By.ID,'com.huiian.timing:id/activity_banner_back_ll'
    # 完成按钮
    finshBtn = By.ID,'com.huiian.timing:id/tv_enter_timing'
    # 删除学习标签按钮
    deleteStudyLabel = By.ID,'com.huiian.timing:id/iv_close'
    # 中考标签
    zhongKaoLabel = By.XPATH,'//*[@text="中考"]'
    # 更多按钮
    moreBtn = By.ID,'com.huiian.timing:id/tv_want_exam_more'
    #自定义学习标签
    editLabelBtn = By.ID,'com.huiian.timing:id/tv_go_custom'
    #自定义标签编辑框
    editLabelBox = By.ID,'com.huiian.timing:id/et'
    #自定义标签选择
    selectLabel = By.ID,'com.huiian.timing:id/recyclerview'

    def click_backBtn(self):
        self.click(self.backBtn)
    def click_finshBtn(self):
        self.click(self.finshBtn)
    def click_deleteStudyLabel(self):
        self.click(self.deleteStudyLabel)
    def click_zhongKaoLabel(self):
        self.click(self.zhongKaoLabel)
    def click_moreBtn(self):
        self.click(self.moreBtn)
    def click_editLabelBtn(self):
        self.click(self.editLabelBtn)
    def click_selectLabel(self):
        self.click(self.selectLabel)
    def tapScreen(self,x,y):
        self.tapOperat(x,y)
    def input_editLabelBox(self,context):
        self.input(self.editLabelBox,context)
