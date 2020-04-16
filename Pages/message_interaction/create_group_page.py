#——————创建学习群页面——————#
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Create_group(BaseAction):
    # 学习讨论小组
    discussTeam = By.ID, 'com.huiian.timing:id/team_type_1'
    # 打卡群
    recordTeam = By.ID, 'com.huiian.timing:id/team_type_2'
    #【下一布】
    nextStep = By.ID,'com.huiian.timing:id/activity_banner_right_tv'
#---------------------------------------------------------------------------------
    #讨论组_发起讨论选择道友页面
    chooseFriend = By.ID,'com.huiian.timing:id/friend_cb'
    chooseFriendDo = By.ID,'com.huiian.timing:id/activity_banner_right_tv'
    createdDiscussTeam = By.ID,'com.huiian.timing:id/iv_team'
 # ---------------------------------------------------------------------------------
    # 讨论组_发起讨论选择道友页面
    choiceGroupPhoto = By.ID, 'com.huiian.timing:id/choice_group_photo_iv'
    teamName = By.ID, 'com.huiian.timing:id/team_name_et'
    introTeam = By.ID, 'com.huiian.timing:id/team_intro_et'
    recordTeamSuccess = By.ID,'com.huiian.timing:id/activity_banner_next_ll'


    def click_discussTeam(self):
        self.click(self.discussTeam)
    def click_nextStep(self):
        self.click(self.nextStep)
    def click_chooseFriend(self):
        self.click(self.chooseFriend)
    def click_chooseFriendDo(self):
        self.click(self.chooseFriendDo)

    def click_recordTeam(self):
        self.click(self.recordTeam)
    def click_choiceGroupPhoto(self):
        self.click(self.choiceGroupPhoto)
    def click_recordTeamSuccess(self):
        self.click(self.recordTeamSuccess)
    def input_tearmName(self,text):
        self.input(self.teamName,text)
    def input_introTeam(self,text):
        self.input(self.introTeam,text)

    def waitAndfind_createdDiscussTeam(self):
        if self.waitLoading(self.createdDiscussTeam, t=2) == True:
            return True
        else:
            return False