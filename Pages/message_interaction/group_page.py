#——————群组页——————
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Group(BaseAction):
    # 群内部的tab页
    groupTab = By.ID, 'com.huiian.timing:id/tv_tab_title'
    # tab群聊
    groupTalk = By.XPATH, '//*[@text="群聊"]'