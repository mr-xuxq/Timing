from Pages.login_page import Login
from Pages.login_phone_page import Login_phone
from Pages.login_phone_pwd_page import Login_phone_pwd
from Pages.main_page import Main
from Pages.message_page import Message
from Pages.chat_page import Chat
from Pages.chooseImage_page import ChooseImage
from Pages.chooseVideo_page import ChooseVideo
from Pages.more_page import More
from Pages.timing_page import Timing
from Pages.person_page import Person
from Pages.personInfo_page import PersonInfo
from Pages.nameInfo_page import NameInfo


class Page:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        return Login(self.driver)

    def login_phone(self):
        return Login_phone(self.driver)

    def login_phone_pwd(self):
        return Login_phone_pwd(self.driver)

    def main(self):
        return Main(self.driver)

    def message(self):
        return Message(self.driver)

    def chat(self):
        return Chat(self.driver)

    def chooseImage(self):
        return ChooseImage(self.driver)

    def chooseVideo(self):
        return ChooseVideo(self.driver)

    def more(self):
        return More(self.driver)

    def timing(self):
        return Timing(self.driver)

    def person(self):
        return Person(self.driver)

    def personInfo(self):
        return PersonInfo(self.driver)

    def nameInfo(self):
        return NameInfo(self.driver)
