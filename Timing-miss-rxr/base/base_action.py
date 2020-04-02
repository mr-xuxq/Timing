from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import Base
import time

class BaseAction(Base):

    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def find_element(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def get_text(self, feature):
        return self.find_element(feature).text

    def is_feature_exist(self, feature):
        try:
            self.find_element(feature)
            return True
        except TimeoutException:
            return False

    def is_toast_exist(self, message):
        """
        根据 部分内容，判断toast是否存在
        :param message: 部分内容
        :return: 是否存在
        """
        message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
        try:
            self.find_element(message_xpath, 5, 0.1)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message):
        """
        根据 部分内容，获取toast上的所有内容
        :param message: 部分内容
        :return: 所有内容
        """
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
            return self.find_element(message_xpath, 5, 0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确或toast有没有出现在屏幕上")

    # 键盘操作，“4”代表返回键。
    def press_back(self):
        self.driver.press_keycode(4)

    #自己封装：在t时间内是否能找到元素
    def waitLoading(self,target,t):
        i = 0
        global consult
        while i < t:
            consult = BaseAction.is_feature_exist(self,target)
            if consult == False:
                time.sleep(1)
                i = i + 1
            else:
                return True

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

    # def tapAction(self, m, n):
    #     l = self.getSize()
    #     xt = int(l[0] * m)
    #     yt = int(l[1] * n)
    #     #print(xt, yt)
    #     self.driver.tap([(xt, yt)])

    # def scroll_page_one_time(self, direction="down"):
    #     """
    #     滑动一次屏幕
    #     :param direction: 方向
    #         "up"：从下往上
    #         "down"：从上往下
    #         "right"：从左往右
    #         "left"：从右往左
    #     :return:
    #     """
    #     width = self.driver.get_window_size()["width"]
    #     height = self.driver.get_window_size()["height"]
    #
    #     center_x = width / 2
    #     center_y = height / 2
    #
    #     left_x = width / 4 * 1
    #     left_y = center_y
    #     right_x = width / 4 * 3
    #     right_y = center_y
    #
    #     top_x = center_x
    #     top_y = height / 4 * 1
    #     bottom_x = center_x
    #     bottom_y = height / 4 * 3
    #
    #     if direction == "up":
    #         self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
    #     elif direction == "down":
    #         self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
    #     elif direction == "left":
    #         self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
    #     elif direction == "right":
    #         self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
    #     else:
    #         raise Exception("请检查参数是否正确，up/down/left/right")
    #
    # def find_element_with_scroll(self, feature, direction):
    #     """
    #     = "up"
    #     边滑边找 某个元素的特征
    #     :param feature: 元素的特征
    #     :param direction: 方向
    #         "up"：从下往上
    #         "down"：从上往下
    #         "right"：从左往右
    #         "left"：从右往左
    #     :return:
    #     """
    #     page_source = ""
    #     while True:
    #         try:
    #             return self.find_element(feature)
    #         except Exception:
    #
    #             self.scroll_page_one_time(direction)
    #
    #             if self.driver.page_source == page_source:
    #                 print("到底了")
    #                 break
    #             page_source = self.driver.page_source
    #
    # def is_keyword_in_page_source(self, keyword, timeout=10, poll=0.1):
    #     """
    #     如果 keyword 在 page_source 中，那么返回 True
    #     如果 keyword 不在 page_source 中，那么返回 False
    #     :param keyword: 关键的字符串
    #     :param timeout: 超时时间，默认为10秒
    #     :param poll: 频率，默认为0.1秒
    #     :return:
    #     """
    #
    #     # 结束时间
    #     end_time = time.time() + timeout
    #
    #     while True:
    #         # 如果结束时间大于当前时间，那么就认为超时了
    #         if end_time < time.time():
    #             return False
    #         if keyword in self.driver.page_source:
    #             return True
    #
    #         time.sleep(poll)

    #
    # #找元素方法，如果没找到则滑动页面
    # def swipeAndFind(self,target,t):
    #     while True:
    #         try:
    #             #如果在规定时间找到该元素，则跳出循环
    #             if self.driver.waitLoading(target,t):
    #                 break
    #             #如果没有找到，向上滑动页面继续找
    #             else:
    #                 self.swipeOperat(0.5,0.7,0.5,0.3,150)
    #         except Exception:
    #             return False



