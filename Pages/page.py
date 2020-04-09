# ——————————————————————-——-browse_information——————————-——————-———-—-——#
from Pages.browse_information.shouye_page import Shouye
from Pages.browse_information.sVlog_list_page import List_sVlog
from Pages.browse_information.video_room_list_page import Video_room_list
from Pages.browse_information.video_hall_page import Video_hall
from Pages.browse_information.video_room_page import Video_room
from Pages.browse_information.daily_page import Daily
# ———————————————————————————-Message_interaction—————-—————————————-——#
from Pages.message_interaction.chat_chooseImage_page import Choose_image
from Pages.message_interaction.chat_chooseVideo_page import Choose_video
from Pages.message_interaction.friend_chat_page import Friend_chat
from Pages.message_interaction.group_page import Group
from Pages.message_interaction.message_page import Message
from Pages.message_interaction.create_group_page import Create_group
# ——————————————————————————-Personal_information———————————-——————-—-——#
from Pages.personal_information.more_page import More
from Pages.personal_information.setting_page import Setting
from Pages.personal_information.editPersonInfo_page import Edit_personal_info
from Pages.personal_information.nameInfo_page import Name_info
from Pages.personal_information.person_home_page import Person_home
from Pages.personal_information.follow_page import Follow
from Pages.personal_information.identification_page import Identification
# ——————————————————————-—————-Post_content————————————————————-—-——#
from Pages.post_content.publish_page import Post_content
# ———————————————————————————-Register_login————————————————-———-—-——#
from Pages.register_login.login_page import Login
from Pages.register_login.login_phone_page import Login_phone
from Pages.register_login.login_phone_pwd_page import Login_phone_pwd
from Pages.register_login.login_phone_captcha_page import Login_phone_captcha
from Pages.register_login.register_add_tags_page import Register_add_tags
from Pages.register_login.register_fillInformation_page import Register_fillInformation
from Pages.register_login.selectPhoto_page import Select_photo
from Pages.register_login.guide_page import Guide
# —————————————————————————————-Timed_learning—————-————————————-—-——#
from Pages.timed_learning.timing_page import Timing

#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

class Page:
    def __init__(self, driver):
        self.driver = driver
# ——————————————————————-——-browse_information——————————-——————-———-—-——#
    def shouye(self):
        return Shouye(self.driver)

    def sVlog_list(self):
        return List_sVlog(self.driver)

    def video_room_list(self):
        return Video_room_list(self.driver)

    def video_hall(self):
        return Video_hall(self.driver)

    def video_room(self):
        return Video_room(self.driver)

    def daily(self):
        return Daily(self.driver)
# ———————————————————————————-Message_interaction—————-—————————————-——#
    def choose_image(self):
        return Choose_image(self.driver)

    def choose_video(self):
        return Choose_video(self.driver)

    def friend_chat(self):
        return Friend_chat(self.driver)

    def group(self):
        return Group(self.driver)

    def message(self):
        return Message(self.driver)

    def create_group(self):
        return Create_group(self.driver)
# ——————————————————————————-Personal_information———————————-——————-—-——#
    def more(self):
        return More(self.driver)

    def setting(self):
        return Setting(self.driver)

    def edit_personal_info(self):
        return Edit_personal_info(self.driver)

    def name_info(self):
        return Name_info(self.driver)

    def person_home(self):
        return Person_home(self.driver)

    def follow(self):
        return Follow(self.driver)

    def identification(self):
        return Identification(self.driver)
# ——————————————————————-—————-Post_content————————————————————-—-——#
    def post_content(self):
        return Post_content(self.driver)
# ———————————————————————————-Register_login————————————————-———-—-——#
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

    def select_photo(self):
        return Select_photo(self.driver)

    def guide(self):
        return Guide(self.driver)
# —————————————————————————————-Timed_learning—————-————————————-—-——#
    def timing(self):
        return Timing(self.driver)