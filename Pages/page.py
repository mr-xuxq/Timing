from Pages.personal_information.setting_page import Setting
from Pages.register_login.login_page import Login
from Pages.register_login.login_phone_page import Login_phone
from Pages.register_login.login_phone_pwd_page import Login_phone_pwd
from Pages.register_login.login_phone_captcha_page import Login_phone_captcha
from Pages.register_login.register_add_tags_page import Register_add_tags
from Pages.register_login.register_fillInformation_page import Register_fillInformation
from Pages.register_login.selectPhoto_page import SelectPhoto
from Pages.register_login.guide_page import Guide
from Pages.browse_information.shouye_page import Shouye
from Pages.browse_information.sVlog_list_page import List_sVlog
from Pages.browse_information.videoRoom_list_page import VideoRoom_list
from Pages.browse_information.video_hall_page import VideoHall

class Page:

    def __init__(self, driver):
        self.driver = driver

    def setting(self):
        return Setting(self.driver)

    def login(self):
        return Login(self.driver)

    def login_phone(self):
        return Login_phone(self.driver)

    def login_phone_pwd(self):
        return Login_phone_pwd(self.driver)

    def login_phone_captcha(self):
        return Login_phone_captcha(self.driver)

    def register_add_tags(self):
        return Register_add_tags(self.driver)

    def register_fillInformation(self):
        return Register_fillInformation(self.driver)

    def selectPhoto(self):
        return SelectPhoto(self.driver)

    def guide(self):
        return Guide(self.driver)

    def shouye(self):
        return Shouye(self.driver)

    def sVlog_list(self):
        return List_sVlog(self.driver)

    def videoRoom_list(self):
        return VideoRoom_list(self.driver)

    def videoHall(self):
        return VideoHall(self.driver)



    # def more_page(self):
    #     return More(self.driver)
    #
    # def more_page_setting(self):
    #     return More_setting(self.driver)
    #
    # def more_homepage_page(self):
    #     return More_homepage(self.driver)
    #
    # def more_homepage_page_modifyinformation(self):
    #     return More_homepage_modifyinformation(self.driver)
