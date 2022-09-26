# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/22 
Desc：
'''
import time

from appium.webdriver.webdriver import WebDriver
from appium import webdriver

# driver.quit()

class TestAndroidAPP(object):

    driver = WebDriver
    @classmethod
    def setup_class(cls):
        print("setup class")
        cls.init_appium()

    def setup_method(self):
        print("setup method 每个用例执行前执行一次")
        self.driver = self.restart_appium()

    def teardown_method(self):
        print("每个用例执行后执行一次")
        self.driver.quit()

    def test_fee(self):
        time.sleep(10)
        self.driver.find_element_by_xpath("//*[@text='在线缴费']").click()
        time.sleep(5)

    @classmethod
    def init_appium(cls) -> WebDriver:
        caps = {
            "platformName": "Android",
            "platformVersion": "8",
            "deviceName": "demo",
            "appPackage": "com.yunxi.AgileApp",
            "appActivity": "com.basern.MainActivity",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
        return driver

    @classmethod
    def restart_appium(cls) -> WebDriver:
        caps = {
            "platformName": "Android",
            "platformVersion": "8",
            "deviceName": "demo",
            "appPackage": "com.yunxi.AgileApp",
            "appActivity": "com.basern.MainActivity",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)
        return driver

