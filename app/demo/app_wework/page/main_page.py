from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from app.app_wework.page.addresslist_page import AddressListPage
from app.app_wework.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def goto_message(self):
        """
        进入到消息页面
        :return:
        """
        pass

    def goto_address(self):
        # self.driver.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录']")

        return AddressListPage(self.driver)
