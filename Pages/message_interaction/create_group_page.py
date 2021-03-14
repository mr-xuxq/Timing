#——————创建学习群页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Create_group(BaseAction):
    # 【后退按钮】
    backBtn = By.ID, 'com.huiian.timing:id/iv_back'
# ---------------------------------------------------------------------------------
    # 【与道友群聊按钮】
    friendChatBtn = By.ID, 'com.huiian.timing:id/tv_friend_group'
    # 【选择道友】
    selectFriend = By.ID, '	com.huiian.timing:id/iv_select'
    #【立即创建按钮】
    createNow = By.ID,'com.huiian.timing:id/tv_create_btn'
#---------------------------------------------------------------------------------
    # 【与粉丝群聊按钮】
    fansChatBtn = By.ID, 'com.huiian.timing:id/tv_fans_group'
    # 【粉丝群后退按钮】
    fansBackBtn = By.ID, 'com.huiian.timing:id/activity_banner_back_iv'
    # 【群封面按钮】
    groupCover = By.ID,'com.huiian.timing:id/iv_select_avatar'
    # 【群名称按钮】
    groupNameBtn = By.ID,'com.huiian.timing:id/cl_group_name'
    # 【群验证按钮】
    groupVerify = By.ID,'com.huiian.timing:id/cb_verify'
    # 【下一步按钮】
    nextStep = By.ID,'com.huiian.timing:id/activity_banner_right_tv'
# ---------------------------------------------------------------------------------
    # 【群名称后退按钮】
    groupNameBackBtn = By.ID,'com.huiian.timing:id/activity_banner_back_ll'
    # 【群名称栏】
    groupNameBox = By.ID,'com.huiian.timing:id/et_name'
    # 【确定按钮】
    yesBtn = By.ID,'com.huiian.timing:id/activity_banner_right_tv'

    def click_backBtn(self):
        self.click(self.backBtn)
    def click_friendChatBtn(self):
        self.click(self.friendChatBtn)
    def click_selectFriend(self):
        self.click(self.selectFriend)
    def click_createNow(self):
        self.click(self.createNow)
    def click_fansChatBtn(self):
        self.click(self.fansChatBtn)
    def click_fansBackBtn(self):
        self.click(self.fansBackBtn)
    def click_groupCover(self):
        self.click(self.groupCover)
    def click_groupName(self):
        self.click(self.groupNameBtn)
    def click_groupVerify(self):
        self.click(self.groupVerify)
    def click_nextStep(self):
        self.click(self.nextStep)
    def click_groupNameBackBtn(self):
        self.click(self.groupNameBackBtn)
    def click_yesBtn(self):
        self.click(self.yesBtn)
    def tapScreen(self, x, y):
        self.tapOperat(x, y)
    def input_groupName(self,text):
        self.input(self.groupNameBox,text)