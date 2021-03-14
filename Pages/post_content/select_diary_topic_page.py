#——————发布日记的话题详情页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Select_diary_topic(BaseAction):
    # 【话题编辑框】
    editTopicBox =By.ID,'com.huiian.timing:id/add_trending_edit'
    # 【关闭按钮】
    closetBtn =By.ID,'com.huiian.timing:id/activity_banner_left_tv'
    # 【完成按钮】
    nextBtn =By.ID,'com.huiian.timing:id/activity_banner_right_tv'
    # 【已有话题选择_默认选择第一位】
    selectTipicBtn =By.ID,'com.huiian.timing:id/tv_content'

    def click_closetBtn(self):
        self.click(self.closetBtn)
    def click_next(self):
        self.click(self.nextBtn)
    def click_selectTipic(self):
        self.click(self.selectTipicBtn)

    def input_topic(self, content):
        self.input(self.editTopicBox,content)