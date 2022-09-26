# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/19 
Desc：
'''

import pytest
import allure
import time
from selenium import webdriver
import os
from os.path import dirname


@allure.testcase("https://www.baidu.com的搜索功能")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    with allure.step('step one:打开浏览器'):
        a = dirname(dirname(__file__)) +os.sep+ '/driver/chromedriver'
        print(a)
        # driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\testframework\\frameworkDemo\\driver\\chromedriver')
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com')

    with allure.step('step two:在搜索栏输入allure,并点击百度一下'):
        driver.find_element('id', 'kw').send_keys(test_data1)
        time.sleep(1)
        driver.find_element('id', 'su').click()
        time.sleep(1)

    with allure.step('step three:截图保存到项目中'):
        driver.save_screenshot('./result/b.png')
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head><body> 首页</body>', 'Attach with HTML type', allure.attachment_type.HTML)

    with allure.step('step four:关闭浏览器'):
        driver.quit()


if __name__ == '__main__':
    pytest.main(['--alluredir=./report/', 'test_allure_screen.py'])
    os.system('allure serve ./report')
