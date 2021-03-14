# ——————————————————————-——-browse_information——————————-——————-———-—-——#
from Pages.browse_information.discover_page import Discover
from Pages.browse_information.follow_page import Follow
from Pages.browse_information.sVlog_list_page import List_sVlog
from Pages.browse_information.free_studyRoom_seat_page import Free_studyRoom_seat
from Pages.browse_information.free_studyRoom_page import Free_studyRoom
from Pages.browse_information.pay_studyRoom_page import Pay_studyRoom
from Pages.browse_information.free_studyRoom_house_page import Free_studyRoom_house
from Pages.browse_information.daily_page import Daily
from Pages.browse_information.tree_hole_page import Tree_hole
from Pages.browse_information.match_friend_page import Match_friend
# ———————————————————————————-Message_interaction—————-—————————————-——#
from Pages.message_interaction.shouye_page import Shouye
from Pages.message_interaction.choose_image_page import Choose_image
from Pages.message_interaction.friend_chat_page import Friend_chat
from Pages.message_interaction.group_chat_page import Group_chat
from Pages.message_interaction.video_record_page import Video_record
from Pages.message_interaction.create_group_page import Create_group
# ——————————————————————————-Personal_information———————————-——————-—-——#
from Pages.personal_information.more_page import More
from Pages.personal_information.setting_page import Setting
from Pages.personal_information.edit_personalData_page import Edit_personalData
from Pages.personal_information.person_home_page import Person_home
from Pages.personal_information.small_more_page import Small_more
# ——————————————————————-—————-Post_content————————————————————-—-——#
from Pages.post_content.post_page import Post
from Pages.post_content.post_diary_page import Post_diary
from Pages.post_content.select_diary_photo_page import Select_diary_photo
from Pages.post_content.select_diary_topic_page import Select_diary_topic
from Pages.post_content.select_cover_page import Select_cover
# ———————————————————————————-Register_login————————————————-———-—-——#
from Pages.register_login.login_page import Login
from Pages.register_login.login_phone_page import Login_phone
from Pages.register_login.login_phone_pwd_page import Login_phone_pwd
from Pages.register_login.login_phone_captcha_page import Login_phone_captcha
from Pages.register_login.register_add_tags_page import Register_add_tags
from Pages.register_login.register_fillInformation_page import Register_fillInformation
from Pages.register_login.selectPhoto_page import Select_photo
from Pages.register_login.binding_phone_page import Banding_phone
from Pages.register_login.guide_page import Guide
# —————————————————————————————-Timed_learning—————-————————————-—-——#
from Pages.timed_learning.timing_page import Timing
from Pages.timed_learning.activity_page import Activity
from Pages.timed_learning.classic_timing_page import Classic_timing
from Pages.timed_learning.tomato_timing_page import Tomato_timing
from Pages.timed_learning.video_timing_page import Video_timing
from Pages.timed_learning.farm_timing_page import Farm_timing
from Pages.timed_learning.friend_timing_page import Firend_timing
from Pages.timed_learning.getup_sleep_page import Getup_sleep
#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

class Page:
    def __init__(self, driver):
        self.driver = driver
# ——————————————————————-——-browse_information——————————-——————-———-—-——#
    def discover(self):
        return Discover(self.driver)

    def follow(self):
        return Follow(self.driver)

    def sVlog_list(self):
        return List_sVlog(self.driver)

    def free_studyRoom_seat(self):
        return Free_studyRoom_seat(self.driver)

    def free_studyRoom(self):
        return Free_studyRoom(self.driver)

    def Pay_studyRoom(self):
        return Pay_studyRoom(self.driver)

    def free_studyRoom_house(self):
        return Free_studyRoom_house(self.driver)

    def daily(self):
        return Daily(self.driver)
        
    def tree_hole(self):
        return Tree_hole(self.driver)

    def match_friend(self):
        return Match_friend(self.driver)
# ———————————————————————————-Message_interaction—————-—————————————-——#
    def shouye(self):
        return Shouye(self.driver)

    def choose_image(self):
        return Choose_image(self.driver)


    def friend_chat(self):
        return Friend_chat(self.driver)

    def group_chat(self):
        return Group_chat(self.driver)

    def video_record(self):
        return Video_record(self.driver)

    def create_group(self):
        return Create_group(self.driver)
# ——————————————————————————-Personal_information———————————-—————-—-——#
    def more(self):
        return More(self.driver)

    def setting(self):
        return Setting(self.driver)

    def edit_personalData(self):
        return Edit_personalData(self.driver)

    def person_home(self):
        return Person_home(self.driver)

    def small_more(self):
        return Small_more(self.driver)
# ——————————————————————-—————-Post_content————————————————————-—-——#
    def post(self):
        return Post(self.driver)

    def post_diary(self):
        return Post_diary(self.driver)

    def select_diary_photo(self):
        return Select_diary_photo(self.driver)

    def select_diary_topic(self):
        return Select_diary_topic(self.driver)

    def select_cover(self):
        return Select_cover(self.driver)
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

    def banding_phone(self):
        return Banding_phone(self.driver)

    def guide(self):
        return Guide(self.driver)
# —————————————————————————————-Timed_learning—————-————————————-—-——#
    def timing(self):
        return Timing(self.driver)

    def activity(self):
        return Activity(self.driver)

    def classic_timing(self):
        return Classic_timing(self.driver)

    def tomato_timing(self):
        return Tomato_timing(self.driver)

    def video_timing(self):
        return Video_timing(self.driver)

    def farm_timing(self):
        return Farm_timing(self.driver)

    def firend_timing(self):
        return Firend_timing(self.driver)

    def getup_sleep(self):
        return Getup_sleep(self.driver)