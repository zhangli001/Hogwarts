from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDaKa:

    def setup(self):
        # 定义了一个字典
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"
        caps['hk   '] = 'true'
        caps['skipDeviceInitialization'] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        # 进入【工作台】页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()

        # 找到“打卡”入口，并且点击进入
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()

        # 定位“外出打卡”tab，切换到外出打卡页面
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        # 进行外出打卡操作
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        # 显式等待,验证是否打卡成功
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)

