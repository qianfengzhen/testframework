# coding=utf-8
'''
Author: qianfengzhen
Email: qianfengzhen@cvte.com
Version: V1.0.0
Date: 2022/9/19 
Desc：
'''
import logging
import os
import allure
import pytest

def test_with_no_severity():
    logging.debug('这是测试没有severity的日志')
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    logging.info('这是trivial_severity的日志')
    pass

@allure.severity(allure.severity_level.BLOCKER)
def test_with_normal_severity():
    logging.info('这是normal_severity的日志')
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity():
    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_override(self):
        pass


if __name__ == '__main__':
    pytest.main(['--alluredir','./result', 'test_allure_severity.py'])
    os.system('allure serve ./result')
