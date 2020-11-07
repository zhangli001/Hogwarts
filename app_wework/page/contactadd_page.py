"""
编辑联系人页面
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

# from app.app_wework.page.memberinvitemenu_page import MemberInviteMenuPage
from app.app_wework.page.base_page import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_contract(self, name, gender, phonenum):
        self.find(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(name)
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")

        if gender == "男":
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.find_and_click(MobileBy.XPATH, "//*[@text='男']")
        else:
            self.find_and_click(MobileBy.XPATH, "//*[@text='女']")

        self.find(MobileBy.XPATH,
                  '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//android.widget.EditText').send_keys(
            phonenum)
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        from app.app_wework.page.memberinvitemenu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
