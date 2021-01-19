from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import Base
import time
sourse = []

class BaseAction(Base):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=15, poll=1):
        """
        根据特征，找元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value))
        return element

    # 点击操作
    def click(self, feature):
        self.find_element(feature).click()

    # 输入
    def input(self, feature, content):
        self.find_element(feature).send_keys(content)

    def get_text(self, feature):
        return self.find_element(feature).text


    # 清空
    def clear(self, feature):
        self.find_element(feature).clear()

    # 键盘操作，“4”代表返回键。
    def press_back(self):
        self.driver.press_keycode(4)

    # 键盘操作，“66”代表回车键
    def press_enter(self):
        self.driver.press_keycode(66)

    #滑动
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipeOperat(self,x1, y1, x2, y2, t):
        l = self.getSize()
        X1 = int(l[0] * x1)
        X2 = int(l[0] * x2)
        Y1 = int(l[1] * y1)
        Y2 = int(l[1] * y2)
        self.driver.swipe(X1, Y1, X2, Y2, t)

    def clickOperat(self, x1, y1, x2, y2, t):
        l = self.getSize()
        X1 = int(l[0] * x1)
        X2 = int(l[0] * x2)
        Y1 = int(l[1] * y1)
        Y2 = int(l[1] * y2)
        self.driver.tap([(X1, Y1), (X2, Y2)], t)

    def tapOperat(self, x, y):
        l = self.getSize()
        X= int(l[0] * x)
        Y= int(l[1] * y)
        self.driver.tap([(X,Y)],1)

    #判断元素是否在当前页面内
    def is_feature_exist(self, feature):
        try:
            self.find_element(feature)
        except Exception as e:
            return False
        else:
            return True


    def waitLoading(self, target, t):
        i = 0
        global consult
        while i < t:
            consult = BaseAction.is_feature_exist(self, target)
            if consult == False:
                time.sleep(1)
                i = i + 1
            else:
                return True